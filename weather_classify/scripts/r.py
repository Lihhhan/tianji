#coding=utf-8
import os, feature, sys, logging
import numpy as np

logging.basicConfig(level=logging.DEBUG,
     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
     datefmt='%a, %d %b %Y %H:%M:%S',
     filename='r.log',
     filemode='a')


save = np.array([])

for root, dirs, files in os.walk('./images'):
         for d in dirs:
             if d != sys.argv[1]:
                 continue
             for rrroot, dddirs, fffiles in os.walk('./images/%s'%d):
                 for f in fffiles:
                     im = feature.feature('./images/%s/%s' %(d,f))
                     res = im.snow_region()
                     save = np.r_[save,res]
                     logging.info('%s %s res:%s'  %(d,f,res))
                     print res
         break
         
np.save('array%s.npy'%sys.argv[1], save)

