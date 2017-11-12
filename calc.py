"""

Assumptions
===========

- encoder is a sequence of Convs, MaxPool and ReLU
- decoder is a sequence of Deconvs, ReLU

"""

import math

in_channel = 1
in_height = 28
in_width = 28

conv = {
    'channels': [8, 16],
    'strides': [2, 2],
    'kernels': [3, 3],
    'paddings': [1, 1],
    'dilations': [1, 1]
}

pool = {
    'strides': [2, 1],
    'kernels': [2, 2]
}

deconv = {
    'channels': [16, 8, 1],
    'strides': [3, 2, 2],
    'kernels': [2, 2, 2],
    'paddings': [0, 1, 0],
}

def conv_formula(h, p, d, k, s):
    o_h = math.floor((h + (2*p) - d * (k - 1) - 1)/s + 1)
    return o_h

def deconv_formula(h, s, i_p, k, o_p):
    o_h = (h - 1) * s - (2*i_p) + k + o_p
    return o_h

def main():

    print("Input: ({}, {}, {}, {})\n".format(128, in_channel, in_height, in_width))

    o_h = None

    print("Encoder")
    for i in range(len(conv['channels'])):

        c = conv['channels'][i]
        p = conv['paddings'][i]
        k = conv['kernels'][i]
        s = conv['strides'][i]
        d = conv['dilations'][i]

        h = in_height if i == 0 else o_h
        o_h = conv_formula(h, p, d, k, s)
        
        print("\tConv {}: ({}, {}, {}, {})".format(i+1, 128, c, o_h, o_h))

        pool_k = pool['kernels'][i]
        pool_s = pool['strides'][i]
        o_h = conv_formula(o_h, 0, 1, pool_k, pool_s)

        print("\tPool {}: ({}, {}, {}, {})".format(i+1, 128, c, o_h, o_h))

    print("\nDecoder")
    for i in range(len(deconv['channels'])):

        c = deconv['channels'][i]
        i_p = deconv['paddings'][i]
        k = deconv['kernels'][i]
        s = deconv['strides'][i]

        o_h = deconv_formula(o_h, s, i_p, k, 0)

        print("\tDeconv {}: ({}, {}, {}, {})".format(i+1, 128, c, o_h, o_h))

    print("\nOutput: ({}, {}, {}, {})\n".format(128, c, o_h, o_h))

if __name__ == '__main__':
    main()
