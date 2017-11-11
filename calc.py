import math

def main():

	batch = 128
	in_height = 28
	in_width = 28
	in_channels = 1
	out_channels = 16
	stride = (3, 3)
	kernel = (3, 3)
	padding = (1, 1)
	dilation = (1, 1)

	out_height = math.floor((in_height + (2*padding[0]) - dilation[0] * (kernel[0] - 1) - 1)/stride[0] + 1)
	out_width = math.floor((in_width + (2*padding[1]) - dilation[1] * (kernel[1] - 1) - 1)/stride[1] + 1)

	print("({}, {}, {}, {})".format(batch, out_channels, out_height, out_width))

if __name__ == '__main__':
	main()






