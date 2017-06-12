#!/usr/bin/env python

#import modules used here -- sys is a very standard one
import sys

# Gather our code in main() function
def main():
    print'Hello there', sys.argv[1]
    # Command line args are in sys.argv[1], sys.argv[2]
    # sys.argv[0] is the script name itself and can be ignored

#Standard boilerplate to call the main() function to begin
# the program
if __name__ == '__main__':
	main()

# def double(num):
#     """Function to double the value111"""
#     return 2*num

# print (double.__doc__)