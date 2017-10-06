#!/usr/bin/env python
import rospy 
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


bridge = CvBridge()

def call_back(data):
	    
	    
	    			cv_image = bridge.imgmsg_to_cv2(data)
	    			cv2.imshow('data',cv_image)
	    			key = cv2.waitKey(33)
	    			
	    	
	    			
		 	

		# return cv_image
	    
		
	
	

#Inialize a new subscriber node 
rospy.init_node('subscriber_node')

# sub = rospy.Subscriber('',String,call_back)
sub = rospy.Subscriber('img', Image, call_back)
rospy.spin()