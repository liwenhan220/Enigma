from PIL import ImageGrab
import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('enigma.mp4',fourcc,60,(1920,1080),True)
while True:
    img = np.array(ImageGrab.grab())
    out.write(img)
##    cv2.imshow('window',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destoryAllWindows()
        break
    
        
    
    
    
