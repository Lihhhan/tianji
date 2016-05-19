#coding=utf-8
import sys, os , train, test, logging


logging.basicConfig(level=logging.DEBUG,
      format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
      datefmt='%a, %d %b %Y %H:%M:%S',
      filename='gamma.log',
      filemode='a')
  



c = [10, 800]
addc = 50

gamma = [5, 40]
addg = 1

maxpre = 0
resmax = 0
logging.info('begin ..')
if sys.argv[1] == 'c':
    for i in range(c[0], c[1], addc):
        train.train(i,5)
        res = test.test()
        logging.warning('c = %s, res = %s' %(i, res))        
        if res > maxpre:
            resmax = i
            maxpre = res
            os.system('cp ./svm_data.dat maxc.dat')
    logging.warning('max c is %s, while maxres = %s' %(resmax, maxpre))
else:
    for i in range(gamma[0], gamma[1], addg):
        train.train(10,i)
        res = test.test()
        logging.warning('gamma = %s, res = %s' %(i, res))
        if res > maxpre:
            resmax = i
            maxpre = res 
            os.system('cp ./svm_data.dat maxg.dat')
    logging.warning('max gamma is %s, while maxres = %s' %(resmax, maxpre))
