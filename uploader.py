#!/usr/bin/env python3 -tt
"""
Tests rsync with amazon s3 using random data. Connection layer to amazon s3 is handled by s3fs-fuse. Python as the scripting language
"""
 
# Imports
import sys
#import os
 
# Global variables
 
# Class declarations
 
# Function declarations
 
def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags value]')
        print('-i seconds delay [int]')
        sys.exit(1)
 
# Main body
if __name__ == '__main__':
    main()

