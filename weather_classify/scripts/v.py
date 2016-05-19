#coding=utf-8
import video, sys
if len(sys.argv) > 1:
    print 'file %s'%sys.argv[1]
    i = video.video(sys.argv[1])
    while(True):
#        print i.snow_region( ) 
        i.Temporal_feature()

