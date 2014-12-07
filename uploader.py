#!/usr/bin/env python3 -tt
"""
Tests rsync with amazon s3 using random data. Connection layer to amazon s3 is handled by s3fs-fuse. Python as the scripting language
"""
 
# Imports
import sys
import pdb
import os
from subprocess import call
#import os
 
# Global variables
 
# Class declarations
 
# Function declarations
def ensure_dir(f):
    d = os.path.dirname(f)
    pdb.set_trace()
    if not os.path.exists(d):
        print('creating directory: ' + f)
        os.makedirs(d)


 
def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags value]')
        print('-i seconds delay [int]')
        sys.exit(1)

    ensure_dir('./uploads/')

    return_code = call("ls -l", shell=True) 
    print(return_code);
 
# Main body
if __name__ == '__main__':
    main()


