#!/usr/bin/env python
import rospy 
import cv2
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
from drawnow import drawnow 

tmp = []
plt.ion()
def plotter():
	plt.plot(tmp)
	plt.grid()
def call_back(data):
	  tmp.append(data.data)
	  drawnow(plotter)
	  if len(tmp) >= 100:
	  	tmp.pop(0)
	  	

rospy.init_node('subscriber_node') 
sub = rospy.Subscriber('chatter', Float32, call_back)
# while 1:
# 	drawnow(plotter)
# 	if len(tmp) >= 100:
# 		tmp.pop(0)
rospy.spin()