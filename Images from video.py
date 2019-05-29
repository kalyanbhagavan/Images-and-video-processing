import cv2
print(cv2.__version__)
videocap = cv2.VideoCapture('file name')  # set to video file name
success, image = videocap.read()
count = 0
success = True
while success:
    if count >= 50:
        ind = count-50
        cv2.imwrite("frame%d.png" % ind, image)     # save frame as PNG file
    success, image = videocap.read()
    print('Read a new frame: ', success)
    count += 1
