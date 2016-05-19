#coding=utf-8
import feature,  video
import sys, os, logging
import numpy as np


logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./log/classify.log',
    filemode='w')

if len(sys.argv) > 2:
    name = sys.argv[1]
    out = sys.argv[2]
else :
    exit();
v = video.video(name)
v.run(out)


