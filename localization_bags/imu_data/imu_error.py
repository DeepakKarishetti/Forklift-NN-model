import rosbag
import os
import sys
import time

input_topic = '/arduino/imu'
bag_file = sys.argv[1]
print("Reading the bag file: {}\n".format(sys.argv[1]))

x = list()
y = list()
yaw = list()

# access bag
bag = rosbag.Bag(bag_file)
bag_contents = bag.read_messages(topics=[input_topic])
bag_name = bag.filename

for topic, msg, t in bag_contents:
        x.append(msg.orientation.x)
        y.append(msg.orientation.y)
        yaw.append(msg.angular_velocity.z)

bag.close

# 
#print(type(x))
	


