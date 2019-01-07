#!/usr/bin/env python3

# Copyright (c) 2018 Marco Zollinger <marco@freelabs.space>
# Licensed under MIT, the license file shall be included in all copies

import pyfakewebcam
import time
import datetime
import cv2
import numpy as np

path = '../calm_hd.mp4'
#path = 0    # webcam

capture = cv2.VideoCapture(path)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
if fps < 1:
    fps = 30

# sudo modprobe v4l2loopback devices=1
cam = pyfakewebcam.FakeWebcam('/dev/video0', width, height)
fill = np.zeros((height, width, 3), np.uint8)

while True:
    start = datetime.datetime.now()
    success, image = capture.read()
    if success:
        frame_nr = capture.get(cv2.CAP_PROP_POS_FRAMES)
        # TODO: make simulated heart rate adjustable and independent of frame rate
        value = int(round(np.sin(2.0 * np.pi * frame_nr / 15.0)))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        fill[:] = (value+1, value+1, value+1)    # +1 offset to prevent bug with negative saturation
        image = cv2.add(image, fill)
        cam.schedule_frame(image)
        diff = datetime.datetime.now() - start
        delay = ((1.0/fps) - (diff.microseconds/1000000))    # wait frame duration (minus processing time) if we're early
        #print(delay)    # DEBUG show speed
        if delay > 0:
            time.sleep(delay)
    else:
        capture = cv2.VideoCapture(path)
capture.release()
