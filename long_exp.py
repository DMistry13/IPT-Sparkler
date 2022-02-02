import cv2 as cv
import numpy as np
import time

def long_ex(vid,d,n):
    #credit: https://www.youtube.com/watch?v=3WC0HyxbI90&t=203s for "long expsoure" picture
    r,m =vid.read()
    fps= int(vid.get(cv.CAP_PROP_FPS))
    width = 1080
    height = 1920
    ximg = d + "\\exp" + str(n) + ".png"
    out = cv.VideoWriter((d + "\\exp" + str(n) + ".avi"),cv.VideoWriter_fourcc('M','J','P','G'), fps/2, (width,height))
    #out = cv.VideoWriter((d + "\\expvid" + str(n) + ".mp4"), cv.VideoWriter_fourcc(*'MP4V'), 30, (width,height))
    t = 0
    while(vid.isOpened()):
        t += 1/fps
        r,f = vid.read()
        if (r==True):
            m=np.maximum(f,m)
            cv.imwrite(ximg,m)
            cv.rectangle(m, (int(width/2-50),height-50),(width,height),(0,0,0), -1)
            cv.putText(m,str(round(t,2))+"s (real time)", (int(width/2),int(height)),cv.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
            out.write(m)
            #cv.imshow("frame",m)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            #time.sleep(1/fps)
        else:
            break
    vid.release()
    out.release()
    print("Finished for "+str(n))