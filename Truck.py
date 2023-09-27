class Truck:
    def __init__(self, truck_id, capacity, speed, load, packages, mileage, address, depart_time):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time 



        # Additional attribute to track the delivered packages and their associated truck
        #self.delivered_packages = []

    def __str__(self):
        return "%s,%s, %s, %s, %s, %s, %s, %s" % (self.truck_id, self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.depart_time)

