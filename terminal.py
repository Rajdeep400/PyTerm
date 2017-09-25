import subprocess
import signal
import sys
import os
from os.path import expanduser
from os import popen
with os.popen('clear') as f:
	clear = f.read()
user=os.getenv('USER')
pc_name=os.uname()[1]



def main():
        while(1):
                try:
                        raise_parameter_error=0
                        comm=take_input()
                        command=comm.split()
                        i=0
                        while i<len(command):
                                if(command[i][-1:]=='\\' and (i+1<len(command))):
                                        command[i]=command[i][:-1]+" "+command[i+1]
                                        command.remove(command[i+1])
                                i+=1
                        parameters=[]
                        other=[]
                        for x in command[1:]:
                                if x[0]=='-':
                                        parameters+=list(x[1:])
                                        if x[1]=='-':
                                                raise_parameter_error=1
                                else:
                                        other+=[x]
			if command[0]=='cd':
                                cd_self(other)
			elif command[0]=='help':
                                help_display(other)
			else:
				subprocess.call(comm, shell = True)
                    
                except Exception as inst:
                        print "Error processing your request, use 'help' to get list of supported commands"

#####################################################
#### PROGRAM RELATED FUNCTIONS
#####################################################

def cd_self(other):
        if len(other)>0 and (os.path.isfile(other[0])==False) and (os.path.exists(other[0])==True):
                os.chdir(other[0])
        elif len(other)==0:
                os.chdir(os.environ['HOME'])
        elif os.path.isfile(other[0]):
                print "bash: cd: "+other[0]+": Not a directory" 
	else:
                print "bash: cd: "+other[0]+": No such file or directory"

#####################################################
#### LETS GIVE IT SOME TERMINAL TOUCH
#####################################################
# FROM http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def take_input():
        return raw_input(user+'@'+pc_name+':'+see_directory()+'$ ')

def signal_handler(signal, frame):
        print('')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def see_directory(x=0):
        path=os.getcwd()
        if x==0:
                return path.replace(os.environ['HOME'],'~',1)
        else:
                return path

def help_display(command):
	print open("helpdoc.txt","r").read()        

if __name__=="__main__":
        main()


