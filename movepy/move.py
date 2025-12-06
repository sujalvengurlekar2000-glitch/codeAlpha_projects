import os
import shutil

# Source folder: change this to your folder path
source_folder = r"c:\Users\tejal\OneDrive\Desktop\internship\hangman"

# Destination folder where .jpg files will be moved
destination_folder = r"c:\Users\tejal\OneDrive\Desktop\internship\hangman\images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Count moved files
moved_count = 0

# Loop through all files in the folder
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, dest_path)
        moved_count += 1
        print(f"Moved: {file_name}")

print(f"\nDone! Total .jpg files moved: {moved_count}")
