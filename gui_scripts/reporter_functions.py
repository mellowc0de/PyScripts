class Datacenter(object):
    def __init__(self,*kwargs):
        self.name=input("Add DC name: ");
        self.state=input("Add DC state: ");
        self.city=input("Add DC city: ");
        
    def dcList(self):
        dc_list=[]
        dc_list.append(self.name)
        return(dc_list)
    

newDC=Datacenter()

print(newDC.dcList())