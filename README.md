# File Organizer Script

This Python script automatically organizes files on your desktop into designated folders based on their file types. It continuously monitors the desktop for new files and moves them to appropriate categories such as Images, Videos, Documents, and more.

## Features
- **Automatic Organization**: Files are automatically sorted into folders based on their extensions.
- **File Type Support**: Supports a variety of file types, including:
  - Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg
  - Videos: .mp4, .mkv, .flv, .avi, .mov, .wmv
  - Audio: .mp3, .wav, .aac, .flac, .ogg
  - Documents: .pdf, .docx, .txt, .xlsx, .pptx, .csv
  - Archives: .zip, .tar, .gz, .rar
  - Scripts: .py, .js, .html, .css, .sh

## Requirements
Before running the script, ensure you have the following installed:
- **Python 3.x**

## How to Use

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Rayyan-Grey/Desktop-File-Organizer.git

2. Navigate to the Project Directory: Change to the directory where the script is located:

    ```bash
    cd Desktop-File-Organizer
    ```
3. Run the Script: Execute the Python script:
   ```bash
   python File-Organizer.py
   ```
4. Manual Organization: The script will also move any existing files present on the Desktop into their respective folders upon starting.

## How It Works

- The script continuously monitors the specified WATCHED_DIR (your Desktop) for new files.

- When a new file is detected, it checks the file type and moves it to the corresponding folder under DESTINATION_DIR (specified as "Main" on your Desktop).

- The monitoring checks occur every 5 seconds.

## Contributing
- Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
