import cv2
import numpy as np


def create_running_text_video(text, text_color, bg_color, width, height, duration):
    fps = 30
    frames = duration * fps
    img = np.zeros((height, width, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_COMPLEX
    text_size, _ = cv2.getTextSize(text, font, 1, 2)
    x = width
    y = int((height + text_size[1]) / 2)
    total_frames = frames
    step = (width + text_size[0]) / total_frames
    video_path = 'running_text.mp4'
    video_writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    t_color = tuple(int(text_color.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))
    background_color = tuple(int(bg_color.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))
    frame_counter = 0

    while frame_counter < total_frames:        
        img[:] = background_color
        x -= step
        if x + text_size[0] < 0:
            break
        cv2.putText(img, text, (int(x), y), font, 1, t_color, 2, cv2.LINE_AA)
        video_writer.write(img)
        frame_counter += 1

    while frame_counter < frames:
        video_writer.write(img)
        frame_counter += 1

    video_writer.release()

    return video_path
