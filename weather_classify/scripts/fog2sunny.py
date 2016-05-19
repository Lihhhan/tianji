import cv2
import numpy as np
import feature, sys, os

d = '1'
if len(sys.argv) > 1:
    d = sys.argv[1]

save = np.array([])

for root, dirs, files in os.walk('./test/%s'%d):
    for f in files:
        im = feature.feature('test/%s/%s'%(d,f))
        res = im.get_features()
        print res.shape
        save = np.r_[save,res]

np.save('fog2snow%stest.npy'%d, save)



