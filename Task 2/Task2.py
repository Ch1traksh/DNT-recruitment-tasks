import cv2 as cv
import numpy as np

vid = cv.VideoCapture("input.mp4")

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter("output.mp4", fourcc, 30.0, (843, 480))

skip_rate = 4

frame_no = 0
processed_frame_count = 0

while True:
    ret = vid.grab()
    if not ret:
        break

    frame_no += 1

    if(frame_no % skip_rate == 0):
        processed_frame_count += 1

        status, frame = vid.retrieve()

        frame = cv.resize(frame, (843, 480))
        out.write(frame)

        cv.imshow("Frame", frame)
        cv.waitKey(1)


vid.release()
out.release()
print(frame_no, processed_frame_count)

