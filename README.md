# Changing-Network-Configurations-In-Linux
the code of this repository is using Tkinter GUI to display current Network configurations and entries to enter a new one.




There are multiple ways to change the network configurations in Linux , but to permanently write new configurations I’m using a python code to write to the “ dhpcd.conf “ file located in the “etc” folder.
Note that the system will restart after writing to this file since the new configurations only take place after the system restart.

The code displays a GUI using Tkinter and the user will input the desired configurations.
After the user press save it will ask “are you sure” , if the user press yes then the new network configurations will be written in a txt file and the system will restart with the new network configurations.
