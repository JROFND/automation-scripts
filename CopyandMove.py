import shutil
import os
from datetime import datetime
import glob
import re

# Define source and destination
source_folder = 'C:/Users/'
destination_folder = r"W:\"
pattern = "*.xlsx"

# Get today's date
today = datetime.today().date()

# Search for matching files
search_pattern = os.path.join(source_folder, pattern)
all_matching_files = glob.glob(search_pattern)

# Filter files modified today
matching_files = [
    f for f in all_matching_files
    if datetime.fromtimestamp(os.path.getmtime(f)).date() == today
]

def copy_then_move_files_handle_duplicates(file_list, destination_folder):
    """
    Copies files to the destination folder and deletes the original only if the copy is successful.
    Handles duplicates by renaming the file if it already exists in the destination.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_path in file_list:
        try:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, file_name)

            # Handle duplicates
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(file_name)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                file_name = f"{base}_{timestamp}{ext}"
                destination_path = os.path.join(destination_folder, file_name)

            # Copy the file
            shutil.copy2(file_path, destination_path)

            # Verify the copy was successful
            if os.path.exists(destination_path):
                os.remove(file_path)
                print(f"Copied and removed original: {file_name}")
            else:
                print(f"Copy failed for: {file_name}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Call the function
copy_then_move_files_handle_duplicates(matching_files, destination_folder)

