import long_exp as le
import new_track as nt
import cv2 as cv
import numpy as np
import os
import post as pst
if __name__ == "__main__":
    lst_vids = []
    dirc = []
    fps = [59.59,57.11,58.96,58.55,59.36,59.65,59.55,57.54,60,59]
    center = [616,542,556,519,537,549,523,549,530,516]
    sc = 15/296
    n = 0
    for (root_path, directories, files) in os.walk(os.getcwd()):
        for i in files:
            if ".csv" in i:
                n+=1
                e = root_path+"\\"+i
                pst.graphs(e,fps[n-1],sc,n,root_path,center[n-1])
                """if "one" not in i:
                    vid = cv.VideoCapture(e)
                    nt.ntr(vid,n,root_path)
                vid = cv.VideoCapture(e)
                le.long_ex(vid,root_path,n)"""