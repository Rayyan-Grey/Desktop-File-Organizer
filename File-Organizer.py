import os
import shutil
import time
import threading

# Path to your Desktop (where files are located)
WATCHED_DIR = r"C:\Users\hp\Desktop"
# Path to your Main folder (where files will be moved and organized)
DESTINATION_DIR = r"C:\Users\hp\Desktop\Main"

# Define file type categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
}

def organize_file(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Determine the file category based on the extension
    file_category = None
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            file_category = category
            break
    
    if not file_category:
        # If the file type doesn't fit a specific category, move it to 'Others'
        file_category = "Others"
    
    # Create the target directory based on the file category
    target_dir = os.path.join(DESTINATION_DIR, file_category)
    os.makedirs(target_dir, exist_ok=True)  # Ensure the folder exists
    
    # Move the file to the appropriate category folder
    try:
        shutil.move(file_path, os.path.join(target_dir, os.path.basename(file_path)))
        print(f"Moved file: {os.path.basename(file_path)} to {target_dir}")
    except Exception as e:
        print(f"Error moving {os.path.basename(file_path)}: {e}")

def move_files():
    # Check all files currently in the Desktop directory
    for filename in os.listdir(WATCHED_DIR):
        file_path = os.path.join(WATCHED_DIR, filename)

        # Check if it's a file (ignore folders)
        if os.path.isfile(file_path):
            # Organize the file based on its type
            organize_file(file_path)

def track_directory():
    # Start with an empty set of tracked files
    tracked_files = set(os.listdir(WATCHED_DIR))
    
    while True:
        time.sleep(5)  # Check every 5 seconds
        
        # Get the current files in the Desktop directory
        current_files = set(os.listdir(WATCHED_DIR))
        
        # Find newly added files (files that are in current but not in tracked)
        new_files = current_files - tracked_files
        
        for new_file in new_files:
            file_path = os.path.join(WATCHED_DIR, new_file)
            if os.path.isfile(file_path):  # Ensure it's a file
                organize_file(file_path)  # Organize and move the file
        
        # Update the tracked files
        tracked_files = current_files

def run_in_background():
    # Run the file moving process in a background thread
    tracker_thread = threading.Thread(target=track_directory)
    tracker_thread.daemon = True
    tracker_thread.start()

if __name__ == "__main__":
    # Ensure the destination directory exists
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)

    print(f"Tracking directory: {WATCHED_DIR}")
    print(f"Moving files to: {DESTINATION_DIR}")
    print("Running in the background...")
    
    # First, move any existing files
    move_files()
    
    # Then, start tracking for new files
    run_in_background()
    
    # Keep the script running
    while True:
        time.sleep(60)
