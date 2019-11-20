import argparse
import sys
import time
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments Test")
    parser.add_argument('-v','--version',action="version",version='1.0.0',help="current version")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q','--quiet',action="store_true",default=True,help="console only returns Warnings, Errors, and Critical messages.")
    group.add_argument('-l','--loud',action="store_true",help="console returns all messages.")
    parser.add_argument('-o','-output',nargs="?",default=False,help="saves the console messages a log file.")

    args = parser.parse_args()

    Logger_Default_File_Path = "logs/log"
    
    print(args)


    if  args.o != False:
        if args.o != None:
            os.makedirs(os.path.dirname(f'{args.o}.log'), exist_ok=True)
            with open(f'{args.o}.log','a+') as f:
                f.write(f'{time.ctime()}\n')
        else:
            os.makedirs(os.path.dirname(f'{Logger_Default_File_Path}.log'), exist_ok=True)
            with open(f'{Logger_Default_File_Path}.log','a+') as f:
                f.write(f'{time.ctime()}\n')
 