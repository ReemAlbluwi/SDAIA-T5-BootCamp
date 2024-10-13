import cv2
import numpy as np
from ultralytics import YOLO
from google.colab.patches import cv2_imshow

best_model = YOLO('path')

vertices1 = np.array([(465, 350), (609, 350), (510, 630), (2, 630)], dtype=np.int32)
vertices2 = np.array([(678, 350), (815, 350), (1203, 630), (743, 630)], dtype=np.int32)

x1, x2 = 325, 635
lane_threshold = 609

text_position_left_lane = (10, 50)
text_position_right_lane = (820, 50)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)
background_color = (255, 0, 0)

cap = cv2.VideoCapture('sample_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('processed_sample_video.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

total_vehicles_in_left_lane = 0
total_vehicles_in_right_lane = 0

vehicle_tracker = {}

vehicles_in_left_lane = 0
vehicles_in_right_lane = 0

vehicle_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    detection_frame = frame.copy()

    detection_frame[:x1, :] = 0
    detection_frame[x2:, :] = 0

    results = best_model.predict(source=detection_frame, imgsz=640, conf=0.4)
    processed_frame = results[0].plot(line_width=1)

    processed_frame[:x1, :] = frame[:x1, :].copy()
    processed_frame[x2:, :] = frame[x2:, :].copy()

    cv2.polylines(processed_frame, [vertices1], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.polylines(processed_frame, [vertices2], isClosed=True, color=(255, 0, 0), thickness=2)

    bounding_boxes = results[0].boxes

    current_vehicle_tracker = {}

    vehicles_in_left_lane = 0
    vehicles_in_right_lane = 0

    for box in bounding_boxes.xyxy:
        x1_box, y1_box, x2_box, y2_box = map(int, box)
        center_x = (x1_box + x2_box) // 2

        matched_vehicle_id = None
        for vehicle_id, (prev_x, prev_y) in vehicle_tracker.items():
            if abs(prev_x - center_x) < 50:
                matched_vehicle_id = vehicle_id
                break

        if matched_vehicle_id is None:
            matched_vehicle_id = vehicle_id
            vehicle_id += 1

        current_vehicle_tracker[matched_vehicle_id] = (center_x, y1_box)

        if center_x < lane_threshold:
            if matched_vehicle_id not in vehicle_tracker:
                total_vehicles_in_left_lane += 1
            vehicles_in_left_lane += 1
        else:
            if matched_vehicle_id not in vehicle_tracker:
                total_vehicles_in_right_lane += 1
            vehicles_in_right_lane += 1

    vehicle_tracker = current_vehicle_tracker

    cv2.rectangle(processed_frame, (text_position_left_lane[0] - 10, text_position_left_lane[1] - 40),
                  (text_position_left_lane[0] + 300, text_position_left_lane[1] + 60), background_color, -1)
    cv2.rectangle(processed_frame, (text_position_right_lane[0] - 10, text_position_right_lane[1] - 40),
                  (text_position_right_lane[0] + 300, text_position_right_lane[1] + 60), background_color, -1)

    cv2.putText(processed_frame, f'Left Lane Count: {vehicles_in_left_lane}', (text_position_left_lane[0], text_position_left_lane[1]), font, font_scale, font_color, 2, cv2.LINE_AA)
    cv2.putText(processed_frame, f'Total Left Counter: {total_vehicles_in_left_lane}', (text_position_left_lane[0], text_position_left_lane[1] + 40), font, font_scale, font_color, 2, cv2.LINE_AA)

    cv2.putText(processed_frame, f'Right Lane Count: {vehicles_in_right_lane}', (text_position_right_lane[0], text_position_right_lane[1]), font, font_scale, font_color, 2, cv2.LINE_AA)
    cv2.putText(processed_frame, f'Total Right Counter: {total_vehicles_in_right_lane}', (text_position_right_lane[0], text_position_right_lane[1] + 40), font, font_scale, font_color, 2, cv2.LINE_AA)

    frame_width = int(cap.get(3))
    name_position = (frame_width // 2 - 100, int(cap.get(4)) - 30)
    cv2.putText(processed_frame, 'Reem , Shoog , Areej , Alhanof', name_position, font, font_scale, font_color, 2, cv2.LINE_AA)

    out.write(processed_frame)

cap.release()
out.release()

cv2.destroyAllWindows()

from IPython.display import HTML
from base64 import b64encode

video_path = "processed_sample_video.avi"

video_file = open(video_path, "rb").read()
video_url = "data:video/mp4;base64," + b64encode(video_file).decode()

HTML(f"""<video width=640 controls><source src="{video_url}" type="video/mp4"></video>""")
