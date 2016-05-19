#coding=utf-8
import feature,  video
import sys, os, logging
import numpy as np
from sqlite3 import dbapi2 as sqlite3

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./log/classify.log',
    filemode='w')

if len(sys.argv) > 3:
    name = sys.argv[1]
    out = sys.argv[2]
    fname = sys.argv[3]
else :
    exit();
v = video.video(name)
v.run(out)


pwd = os.getcwd()
rv = sqlite3.connect(pwd + '/tasklist.db')

rv.execute('update tasks set prograss = "1" where filename = "%s"' %fname)
rv.commit()
rv.close()

