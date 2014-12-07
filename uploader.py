#!/usr/bin/env python3 -tt
"""
Tests rsync with amazon s3 using random data. Connection layer to amazon s3 is handled by s3fs-fuse. Python as the scripting language
"""
 
# Imports
import sys
import pdb
import os
from subprocess import call
import uuid
import shutil
import time

#import os
 
# Global variables
 
# Class declarations
 
# Function declarations
def ensure_dir(f):
    d = os.path.dirname(f)
    #pdb.set_trace()
    if not os.path.exists(d):
        myprint('creating directory: ' + f)
        os.makedirs(d)

def myprint(msg):
    with open("output.txt", "a") as myfile:
      myfile.write(str(msg) + "\r\n")
    print(str(msg))
 
def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags value]')
        print('-i seconds delay [int]')
        sys.exit(1)

    ensure_dir('./uploads/')

    infiniteLoop = 1
    while (infiniteLoop == 1):

      diruuid = uuid.uuid1()
      rsyncdir = './uploads/'+ diruuid.urn[9:]

      os.makedirs(rsyncdir)
      for x in range(0, 3):
        shutil.copy("./wallpaper2.jpg", rsyncdir + "/wallpaper_" + str(x))

      return_code = call("ls -l ./uploads", shell=True) 
      myprint("\r\nListing directory: " + rsyncdir);
      return_code = call("ls -l " + rsyncdir, shell=True)
      myprint(return_code);
    
      myprint("Calling rsync....");
      start = time.time()
      return_code = call("/usr/bin/rsync -r --inplace ./uploads/ /home/kosiara/s3mnt/rsync", shell=True)
      end = time.time()
      time_elapsed = end - start
    
      myprint("Upload size: ")
      call("du -hs ./uploads/ >> output.txt", shell=True)
      myprint("Number of files:")
      call("find ./uploads -type f | wc -l >> output.txt", shell=True)
      myprint(str(time_elapsed) + " sec.")
    
      myprint("Sleeping 10 sec")
      time.sleep( 10 )
 
# Main body
if __name__ == '__main__':
    main()


