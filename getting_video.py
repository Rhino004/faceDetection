import cv2
vid = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
# we can use cap.set instead of frame_width / height 
#capt.set(width id = 3 or lenth id = 4, size)
while True:
    #reads and stores the frame from the video capture
    rst, frame = vid.read()
    #dislpay each frame that was capture 
    cv2.imshow("video", frame)
    if cv2.waitKey(1) == ord("q"):#waits until the key is pressed
        break
vid.release()
cv2.destroyAllWindows()#closes all windows