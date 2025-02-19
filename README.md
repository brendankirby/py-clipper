# Clipping Script

py-clipper is a Python-based command-line tool that automates the creation of video clips from a single MP4 video file using timestamps recorded in a text file. 
It leverages `ffmpeg` to trim the video based on provided timestamps and saves the resulting clips in a dedicated directory.

## Features

- **Automatic File Detection:**  
  - Expects exactly one MP4 video file and one TXT file (with timestamps) in the current directory.

- **Timestamp Parsing:**  
  - Reads timestamps in `hh:mm:ss` format from the TXT file.
  - Supports optional notes after the timestamp to generate a custom filename.
  - Cleans up filenames by removing invalid characters.

- **Clip Generation:**  
  - Automatically calculates the clip start time by subtracting 10 seconds from the recorded timestamp (without going below zero).
  - Generates clips of a fixed duration (120 seconds) using `ffmpeg` with a copy codec for fast processing.

- **Organized Output:**  
  - Saves all generated clips in a "Clips" folder located in your Downloads directory.
  - If a "Clips" folder already exists, creates a new folder with an incremented name (e.g., "Clips (1)").

## Usage

1. **Prerequisites:**
   - Install Python 3 on your system.
   - Ensure `ffmpeg` is installed and accessible from the command line.

2. **Prepare Your Files:**
   - Place the script, one MP4 video file, and one TXT file with timestamps (formatted as `hh:mm:ss - Note` where the note is optional) in the same directory.

3. **Run the Script:**
   - Open a terminal and navigate to the directory containing your files.
   - Run the script using:
     ```bash
     python clipping_script.py
     ```
   - The script will process the video, create clips based on the timestamps, and automatically open the output folder where the clips are saved.

4. **Review Your Clips:**
   - The generated clips will be saved in a "Clips" folder in your Downloads directory. If a folder already exists, a new folder with an incremented name is created.
