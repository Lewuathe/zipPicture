#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import commands
from datetime import date
from datetime import timedelta
from optparse import OptionParser

def setOptParser() :
    parser = OptionParser()

    parser.add_option("-a", "--all", dest="all", 
                  help="loop from past target date", action="store_true")
    
    return parser


def zip(targetDate):
    cmd = 'zip ' + targetDate + ' ' + targetDate + '*'
    print "[command] " + cmd
    commands.getstatusoutput(cmd)

if __name__ == "__main__":
    # your code

    parser = setOptParser()

    (options, args) = parser.parse_args()

    target = 0
    if len(args) > 0:
        target = int(args[0])

    targetDate = date.today() - timedelta(days=target)
    
    if options.all :
        while target >= 0:
            targetDate = date.today() - timedelta(days=target)
            target = target - 1
            zip(str(targetDate))
    else:
        zip(str(targetDate))



    
    
        
    

    
    
