import sys

input_file = sys.argv[1]

with open(input_file, 'r') as r:
	a = (" ".join(line.strip() for line in r))
	b = a.replace('data: ', "")
	c = b.replace(' ---', "")
	d = [int(i) for i in c.split(' ')]

output_file = input_file.replace(input_file, 'data_' + input_file)

with open(output_file, 'w') as f:
	f.write('{}\n'.format(d))
