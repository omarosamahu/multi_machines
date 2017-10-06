#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 
import math 

class OutAndBack:
	def __init__(self):
		#give the node a name
		rospy.init_node('out_and_back')
		#create publisher 
		self.cmd_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=5)
		#How fast will we update the robot's movement
		r = rospy.Rate(90)
		#linear speed
		linear_spead = 0.2
		#Adjust linear distance & goal limitation 
		goal = 1.0
		#Adjust linear duration
		linear_duration = goal / linear_spead
		#angular speed
		angular_speed = 1.0
		#set the rotation angle equal pi  
		goal_angle = math.pi / 2
		#Angular duration 
		angular_duration = goal_angle / angular_speed

		while not rospy.is_shutdown():
			
			move_cmd = Twist()
			move_cmd.linear.x = linear_spead
			ticks = int(linear_duration * 90)

			for t in range(ticks):
				self.cmd_vel.publish(move_cmd)
				r.sleep()
			#publish an empty value to stop the robot before the rotation
			move_cmd = Twist()
			self.cmd_vel.publish(move_cmd)
			rospy.sleep(1)
			#start rotation 
			move_cmd.angular.z = angular_speed
			ticks = int(goal_angle * 90)
			for t in range(ticks):
				self.cmd_vel.publish(move_cmd)
				r.sleep()
			#stop the rotation before next transelation 
			move_cmd = Twist()
			self.cmd_vel.publish(move_cmd)
			rospy.sleep(1)
			#stop the robot 
			self.cmd_vel.publish(Twist())
	def shutdown(self):
			# Always stop the robot when shutting down the node.
			rospy.loginfo("Stopping the robot...")
			self.cmd_vel.publish(Twist())
			rospy.sleep(1)

if __name__ == '__main__':
	
		OutAndBack()

		