#!/usr/bin/env python

# This file is an example of multiple inheritance
# To view the code run the python interactive shell
#  enter the the following:
# >>> from oop_practice import *
# Add DC name:  SITE
# Add DC state:  STATE
# Add DC city:  CITY NAME
# Add DC manager: MANAGER NAME
# How many PODs? POD COUNT
# How many ROWs in the DC?  ROW COUNT
# How many Racks in the DC? RACKS COUNT
# ----------------------------------------------------------------
# <oop_practice.addDatacenter object at 0x000001326A4AA410>
# ----------------------------------------------------------------
# Datacenter:  SITE
# City:  CITY NAME
# State:  STATE
# Manager:  MANAGER NAME
# PODs:  POD COUNT
# Rows:  ROW COUNT
# Racks:  RACKS COUNT
# None
# ----------------------------------------------------------------
# >>> 
# Output: 
# >>> 
# Output: 

class addDatacenter:    
    def __init__(self):
        """Initialize the Datacenter class. Input data for DC name, state, 
        city, manager, and pod count.
        """
        self.name=input("Add DC name:  ").upper();
        self.state=input("Add DC state:  ").upper();
        self.city=input("Add DC city:  ").upper();
        self.manager=input("Add DC manager: ").upper();
        self.pods=int(input("How many PODs?  "));  # type: ignore
        self.rows=int(input("How many ROWs in the DC?  "));  # type: ignore
        self.racks=int(input("How many Racks in the DC?  "));  # type: ignore
        
    def create_dc_pods(self):
        """Uses self.pods integer as the dc pod count as well as to form 
        the names that are appended to dc_pod_list
        """
        dc_pod_count = self.pods

        try:
            if type(dc_pod_count) is int:
                # DC POD List collects pod names from data input of self.pods
                dc_pod_list = []
                
                for pod_int in (n+1 for n in range(dc_pod_count)):
                    pod_int = "POD" + str(pod_int)
                    dc_pod_list.append(pod_int)
                    
                    print(dc_pod_list) # print statement for testing purposes
            else:
                print("not a valid number")

        except TypeError:
            print("Input must be an integer")
    
    def create_dc_rows(self):
        """Uses self.rows to determine the total number of rows in the Datacenter.
        """
        dc_rows_count = self.rows

        try:
            if type(dc_rows_count) is int:
                # DC POD List collects pod names from data input of self.pods
                dc_rows_list = []
                
                for row_int in (n+1 for n in range(dc_rows_count)):
                    row_int = "ROW" + str(row_int)
                    dc_rows_list.append(row_int)
                    
                    #print(dc_rows_list) # print statement for testing purposes
            else:
                print("not a valid number")

        except TypeError:
            print("Input must be an integer")
    
    def create_dc_racks(self):
        """Defines the PODs and their respective rows in the Datacenter
        """
        dc_racks_count = self.racks
        
        try:
            if type(dc_racks_count) is int:
                # DC POD List collects pod names from data input of self.pods
                dc_racks_list = []
                
                for rack_int in (n+1 for n in range(dc_racks_count)):
                    rack_int = "RACK" + str(rack_int)
                    dc_racks_list.append(rack_int)
                    
                    #print(dc_racks_list) # print statement for testing purposes
            else:
                print("not a valid number")

        except TypeError:
            print("Input must be an integer")
    
    def dc_info(self):
        """Prints all the information collected and processed within createDatacenter class"""
        dc_info_txt = "Datacenter:  {} \nCity:  {} \nState:  {} \nManager:  {} \nPODs:  {} \nRows:  {} \nRacks:  {}".format(self.name, self.city, self.state, self.manager, self.pods, self.rows, self.racks)
        
        print(dc_info_txt)
 
      
dc = addDatacenter()


 
print("----------------------------------------------------------------")
print(dc)
#print(dc.create_dc_pods())  # print statement for testing purposes
#print(dc.create_dc_rows())  # print statement for testing purposes
#print(dc.create_dc_racks())  # print statement for testing purposes
print("----------------------------------------------------------------")
print(dc.dc_info())
print("----------------------------------------------------------------")