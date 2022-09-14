#!/usr/bin/env python3

import sys

#if __name__ == '__main__':
#    sys.stderr.write("client is not implemented yet\n")

#This is simply a way for us to run a test to see if
#We're passing the files correct

args_length = len(sys.argv)
print("There are {arguments} in the list".format(arguments=args_length))
i = 0
while i < args_length:
    print("Argument #{args} = {argu}".format(args=i, argu=sys.argv[i]))
    i+= 1
