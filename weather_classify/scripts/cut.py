#coding=utf-8
import cv2, os , feature,sys
import numpy as np

count = 0

t = [0,0,0] 

count = 0
for root, dirs, files in os.walk('./cut/%s'%sys.argv[1]):
    for f in files:
        im = feature.feature('./cut/%s/%s'%(sys.argv[1],f))
        res =  im.get_patch()[0][0]
        print res 
        t[int(res)] += 1
        count += 1

        print t[int(sys.argv[1])]/float(count)

        '''
        im = cv2.imread('./cut/2/%s'%f)
        print im.shape[0]/100, im.shape[1]/100, im.shape
        for i in range(im.shape[0]/100):
            for j in range(im.shape[1]/100):
                image = im[i*100: (i+1)*100, j*100: (j+1)*100]
#                print  type(im[i*100: (i+1)*100, j*100: (j+1)*100]), im[i*100: (i+1)*100, j*100: (j+1)*100].shape
                cv2.imwrite('./cut/3/%s.jpg'%count, image)
                count += 1
        '''


