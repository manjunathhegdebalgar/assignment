""" Program to ping and check the status of an IP nad to list all the installed softwares"""
import os


def check_ping(ip):
    hostname = ip
    response = os.system("ping -c 1 " + hostname)
    # checking the response
    if response == 0:
        ping_status = "Network Active"
    else:
        ping_status = "Network Error"

    return ping_status


host_name = str(input("Enter a hostname to ping and check status"))
print(check_ping(host_name))
print(".........printing all the installed softwares.......")
print(os.system("apt list --installed"))
