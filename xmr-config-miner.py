import os
import subprocess
from datetime import date

#! Path var
LINUX_PATH = "xmrig-6.15.3-Linux/"
WINDOWS_PATH = "\\xmrig-6.15.3-Windwos"
FREEBSD_PATH = "xmrig-6.15.3-FreeBSD/"
MACOSX64 = "xmrig-6.15.3-MacOSx64/"
MACOSARM = "xmrig-6.15.3-MacOSarm/"

#! Config
#Pool Info
pool = "gulf.moneroocean.stream"
port = "10128"
user = "83BtAgSG22x4mWKGvARh1Rc6CGg7H2hsdQnwYdzTdbshTei3QX6puHUZ9srSf26M9qFoQzw1uXZdEhJ9XnBefXQJGGsEYa2" #?Wallet Adress
password = "main_PC" #?Password or ID

#Server Config
threads = 6
gpu = True
gpu_nvidea = True
gpu_amd = False

#Logs and Output
logging = True
health_output = True
hashrate_output = True
intervall_outputs = 10


#! Code
#Command
command = "-o " + pool + ":" + port + " -u " + user + " -p " + password + " --threads=" + str(threads) + " "

linux_cmd = "./xmrig "
win_cmd = "xmrig.exe "


#GPU
if gpu == True:
    if gpu_nvidea & gpu_amd == True:
        command = command + "--opencl --cuda"
    elif gpu_nvidea == True:
        command = command + "--cuda "
    elif gpu_amd == True:
        command = command + "--opencl "


#OS
os = str(input("What OS are you running? \nWindows, Linux, FreeBSD, MacOS x64, MacOS ARM (M1) \n(W / L / F / Mx64 / M1) press Enter to continue, Ctrl + c to cancel\n"))

if os == "W" or os == "w":
    command = win_cmd + command
elif os == "L" or os == "l":
    command = linux_cmd + command
elif os == "F" or os == "f":
    command = linux_cmd + command
elif os == "Mx64" or os == "mx64":
    command = linux_cmd + command
elif os == "M1" or os == "m1":
    command = linux_cmd + command
else:
    print("Error! Wrong Input \nOnly W or L are valid!")
    exit()

#Logging
today = date.today()
d = today.strftime("%d-%m-%Y")

filename_linux = "logs/" + d + ".log"
filename_win = "\\logs\\" + d + ".log"

if os == "L" or "l" or "F" or "f" or "Mx64" or "mx64" or "M1" or "m1":
    filename = filename_linux
elif os == "W" or "w":
    filename = filename_win


if logging == True:
    command = command + "--log-file=" + filename + " "

if health_output == True:
    command = command + "--print-time=" + str(intervall_outputs) + " "
if hashrate_output == True:
    command = command + "--health-print-time=" + str(intervall_outputs) + " "


#Pritn raw resulr
print("\n \n" + command)

#execute the comand in the sehll
if os == "W" or os == "w":
    command_execute = "cd " + WINDOWS_PATH + " ; " + command
elif os == "L" or os == "l":
    command_execute = "cd " + LINUX_PATH + " && " + command
elif os == "F" or os == "f":
    command_execute = "cd " + FREEBSD_PATH + " && " + command
elif os == "Mx64" or os == "mx64":
    command_execute = "cd " + MACOSX64 + " && " + command
elif os == "M1" or os == "m1":
    command_execute = "cd " + MACOSARM + " && " + command
else:
    print("Fatal executuion Error!")

print(command_execute)

subprocess.call(command_execute, shell=True)
