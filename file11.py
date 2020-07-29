import sys
f=open("pro.txt","r")
l=f.readline()
l2=f.readline()
sys.stdout.write(l)
sys.stdout.write(l2)
sys.stderr.write("No error occured\n")
