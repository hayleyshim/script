from keyboard import press_and_release, write
from time import sleep

command = "the command will be here soon!"
press_and_release("left windows + R") #this will open run
sleep(0.5)
write("cmd")#this will open cmd
press_and_release("enter")
sleep(0.5)
write(command)#this will the command inside the cmd
press_and_release("enter")