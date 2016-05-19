#coding=utf-8
import os, feature, sys, logging
import numpy as np, cv2

logging.basicConfig(level=logging.DEBUG,
     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
     datefmt='%a, %d %b %Y %H:%M:%S',
     filename='path.log',
     filemode='a')


save = np.array([])

for root, dirs, files in os.walk('./patch'):
         for d in dirs:
             if d != sys.argv[1]:
                 continue
             for rrroot, dddirs, fffiles in os.walk('./patch/%s'%d):
                 for f in fffiles:
                     im = cv2.imread('./patch/%s/%s' %(d,f))
                     res = feature.feature.GLCM(im, 99, 99, 64)
                     save = np.r_[save,res]
                     logging.info('%s %s res:%s'  %(d,f,res))
                     print res
         break
         
np.save('glcm%s.npy'%sys.argv[1], save)

