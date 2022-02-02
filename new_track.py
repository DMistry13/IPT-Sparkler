import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

def ntr(vid,n,d):
    blank_image = np.zeros((1920,1080,3), np.uint8)
    fps= int(vid.get(cv.CAP_PROP_FPS))
    data = []
    fm = 0
    out = cv.VideoWriter((d + "\\dots" + str(n) + ".avi"),cv.VideoWriter_fourcc('M','J','P','G'), fps/2, (1080,1920))
    ximg = d + "\\dot"+str(n)+".png"
    while vid.isOpened():
        r,f= vid.read()
        fm +=1
        if r == True:
            gray = cv.cvtColor(f,cv.COLOR_RGB2GRAY)
            _ , mask = cv.threshold(gray,50,255,cv.THRESH_BINARY)
            mask = cv.GaussianBlur(mask, (3, 3), 0)
            img_hsv = cv.cvtColor(f, cv.COLOR_BGR2HSV)
            hsv_color1 = np.asarray([132, 88, 75])
            hsv_color2 = np.asarray([240, 230, 220])
            mask1 = cv.inRange(img_hsv, hsv_color1, hsv_color2)
            mask = mask + mask1
            contours, _ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                    area = cv.contourArea(cnt)
                    if area < 500:
                        #cv.drawContours(f, [cnt],-1, (0,255,0),2)
                        x ,y , w, h = cv.boundingRect(cnt)
                        #cv.putText(f,str(area), (x+w+sc-15,y+h+sc+15),cv.FONT_HERSHEY_PLAIN,1,(0,255,0),1)
                        cx = int(x+w/2)
                        cy = int(y+h/2)
                        v = np.sqrt(w**2 + h**2) * 125
                        data.append([cx,cy,fm,v])
                        cv.circle(blank_image,(cx,cy),2,(255,0,0),-1)
            #print("At frame "+ str(fm))
            #cv.imshow("mask",blank_image)
            out.write(blank_image)
            cv.imwrite(ximg,blank_image)
            if cv.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            break
    out.release()
    vid.release()
    print("Video is proccsed for " + str(n))
    #plot of x-distance againsts time
    '''fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    #print(data)
    exp = lambda x: 10**(x)
    log = lambda x: np.log10(x)
    ax3.plot(np.linspace(0,len(nppft),len(nppft)),nppft,"xb")    #plot of number of particles per frame againsts time
    for i in data:
        if i[2] > 1500:
            ax1.plot((i[2]/60, np.abs(i[0]-center)*sc),"xr")
            ax2.plot(i[2]/60,i[3],"xy")     #plot of v againsts time
            #ax3.plot(i[2]/60,i[4],"xb")    #plot of number of particles per frame againsts time
            ax4.plot((np.abs(i[0]-center)*sc),(i[3]),"kx")
    print("Making XDT for " +str(n))
    ax1.set_ylabel("Horizontal distance (cm)")
    ax1.set_xlabel("Time (s)")
    ax1.set_title("Graph of x-distance againsts frames of recording " + str(n))
    ax1.grid()
    fig1.savefig('XDT'+str(n)+'.png')
    print("XDT done, making VT for " +str(n))
    ax2.set_ylabel("Speed (cm per sec)")
    ax2.set_xlabel("Time (s)")
    ax2.set_title("Graph of speed againsts Time of recording " + str(n))
    ax2.grid()
    fig2.savefig('VT'+str(n)+'.png')
    print("VT done, making MPPFT for " +str(n))
    ax3.set_ylabel("Number of particles per frame")
    ax3.set_xlabel("Time (s)")
    ax3.set_title("Number of particles per frame of recording " + str(n))
    ax3.grid()
    fig3.savefig('NPPFT'+str(n)+'.png')
    print("NPPFT done, making VX for " +str(n))
    ax4.set_ylabel("Speed")
    ax4.set_xlabel("x-distance (cm)")
    ax4.set_title("Speed againsts x-distance of recording " + str(n))
    ax4.grid()
    fig4.savefig('VX'+str(n)+'.png')
    print("VX done for " +str(n))'''
    nm = d +"\\position_data_" + str(n) + ".csv"
    np.savetxt(nm, data, delimiter=",", fmt="%.2f",header="cx,cy,n,v", comments="")
    print("DONE for "+ str(n))
