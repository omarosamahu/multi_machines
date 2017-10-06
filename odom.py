import rospy 
from geometry_msgs.msg import Twist, Point, Quanternion
import tf 
from rbx1_nav.transform_utils import quat_to_angle, normalize_angle
from math import *

class OutAndBack:
	def __init__(self):
		#Give the node a name 
		rospy.init_node('out_and_back')
		#create a publisher 
		pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		#adjust rate 
		r = rospy.Rate(20)

		#linear speed
		linear_speed = 0.2 
		#goal distance 
		goal_distance = 1.0 
		#angular speed
		angular_speed =  1.0 
		goal_angle = pi 
		#create a tf listener 
		self.tf_listener = tf.TransformListener()
		#give tf some time to fill its buffer 
		rospy.sleep(2)
		# Set the odom frame 
		self.odom_frame = '/odom'

		try:
			self.tf_listener.waitForTransform(self.odom_frame,
				'/base_footprint', rospy.Time(), rospy.Duration(1.0))
			self.base_frame = '/base_footprint'
		except (tf.Exception, tf.ConnectivityException, tf.LookupException):
			try:
				self.tf_listener.waitForTransform(self.odom_frame,
					'/base_link', rospy.Time(), rospy.Duration(1.0))
				self.base_frame = '/base_link'
	
			except (tf.Exception, tf.ConnectivityException,tf.LookupException):
					rospy.loginfo("Cannot find transform between /odom and/base_link or /base_footprint")
		pos = Point()

		for i in range(2):
			move_cmd = Twist()
			move_cmd.linear.x = linear_speed
			#get the starting position values 
			(pos,rot) = self.get_odom()

			x_start = pos.x
			y_start = pos.y

			dist = 0
			while dist < goal_distance and not rospy.is_shutdown():
			 	self.pub.publish(move_cmd)
			 	r.sleep()
			 	dist = sqrt((pos.x - x_start)**2 + (pos.y - y_start)**2 ) 
			#stop robot before rotation 
			move_cmd = Twist()
			self.pub.publish(move_cmd)
			rospy.sleep(1)
			#start rotation 
			move_cmd.angular.z = angular_speed
	def get_odom(self):
		(trans, rot) = self.tf_listener.lookupTransform(self.odom_frame,self.base_frame, rospy.Time(0))

