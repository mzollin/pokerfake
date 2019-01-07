# pokerfake
<p>
  <b>protect your webcam feed from tools that detect your heart rate</b><br>
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/pokerfake"><img alt="Updates" src="https://pyup.io/repos/github/mzollin/pokerfake/shield.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/pokerfake"><img alt="Python3" src="https://pyup.io/repos/github/mzollin/pokerfake/python-3-shield.svg"></a><br><br>
<p>

Inspiration: https://github.com/thearn/webcam-pulse-detector

Pokerfake works by varying the image brightness to simulate a pulse, therefore covering up your real heart rate.<br>
It's currently just a proof of concept, so **don't rely on it.**

## Setup and usage:
- sudo apt install v4l2loopback-utils python-opencv
- pip3 install -r requirements.txt
- sudo modprobe v4l2loopback devices=1

This will set up a virtual /dev/video device to which you can write the faked video stream using pokerfake.py<br>
Example: &nbsp; [videochat-app]<----/dev/video1---[pokerfake.py]<----/dev/video0----[your webcam]

## Python dependencies:
- opencv_python
- pyfakewebcam
- numpy
