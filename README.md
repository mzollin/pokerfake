# pokerfake
<p>
  <b>protect your webcam feed from tools that detect your heart rate</b><br>
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/pokerface"><img alt="Updates" src="https://pyup.io/repos/github/mzollin/pokerfake/shield.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/pokerface"><img alt="Python3" src="https://pyup.io/repos/github/mzollin/pokerfake/python-3-shield.svg"></a><br><br>
<p>
  
## Setup and usage:
- sudo apt install v4l2loopback-utils python-opencv
- pip3 install -r requirements.txt
- sudo modprobe v4l2loopback devices=1

This will set up a virtual /dev/video device to which you can write the faked video stream using pokerface.py

## Python dependencies:
- opencv_python
- pyfakewebcam
- numpy
