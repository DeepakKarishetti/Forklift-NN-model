#!/usr/bin/env python

import rosbag
import os
import sys
import time

if (len(sys.argv) > 4):
	print("Ivalid input arguments!\n")

elif (len(sys.argv) == 4):
	input_topic = sys.argv[1]
	bag_file = sys.argv[2]
	file_name = sys.argv[3]
	print("Reading the bag file: {}\n".format(sys.argv[2]))

	all_topics = list()
	x = list()
	y = list()
	yaw = list()	

	# access bag
	bag = rosbag.Bag(bag_file)
	bag_contents = bag.read_messages(topics=[input_topic])
	bag_name = bag.filename
	
	topics = list()
	for topic, msg, t in bag_contents:
		x.append(msg.orientation.x)
		y.append(msg.orientation.y)
		yaw.append(msg.angular_velocity.z)

		if topic not in topics:
			topics.append(topic)

	all_topics = list(set(topics))
	bag.close

"""
	# Writing to the file
	filename = file_name.replace(file_name, 'extracted_' + file_name) + '_data.txt'
	with open(filename, 'w') as txt_file:
		txt_file.write('{}\n'.format(all_messages))

	#print(type(all_messages[1]))
	
elif (len(sys.argv) == 2):
	
	all_bag_files = [i for i in os.listdir(".") if i[-4: ] == ".bag"]
	total_files = str(len(all_bag_files))
	print("Reading all the {} bag files: \n".format(total_files))
	for i in all_bag_files:
		print(i)
	print('\n')


	input_topic = sys.argv[1]

	all_topics = list()
	all_messages = list()

	for bag_file in all_bag_files:
		# access bag
		bag = rosbag.Bag(bag_file)
		bag_contents = bag.read_messages(topics=[input_topic])
		bag_name = bag.filename
	
		topics = list()
		for topic, msg, t in bag_contents:
			all_messages.append(msg.data)
			if topic not in topics:
				topics.append(topic)

		all_topics = list(set(topics))
	bag.close

	# Writing to the file
	file_name = input_topic.replace('/', '_')
	filename = file_name.replace(file_name, 'extracted' + file_name) + '_data.txt'

	with open(filename, 'w') as txt_file:
		txt_file.write('{}\n'.format(all_messages))	

	#print(len(all_messages))

else:
	print("Invalid arguments entered!")
	sys.exit(1)
"""


