#coding=utf-8
import cv2
import numpy as np
'''
snow = np.load('array0.npy')

l = snow.shape
s_t = np.linspace(0, 0, l[0]/5)

rain = np.load('array2.npy')
l = rain.shape
r_t = np.linspace(2, 2, l[0]/5)


train = np.array(np.r_[snow,rain], dtype = np.float32)
train.shape = -1 , 5 
test = np.array(np.r_[s_t,r_t], dtype = np.float32)

svm_params = dict( kernel_type = cv2.SVM_LINEAR, svm_type = cv2.SVM_C_SVC, C = 50, gamma=5.38 )

svm = cv2.SVM()
svm.train(train, test, params=svm_params)
svm.save('svm_data_rain2snow.dat')
'''
svm = cv2.SVM()
svm.load('svm_data_rain2snow.dat')

snow = np.load('testarray0.npy')
l = snow.shape
s_t = np.linspace(0, 0, l[0]/5)
rain = np.load('testarray2.npy')
l = rain.shape
r_t = np.linspace(2, 2, l[0]/5)
train = np.array(np.r_[snow,rain], dtype = np.float32)
train.shape = -1 , 5
test = np.array(np.r_[s_t,r_t], dtype = np.float32)

res = svm.predict_all(train)

count = 0
alll = train.shape[0]
for i in range(train.shape[0]):
    print res[i][0], test[i],count
    if res[i][0] == test[i]:
        count += 1
print float(count)/alll
