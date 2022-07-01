#!/usr/bin/python3
# -*- coding:utf-8 -*-

try:
    import os, sys
    import pywhatkit
except ImportError:
    import os



def grapher(filee) -> str:
    buildfile  = os.path.join(filee)
    for a in range(0, 1):
        pywhatkit.image_to_ascii_art(buildfile)


if __name__ == '__main__':
    # for w in (sys.argv):
    grapher(sys.argv[1])
    # for x in len(sys.argv):
        #if x > 1 :
        # print(x)
