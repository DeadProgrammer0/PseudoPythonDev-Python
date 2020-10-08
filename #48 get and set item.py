# Getitem and Setitem.

# An ordinary class.
class Company1:

    def __init__(self):
        self.new_item = {}

    def set_item(self,name,date):
        self.new_item[name] = date

    def get_item(self,item):
        return self.new_item[item]

#This Method is doing the work but its too repeatative and lengthy.

Mc_Donalds = Company1()
Mc_Donalds.set_item("Mc CheeseBurst", "2020-9-11")
Mc_Donalds.set_item("Mc ChickenPick","2019-2-20")

print(Mc_Donalds.get_item("Mc ChickenPick"))

class Company2:

    def __init__(self):
        self.new_item = {}

    def __setitem__(self,name,date):
        self.new_item[name] = date

    def __getitem__(self,item):
        return self.new_item[item]

# This is why we should use getitem and setitem. It makes our code neat and effecient.

SubWay = Company2()
SubWay["ChillyChick"] = "2020-11-2"
SubWay["VeggyDelight"] = "2019-1-22"

print(SubWay["VeggyDelight"])

