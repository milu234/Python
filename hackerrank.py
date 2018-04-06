n = raw_input()
input_line = raw_input()
input_list = input_line.split()
for i in xrange(len(input_list)):
	input_list[i] = int(input_list[i])

	t=tuple(input_list)
	print hash(t)