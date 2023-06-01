import cv2
import numpy as np


def create_running_text_video(text, width, height, duration):
    fps = 30
    frames = duration * fps

    img = np.zeros((height, width, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, _ = cv2.getTextSize(text, font, 1, 2)

    x = width
    y = int((height + text_size[1]) / 2)

    target_x = int(width / 2 - text_size[0] / 2)

    # Расчет количества кадров для полной длительности видео
    total_frames = frames

    # Расчет шага смещения для каждого кадра
    step = (width + text_size[0]) / total_frames

    video_writer = cv2.VideoWriter('running_text.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    frame_counter = 0
    while frame_counter < total_frames:
        img.fill(0)

        x -= step

        if x + text_size[0] < 0:
            break

        cv2.putText(img, text, (int(x), y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        video_writer.write(img)
        frame_counter += 1

    # Добавление пустых кадров для достижения заданной длительности видео
    while frame_counter < frames:
        video_writer.write(img)
        frame_counter += 1

    video_writer.release()
