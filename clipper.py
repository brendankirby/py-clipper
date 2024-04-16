import os
import subprocess
import re

def read_timestamps(timestamps_file):
    timestamps = []
    with open(timestamps_file, 'r') as file:
        for line in file:
            line = line.strip()
            match = re.match(r'^(\d{2}:\d{2}:\d{2})\s+(?:-\s*(.*))$', line)
            if match:
                timestamp, note = match.groups()
                filename = note.strip().replace(' ', '_') if note else timestamp.replace(':', '.')
                filename = re.sub(r'[^\w\s.-]', '', filename)  # Remove invalid characters from filename
                timestamps.append((timestamp, filename))
    return timestamps

def find_file(directory, extension):
    files = [file for file in os.listdir(directory) if file.endswith(extension)]
    if len(files) != 1:
        raise ValueError(f"There should be exactly one {extension} file in the directory.")
    return files[0]

def create_clips(video_file, timestamps):
    output_dir = os.path.join(os.path.expanduser("~/Downloads"), "Clips")

    # If the Clips directory already exists, find the next available name
    i = 1
    while os.path.exists(output_dir):
        output_dir = os.path.join(os.path.expanduser("~/Downloads"), f"Clips ({i})")
        i += 1

    # Create the Clips directory
    os.makedirs(output_dir)

    # Open the clips directory
    subprocess.run(["open", output_dir])

    # Create clips
    for index, (timestamp, filename) in enumerate(timestamps, start=1):
        start_time = f"{max(0, int(timestamp[:2]) - 10):02d}:{timestamp[3:]}"
        clip_name = f"{filename}.mp4"
        clip_path = os.path.join(output_dir, clip_name)

        # Trim video using ffmpeg
        cmd = ['ffmpeg', '-i', video_file, '-ss', start_time, '-t', '120', '-c', 'copy', clip_path]
        print(f"\nCreating Clip {index}: {clip_name}")
        print("Executing command:", " ".join(cmd))  # Log ffmpeg command being executed
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"\nClips saved to {output_dir}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    video_file = find_file(current_directory, '.mp4')
    timestamps_file = find_file(current_directory, '.txt')

    timestamps = read_timestamps(timestamps_file)
    create_clips(video_file, timestamps)
