import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.optimize import curve_fit

def gen_linear_A(m,vars):
    datapoint = range(m) #assuming we have equally placed points, thus range
    A = np.zeros((m,vars))
    for i in datapoint:
        for j in range(vars):
            A[i][j] = datapoint[i]**j
    return A

def gen_kern(m, c):
    A = np.ones((m,m))
    if c:
        for i in range(m):
            for j in range(m):
                A[i][j] = np.exp(-((i-m)**2)/2) * np.exp(-((j-m)**2)/2)
    else:
        A = A / (m**2)
    
    return A




def fun1(x, a, b, c, d):
    return a * np.sin(x*b) + c * np.cos(x*d)



#MAIN

video_seq = []

file_name = input("What .mp4 file should be used?")
video_info = cv2.VideoCapture(file_name)
fps = video_info.get(cv2.CAP_PROP_FPS)
while video_info.isOpened():
    ret, frame = video_info.read()
    
    if not ret:
        break

    video_seq.append(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

data_amount = input("How many frames should be used for interpolation")
convolution = input("what is the odd N, NxN convolution applied to frames")
scaling = input("Should there be euler dropoff for the muddling(1/0)")

kern = gen_kern(convolution, scaling)




video_info.release()

