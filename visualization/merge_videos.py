# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import argparse
import subprocess
import os

def merge_videos(left_video_path, right_video_path, output_path, middle_video_path=None, fps=30):
    if middle_video_path:
        # If middle video is provided, merge three videos side by side
        command = [
            'ffmpeg',
            '-i', left_video_path,
            '-i', middle_video_path,
            '-i', right_video_path,
            '-filter_complex', f'[0:v][1:v][2:v]hstack=inputs=3[v]',
            '-map', '[v]',
            '-r', str(fps),  # Set the output fps
            '-c:v', 'libx264',
            '-crf', '23',
            '-preset', 'veryfast',
            output_path
        ]
    else:
        # If no middle video is provided, merge two videos side by side
        command = [
            'ffmpeg',
            '-i', left_video_path,
            '-i', right_video_path,
            '-filter_complex', f'[0:v][1:v]hstack=inputs=2[v]',
            '-map', '[v]',
            '-r', str(fps),  # Set the output fps
            '-c:v', 'libx264',
            '-crf', '23',
            '-preset', 'veryfast',
            output_path
        ]
    
    subprocess.run(command, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge two or three videos side by side.')
    parser.add_argument('--left_video', '-l', type=str, required=True, help='Path to the left video file')
    parser.add_argument('--middle_video', '-m', type=str, help='Path to the middle video file (optional)')
    parser.add_argument('--right_video', '-r', type=str, required=True, help='Path to the right video file')
    parser.add_argument('--output', '-o', type=str, default='output.mp4', help='Output video file path')
    parser.add_argument('--fps', '-f', type=int, default=30, help='Frames per second for the output video (default: 30)')

    args = parser.parse_args()

    if not os.path.exists(args.left_video):
        raise FileNotFoundError(f"Left video file not found: {args.left_video}")
    if not os.path.exists(args.right_video):
        raise FileNotFoundError(f"Right video file not found: {args.right_video}")
    if args.middle_video and not os.path.exists(args.middle_video):
        raise FileNotFoundError(f"Middle video file not found: {args.middle_video}")

    merge_videos(args.left_video, args.right_video, args.output, args.middle_video, args.fps)
    print(f"Videos merged successfully into {args.output} with {args.fps} fps")
