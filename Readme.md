# Video Processing Project

This project processes a video file using OpenCV to apply various image processing techniques and save the output as a new video file. The script displays multiple processed versions of each frame (e.g., grayscale, HLS, HSV, etc.) and logs the process for debugging.

## Prerequisites

- Python 3.6 or higher
- A video file (e.g., Demo.mp4) to process
- pip (Python package manager)

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Create a Virtual Environment

Create a virtual environment named venv to isolate project dependencies.

python -m venv venv

### 2. Activate the Virtual Environment

Activate the virtual environment to ensure dependencies are installed locally.

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

After activation, you should see (venv) in your terminal prompt.

### 3. Install Required Package

Install the opencv-python package, which is required for video processing.

pip install opencv-python

### 4. Update Video Path

The script (Video_processing.py) references a video file at the following path:

video_path = '/path/to/your/video/Demo.mp4'

Before running the script, update the video_path variable in Video_processing.py to point to the location of your Demo.mp4 file. For example:

video_path = '/home/user/videos/Demo.mp4'  # Replace with your actual video file path

To edit the file:
1. Open Video_processing.py in a text editor.
2. Locate the line video_path = '/path/to/your/video/Demo.mp4'.
3. Replace /path/to/your/video/Demo.mp4 with the absolute path to your video file.

### 5. Run the Script

Run the video processing script:

python Video_processing.py

## What the Script Does

- Loads the video from the specified video_path.
- Applies various image processing techniques (e.g., grayscale, HLS/HSV color spaces, adaptive thresholding, edge detection, Gaussian blur, histogram equalization).
- Displays the processed frames in separate windows.
- Saves the processed video as processed_video.mp4 in the same directory.
- Logs processing details to video_processing.log.

## Notes

- Ensure your video file (Demo.mp4) is accessible at the specified path.
- Press q while the video windows are open to stop processing early.
- The script requires a valid video file to run successfully. If the file is missing or inaccessible, an error will be logged and displayed.

## Troubleshooting

- If you encounter issues with opencv-python, ensure it is installed correctly by running pip show opencv-python.
- Verify the video file path is correct and the file is not corrupted.
- Check video_processing.log for detailed error messages if the script fails.
