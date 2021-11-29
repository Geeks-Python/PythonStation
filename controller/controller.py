import cv2
import imutils
from imutils.video import VideoStream
import numpy as np

cam = VideoStream(src=0).start()
currentKey=list()