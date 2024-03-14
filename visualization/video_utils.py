# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import cv2
import os
import numpy as np


def video_slice(video_path, output_path='./frames', start_time="00:00", end_time="00:10", target_frame_rate=-1):
    """
    Extracts frames from a video file at a given frame rate.
    
    Args:
        video_path (str): Path to the video file.
        output_path (str): Path to the directory where the frames will be saved.
        start_time (str): Start time of the slice in the format "MM:SS". Set to -1 to start from the beginning.
        end_time (str): End time of the slice in the format "MM:SS". Set to -1 to end at the end of the video.
        target_frame_rate (int): Frame rate of the output images. Set to -1 to use the frame rate of the video.
    """
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if target_frame_rate == -1:
        target_frame_rate = fps
    
    if start_time == -1:
        start_time_seconds = 0
    else:    
        start_time_seconds = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
    if end_time == -1:
        end_time_seconds = np.floor(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps)
    else:
        end_time_seconds = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])

    start_frame_number = int(start_time_seconds * fps)
    end_frame_number = int(end_time_seconds * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)

    frame_interval = int(fps / target_frame_rate)

    frame_count = start_frame_number
    image_count = 0

    while cap.isOpened() and frame_count <= end_frame_number:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            image_path = os.path.join(output_path, f'image_{image_count}.jpg')
            cv2.imwrite(image_path, frame)
            image_count += 1

        frame_count += 1

    cap.release()

    print(f"Saved {image_count} images to {output_path}")