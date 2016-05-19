#coding=utf-8
from PIL import Image
import math, sys
import cv2, os, logging
import numpy as np
import feature

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='predict.log',
    filemode='a')

def test( ):
    logging.info('predict start ...')

    weather_map = ['snow','fog','rain','sunny']
    #总数
    s = [ 0 for i in range(4)] 
    #错误数
    r = [ 0 for i in range(4)]
    a = 0
    for root, dirs, files in os.walk('./test'):
        for d in dirs:
            #if d != '2':
                #continue
            for rrroot, dddirs, fffiles in os.walk('./test/%s'%d):
                s[int(d)] = len(fffiles)
                for f in fffiles:
                    im = feature.feature('./test/%s/%s' %(d,f))
                    res = im.svmclassify('svm_data_rain2snow.dat')
                    a += 1
                    if weather_map[int(d)] == res:
                        r[int(d)] += 1
                        logging.info('classify right %s -> %s , total r/s =%f, r/s=%f'  %(weather_map[int(d)], res, float(sum(r))/a, float(r[int(d)])/s[int(d)]))
                    else:
                        logging.info('classify wrong %s -> %s' %(weather_map[int(d)], res))
        break
    for i in range(4):
        logging.info('%s: %f' %(weather_map[i], float(r[i])/s[i]))
    logging.info('all: %f' %(float(sum(r))/sum(s)))

    return float(sum(r))/sum(s)
test()
