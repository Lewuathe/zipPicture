# -*- coding: utf-8 -*-

import os
import sys
import commands

if __name__ == "__main__":
    pics = [pic for pic in os.listdir('.') if pic.startswith('DSCN')]
    for pic in pics:
        cmd = "sips -g all " + pic +  "  | grep creation | awk '{print $2,$3}'"
        out = commands.getoutput(cmd).split()
        dst = out[0].replace(':', '-') + ' ' + out[1].replace(':', '.') + '.jpg'
        print '{pic} ->  {dst}'.format(pic=pic, dst=dst)
        os.rename('./' + pic, './' + dst)
