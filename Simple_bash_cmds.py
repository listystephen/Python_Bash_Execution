import subprocess
import sys

def fun_call(*n):
        subprocess.call(n,shell = True)


def switch_fun():
        ch = int(input("Enter the no: \n \n 1 - Current directory \n 2 - list out the contents \n 3 - disk utilization \n 4 - User information \n \n"))
        if ch == 1:
                fun_call('pwd')
        elif ch == 2:
                fun_call('ls -l -t')
        elif ch == 3:
                fun_call('df -h')
        else:
                fun_call("df -h |grep usr/sap|awk '{print $6}'|cut -d'/' -f 4")

        rec = raw_input("Do you want to continue ?,press (y/n) : ")


        if (rec=='y'):
                switch_fun()
        else:
                print("Exited")


if __name__ == "__main__":
        switch_fun()