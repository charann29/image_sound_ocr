from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import os


def image_to_sound(image_path, output_sound_path="sound.mp3"):
    """
    Converts an image to speech audio by extracting text from the image
    and converting it to sound.
    
    :param image_path: Path to the image file.
    :param output_sound_path: Path where the sound file will be saved.
    :return: True if successful, False otherwise.
    """
    try:
        # Open and process the image
        with Image.open(image_path) as img:
            decoded_text = image_to_string(img)
            cleaned_text = " ".join(decoded_text.splitlines())

        if cleaned_text.strip():
            print(f"Extracted text: {cleaned_text}")
            sound = gTTS(cleaned_text, lang="en")
            sound.save(output_sound_path)
            print(f"Sound saved to {output_sound_path}")
            return True
        else:
            print("No text found in the image.")
            return False

    except Exception as error:
        print(f"An error occurred: {error}")
        return False


def process_images_in_directory(directory_path):
    """
    Processes all image files in a directory, converting each to a sound file.
    
    :param directory_path: Path to the directory containing image files.
    """
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory_path, filename)
            sound_filename = os.path.splitext(filename)[0] + ".mp3"
            sound_path = os.path.join(directory_path, sound_filename)
            success = image_to_sound(image_path, sound_path)
            if success:
                print(f"Processed {filename} successfully.\n")
            else:
                print(f"Failed to process {filename}.\n")


if __name__ == "__main__":
    directory = "images"  # Change this to your directory path
    process_images_in_directory(directory)
    input("Press Enter to exit...")
