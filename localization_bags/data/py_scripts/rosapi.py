import rosbag
import rospy
import time

pwm_data = list()
pwm_t = list()

velocity_data = list()
velocity_t = list()

bag = rosbag.Bag('2019-06-01-12-31-03_long drive.bag')
for topic, msg, t in bag.read_messages(topics=['/velocity_node/pedal_pwm']):
	pwm_t.append("{}".format((t)))
	pwm_data.append(msg.data)
bag.close()

#

bag = rosbag.Bag('2019-06-01-12-31-03_long drive.bag')
for topic, msg, t in bag.read_messages(topics=['/velocity_node/velocity']):   
	velocity_t.append("{}".format(t))
	velocity_data.append(msg.data)
bag.close()

#print(len(velocity_data))
print((pwm_t))
print((velocity_t))
a = [x for x in pwm_t if x in velocity_t]
if not a:
	print("NIL")
else:
	for i in a:
		print(a)

