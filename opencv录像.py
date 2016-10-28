import cv2
import time

interval = 0.1  # seconds
num_frames = 100
out_fps = 10

capture = cv2.VideoCapture(0)
size =(int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
video = cv2.VideoWriter("me.avi", cv2.cv.CV_FOURCC('I','4','2','0'), out_fps, size)


for i in xrange(42):
  capture.read()

for i in xrange(num_frames):
  _, frame = capture.read()
  video.write(frame)


##  filename = '{:4}.png'.format(i).replace(' ', '0')
##  cv2.imwrite(filename, frame)

  print('Frame {} is captured.'.format(i))
  #time.sleep(interval)

video.release()
capture.release()
