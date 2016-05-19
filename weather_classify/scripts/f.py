#coding=utf-8
import feature, os 

for root, dirs, files in os.walk('./old'):
    for f in files:
        im = feature.feature('./old/%s'%f)
        print f, im.classify()





