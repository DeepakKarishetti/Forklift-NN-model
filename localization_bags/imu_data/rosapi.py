import rosbag
bag = rosbag.Bag('angle_90_left_2019-05-15-11-53-35.bag')
for topic, msg, t in bag.read_messages(topics=['/arduino/imu/']):
	print(msg.orientation.x)
bag.close()
