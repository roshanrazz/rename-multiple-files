# put all your files to be renamed in "filehere" folder. 

import os

cwd = os.getcwd()
path = os.path.join(cwd,"filehere")
os.chdir(path)

ext = input("Enter file extension : ")
filename = os.listdir()
x=1
	
for i in filename:
	os.rename(i,f"{x}.{ext}")
	x+=1
	
	
		