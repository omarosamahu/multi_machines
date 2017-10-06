#!/usr/bin/env python
import rospy 
import cv2 
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from Adafruit_BNO055 import BNO055




#init new node 
rospy.init_node('image publisher')
#create the publisher 
pub = rospy.Publisher('img',Image,queue_size=100)
#adjust rate 
rate = rospy.Rate(10)

''''
heeeeeeeeeeeeeeeeeeeere we gooooooo 
'''
bridge = CvBridge()
#initialize the camera module
cam = cv2.VideoCapture(-1)

while not rospy.is_shutdown():
	while True:
		
		_,frame = cam.read()
	#	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		data = bridge.cv2_to_imgmsg(frame)
		pub.publish(data)
		rate.sleep()
		if KeyboardInterrupt:
			break
