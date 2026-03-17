import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.optimize import curve_fit

def gen_linear_A(m,vars):
    datapoint = range(1,m+1) #assuming we have equally placed points, thus range
    A = np.zeros((m,vars))
    for i in range(datapoint):
        for j in range(vars):
            A[i][j] = datapoint[i]**j
    return A






def fun1(x, a, b, c, d):
    return a * np.sin(x*b) + c * np.cos(x*d)



#MAIN

video_seq = []

file_name = input("What .mp4 file should be used? \n")
video_info = cv2.VideoCapture(file_name)
fps = video_info.get(cv2.CAP_PROP_FPS)

#putting the data into a array
while video_info.isOpened():
    ret, frame = video_info.read()
    
    if not ret:
        break

    video_seq.append(frame)

    

data_amount = input("How many frames should be used for interpolation\n")
polyamnt = input("what number polynomial approximation should be used? 0 if using custom\n")
convolution = input("what is the odd N, NxN convolution applied to frames\n")
scaling = input("Should there be euler dropoff for the muddling(1/0)\n")

Amat = []
if polyamnt != 0:
    Amat = gen_linear_A(data_amount,polyamnt)

solution_vec = np.array(np.zeros(len(video_seq[0]),len(video_seq[0,0])), dtype=list)
#numpy array in the shape of [x,y,color] which stores lists where we will deposit the x's for the function solutions
#having different functions for the colors is... suboptimal

for i in range(len(video_seq)/data_amount):
    interdata = video_seq[i:(i+data_amount)] #gets a subsection of the frames
    for i in range(len(interdata)):
        if scaling==0:
            interdata[i] = cv2.cvtColor(interdata[i], cv2.COLOR_BGR2GRAY)
            interdata[i] = cv2.blur(interdata[i], (convolution,convolution))
            
        else:
            interdata[i] = cv2.cvtColor(interdata[i], cv2.COLOR_BGR2GRAY)
            interdata[i] = cv2.GaussianBlur(interdata[i], (convolution,convolution), 0)
            
    
    #interdata[frame, x, y, color]
    if Amat != []:
        #we use scipy.optimize.nnls for non negative least squares approximation for each color
        ymat = interdata(:,x,y,0)
    else:
        #this is using scipy.optimize.least_squares for nonlinear least squares

    
    





#freeing video after capturing it
video_info.release()

