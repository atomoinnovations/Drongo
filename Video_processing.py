# Importing necessary libraries
import cv2
import numpy as np
import time
import logging
import os

# Configure logging for debugging and tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='video_processing.log'
)
logger = logging.getLogger(__name__)

# Function to check if video file exists and is accessible
def check_video_file(video_path):
    """
    Verify if the video file exists and can be opened.
    
    Args:
        video_path (str): Path to the video file
    Returns:
        bool: True if video can be opened, False otherwise
    """
    if not os.path.exists(video_path):
        logger.error(f"Video file {video_path} does not exist")
        return False
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logger.error(f"Failed to open video file {video_path}")
        return False
    cap.release()
    return True

# Function to initialize video writer for saving processed video
def initialize_video_writer(cap, output_path, width, height):
    """
    Initialize VideoWriter object for saving processed video.
    
    Args:
        cap: VideoCapture object
        output_path (str): Path to save the output video
        width (int): Frame width
        height (int): Frame height
    Returns:
        VideoWriter object
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
    fps = cap.get(cv2.CAP_PROP_FPS)
    return cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Function to apply image processing techniques
def process_frame(frame, target_size=(540, 380)):
    """
    Apply various image processing techniques to the frame.
    
    Args:
        frame: Input frame
        target_size: Tuple of (width, height) for resizing
    Returns:
        Dictionary containing processed frames
    """
    # Resize frame
    resized_frame = cv2.resize(
        frame, target_size, fx=0, fy=0, interpolation=cv2.INTER_CUBIC
    )
    
    # Convert to grayscale
    gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    # Convert to different color spaces
    hls = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HLS)
    hsv = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    
    # Apply Laplacian edge detection
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = cv2.convertScaleAbs(lap)  # Convert to uint8 for display
    
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)
    
    return {
        'original': resized_frame,
        'gray': gray,
        'hls': hls,
        'hsv': hsv,
        'thresh': thresh,
        'laplacian': lap,
        'blur': blur,
        'equalized': equalized
    }

# Main function to process video
def main():
    # Video file path
    video_path = 'Demo.mp4'
    output_path = 'processed_video.mp4'
    
    # Check if video file is accessible
    if not check_video_file(video_path):
        print("Error: Cannot access video file. Exiting...")
        return
    
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    logger.info(f"Video loaded: {width}x{height}, {fps} FPS, {total_frames} frames")
    
    # Initialize video writer
    out = initialize_video_writer(cap, output_path, 540, 380)
    
    # Display loading message
    print("Downloading video . . .")
    time.sleep(10)  # Simulate download delay
    
    print("Processing Video . . .")
    time.sleep(15)  # Simulate processing delay
    
    # Initialize frame counter and timing
    frame_count = 0
    start_time = time.time()
    
    # Font settings for text overlay
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    font_scale = 1
    color = (0, 255, 0)  # Green text
    thickness = 2
    
    # Loop until the end of the video
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            logger.info("End of video reached")
            break
        
        frame_count += 1
        
        # Process the frame
        processed = process_frame(frame)
        
        # Calculate and display frame rate
        elapsed_time = time.time() - start_time
        current_fps = frame_count / elapsed_time if elapsed_time > 0 else 0
        
        # Add text overlays
        cv2.putText(
            processed['original'],
            f'Frame: {frame_count}/{total_frames}',
            org,
            font,
            font_scale,
            color,
            thickness
        )
        cv2.putText(
            processed['original'],
            f'FPS: {current_fps:.2f}',
            (50, 100),
            font,
            font_scale,
            color,
            thickness
        )
        
        # Display the resulting frames
        cv2.imshow('Original Frame', processed['original'])
        cv2.imshow('Grayscale', processed['gray'])
        cv2.imshow('HLS Color Space', processed['hls'])
        cv2.imshow('HSV Color Space', processed['hsv'])
        cv2.imshow('Adaptive Threshold', processed['thresh'])
        cv2.imshow('Laplacian Edge', processed['laplacian'])
        cv2.imshow('Gaussian Blur', processed['blur'])
        cv2.imshow('Histogram Equalized', processed['equalized'])
        
        # Write the processed frame to output video
        out.write(processed['original'])
        
        # Log frame processing
        logger.info(f"Processed frame {frame_count}")
        
        # Define 'q' as the exit button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            logger.info("User interrupted video processing")
            break
    
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    # Log completion
    logger.info("Video processing completed")
    print(f"Processed video saved as {output_path}")

# Run the main function
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
