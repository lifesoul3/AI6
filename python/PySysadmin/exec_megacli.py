import os
from subprocess import Popen

def megacli(args):
    os.chdir('/opt/lsi/MegaCLI')
    cmd='./MegaCli '+args
    Popen(cmd,shell=True)

if __name__=="__main__":
    megacli('-AdpGetTime -aAll')
    