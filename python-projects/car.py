class Car:

    def __init__(self, color, engine_type, gas_tank, odometer):
        self.color = color
        self.engine_type = engine_type
        self.gas_tank = gas_tank
        self.odometer = odometer

    def __str__(self):
        return "The " + self.color + " car has the following engine type: " + self.engine_type
    

    def drive(self):
        if self.engine_type == "4_cylinder":
            self.gas_tank -= 3
            self.odometer += 90

        if self.engine_type == "V8":
            self.gas_tank -= 4
            self.odometer += 50

        return f"The {self.color} car just drove!"
    

    def get_gas_tank(self):
        return f"There are {self.gas_tank} gallons left in the car"
    

    def get_odometer(self):
        return f"The odometer is now at level {self.odometer}"