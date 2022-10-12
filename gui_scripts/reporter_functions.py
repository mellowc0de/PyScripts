class Datacenter():
    dc_list=[]
    
    def __init__(self,*kwargs):
        self.name=input("Add DC name: ");
        self.state=input("Add DC state: ");
        self.city=input("Add DC city: ");

    def add_dc(self):
        dc.dc_list.append(self.name)
        return(dc.dc_list)
    

dc = Datacenter()


print(dc.add)