import tkinter as tk
import os
import netifaces
from tkinter import messagebox
from subprocess import call
import time

'''

to download netifaces library please refer to this :

https://zoomadmin.com/HowToInstall/UbuntuPackage/python3-netifaces

the subproccess :

https://pypi.org/project/subprocess.run/
'''

os.chdir(r'/home/pi/Documents') # the folder of all the files
root = tk.Tk()
root.title('Network configurations')

# the next lines are used to center the program

window_width=root.winfo_reqwidth()
window_height=root.winfo_reqheight()
pos_r = int(root.winfo_screenwidth()/2 - window_width/2)
pos_l = int(root.winfo_screenheight()/2 - window_height/2)

root.geometry("+{}+{}".format(pos_r,pos_l))


# all the next lines for entering the network configurations

ip_label = tk.Label(root,text = ' IP : ').grid(row=0,column=0)
subnet_label = tk.Label(root,text = ' Subnet Mask : ').grid(row=1,column=0)
gateway_label = tk.Label(root,text = ' Gateway : ').grid(row=2,column=0)
#mac_label = tk.Label(root,text = ' Mac address : ').grid(row=3,column=0)

ip_entry = tk.Entry(root,width=30)
ip_entry.grid(row=0,column=1)

subnet_entry = tk.Entry(root,width=30)
subnet_entry.grid(row=1,column=1)

gateway_entry = tk.Entry(root,width=30)
gateway_entry.grid(row=2,column=1)

#mac_entry = tk.Entry(root,width=30)
#mac_entry.grid(row=3,column=1)

# End of netwrok configuration enteries


# Next lines for Displaying the current network configurations

device = netifaces.ifaddresses('eth0') # device to find its network configurations

# IP

current_ip_text = tk.Label(root,text = 'Current IP   :   ').grid(row=6,column=0)
current_ip_number = device[netifaces.AF_INET][0]['addr'] # to get the current IP
current_ip__number_label = tk.Label(root,text = current_ip_number)
current_ip_number_place = current_ip__number_label.grid(row=6,column=1)
ip_entry.insert(0,current_ip_number) # display the current IP in the box entry


# Subnet

current_subnet_text = tk.Label(root,text = 'Current Subnet Mask   :   ').grid(row=7,column=0)
current_subnet_number = device[netifaces.AF_INET][0]['netmask'] # getting the subnet
current_subnet_number_label = tk.Label(root,text = current_subnet_number)
current_subnet_number_place = current_subnet_number_label.grid(row=7,column=1)
subnet_entry.insert(0,current_subnet_number) # display the current subnet in the box entry


#Gateway


current_gateway_text = tk.Label(root,text = 'Current Gateway   :   ').grid(row=8,column=0)
current_gateway_number = netifaces.gateways()['default'][netifaces.AF_INET][0] # Getting the gateway
current_gateway_number_label = tk.Label(root,text = current_gateway_number)
current_gateway_number_place = current_gateway_number_label.grid(row=8,column=1)
gateway_entry.insert(0,current_gateway_number) # display the current gateway in the box entry


# Mac

#current_mac_text = tk.Label(root,text = 'Current Mac address   :   ').grid(row=9,column=0)
#current_mac_number = device[netifaces.AF_LINK][0]['addr'] # getting the mac address
#current_mac_number_label = tk.Label(root,text = current_mac_number)
#current_mac_number_place = current_mac_number_label.grid(row=9,column=1)
#mac_entry.insert(0,current_mac_number) # display the current mac in the box entry




k = 1 # starting k value as one , this value will be used to check of other files exist with the same name


# the following dictionary is used to identify the user wanted Subnet Prefix from the subnet

subnet_dict = {'128.0.0.0':'/1',\
               '192.0.0.0':'/2',\
               '224.0.0.0':'/3',\
               '240.0.0.0':'/4',\
               '248.0.0.0':'/5',\
               '252.0.0.0':'/6',\
               '254.0.0.0':'/7',\
               '255.0.0.0':'/8',\
               '255.128.0.0':'/9',\
               '255.192.0.0':'/10',\
               '255.224.0.0':'/11',\
               '255.240.0.0':'/12',\
               '255.248.0.0':'/13',\
               '255.252.0.0':'/14',\
               '255.254.0.0':'/15',\
               '255.255.0.0':'/16',\
               '255.255.128.0':'/17',\
               '255.255.192.0':'/18',\
               '255.255.224.0':'/19',\
               '255.255.240.0':'/20',\
               '255.255.248.0':'/21',\
               '255.255.252.0':'/22',\
               '255.255.254.0':'/23',\
               '255.255.255.0':'/24',\
               '255.255.255.128':'/25',\
               '255.255.255.192':'/26',\
               '255.255.255.224':'/27',\
               '255.255.255.240':'/28',\
               '255.255.255.248':'/29',\
               '255.255.255.252':'/30',\
               '255.255.255.254':'/31',\
               '255.255.255.255':'/32'}



def user_click(): # when the user click save
    
    
    
    user_response = messagebox.askquestion('Are you sure ?','Are you sure you want to save these changes ? the system will restart')
    
    if user_response == 'yes':
        
        subnet_perfix = subnet_dict.get(subnet_entry.get()) # getting the subnet prefix from the dictionary
        
        network_file = open('/etc/dhcpcd.conf','w') # this file is used for static network configurations

        # the next lines of code will write the network configuration we want in the file
        # these configuration takes place only when the system restart
        
        network_file.write('interface eth0\n') # the device is eth0
        network_file.write('static ip_address='+ip_entry.get()+subnet_perfix+'\n') # writing IP and the prefix of the subnet mask
        network_file.write('static routers='+gateway_entry.get()+'\n')
        network_file.write('static domain_name='+gateway_entry.get()) # the last two lines for the gateway
        
        
        
                
        def save_changes(): # this function is used to save the new configuration in a txt file
            global k
            
            try:

                f = open('Netwrok Configuarotion {number}.txt '.format(number = k),'x') # 'x' means writing a new file
                f.write('IP   :  ')
                f.write(ip_entry.get())
                f.write('\nSubnet   :  ')
                f.write(subnet_entry.get())
                f.write('\nGateway   :  ')
                f.write(gateway_entry.get())
                #f.write('\nMac address   :  ')
               # f.write(mac_entry.get())
                call(['sudo','reboot']) # reboot the system after writiing the configurations
                
            except FileExistsError as file_error: # if a file of the same name exist , increment k by 1 ( it will change the file name )
                k = k+1
                save_changes()
        save_changes()
        
    
        



save_button = tk.Button(root,text=' Save ',command = user_click)
save_button.grid(row=4,column=0)


root.mainloop()





