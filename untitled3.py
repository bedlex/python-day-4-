class battery():
    volts =7.8
    def __init__(self,cells):
        self.cells = cells
class car():
    def __init__(self,year,make,model,battery):
        self.year = year
        self.make = make
        self.model = model
        self.battery = battery
      
    
    
batt = battery(6)
tesla = car("2019","tesla","model-x", batt)
print(tesla.battery.cells)
print(tesla.battery.volts)