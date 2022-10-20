class Datacenter:
    dc_list=[]
    
    def __init__(self,*kwargs):
        self.name=input("Add DC name: ").upper();
        self.state=input("Add DC state: ").upper();
        self.city=input("Add DC city: ").upper();

    def add_dc(self):
        dc.dc_list.append(self.name)
        return(dc.dc_list)
    

dc = Datacenter()


print(dc.add_dc())