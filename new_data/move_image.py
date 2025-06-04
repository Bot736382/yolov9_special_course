import os
import shutil

def move_images(text_file, dest_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    # Read the list of image numbers
    with open(text_file, 'r') as file:
        image_numbers = [line.strip() for line in file]

    # Loop through and move each image
    for image_number in image_numbers:
        image_filename = f"{image_number}.jpg"
        source_image_path = os.path.join('./', image_filename)
        destination_image_path = os.path.join(dest_folder, image_filename)

        if os.path.exists(source_image_path):
            shutil.move(source_image_path, destination_image_path)
            print(f"Moved {image_filename} to {dest_folder}")
        else:
            print(f"{image_filename} not found in the source folder.")

# Move train, test, and val images
move_images('../ImageSets/Main/train.txt', './train/')
move_images('../ImageSets/Main/test.txt', './test/')
move_images('../ImageSets/Main/val.txt', './val/')		
