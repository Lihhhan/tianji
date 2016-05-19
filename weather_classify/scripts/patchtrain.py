#coding=utf-8
import cv2
import numpy as np

def patch(c = 5.81, g = 4.33):
    snow = np.load('glcm0.npy')

    l = snow.shape
    s_t = np.linspace(0, 0, l[0]/4)

    rain = np.load('glcm2.npy')
    l = rain.shape
    r_t = np.linspace(2, 2, l[0]/4)
    
    #train = np.array(np.r_[snow,rain], dtype = np.float32)
    train = np.array(np.r_[snow[:200],rain[:200]], dtype = np.float32)
    train.shape = -1 , 4
    res = np.array(np.r_[s_t[:50],r_t[:50]], dtype = np.float32)

    test = np.array(np.r_[snow[200:],rain[200:]], dtype = np.float32)
    test.shape = -1, 4
    rres = np.array(np.r_[s_t[50:],r_t[50:]], dtype = np.float32)

    svm_params = dict( kernel_type = cv2.SVM_RBF, svm_type = cv2.SVM_C_SVC, C = c, gamma=g )

    svm = cv2.SVM()
    svm.train(train, res, params=svm_params)
    svm.save('svm_data_rain2snow.dat')


    #svm.load('svm_data_rain2snow.dat')
    
    '''
    count = 0
    alll = len(test) 
    for i in range(len(test)):
        r = svm.predict_all(np.array([test[i]], dtype = np.float32))
        print r, rres[i]
        if r == rres[i]:
            count += 1
    print float(count)/alll
    '''

    r = svm.predict_all(test)
    count = 0
    alll = r.shape[0]
#    print alll
    for i in range(r.shape[0]):
#        print r[i][0], rres[i],count
        if r[i][0] == rres[i]:
            count += 1
#    print float(count)/alll
    return float(count)/alll

def left_one():
    snow = np.load('glcm0.npy')
    l = snow.shape
    s_t = np.linspace(0, 0, l[0]/4)
    
    rain = np.load('glcm2.npy')
    l = rain.shape
    r_t = np.linspace(2, 2, l[0]/4)

    train = np.array(np.r_[snow[:200], rain[:200]], dtype = np.float32)
    train.shape = -1 , 4
    res = np.array(np.r_[s_t[:50],r_t[:50]], dtype = np.float32)

    svm_params = dict( kernel_type = cv2.SVM_LINEAR, svm_type = cv2.SVM_C_SVC, C = 8.37, gamma=9.04 )
    
    count = 0
    alll = 0
    for i in range(train.shape[0]):
        #第i个放到第一位
        temp = train[i]
        train[i] = train[0]
        train[0] = temp
        
        temp = res[i]
        res[i] = res[0]
        res[0] = temp

        svm = cv2.SVM()
        svm.train(train[1:], res[1:], params=svm_params)
        #svm.save('svm_data_rain2snow.dat')
    
        #svm.load('svm_data_rain2snow.dat')
        r = svm.predict_all(np.array([train[0]], dtype = np.float32))
        if r == res[0]:
            count += 1
        alll += 1
        print float(count)/train.shape[0], alll, train.shape[0], r, res[0]

patch()
'''
m = 0
gx = 0
cx = 0
for g in np.linspace(1, 50, 500):
    for c in np.linspace(1, 50, 500):
        r = patch(c,g)
        if r > m:
            gx = g
            cx = c
            m = r
            print g,c, r

#left_one()
'''
