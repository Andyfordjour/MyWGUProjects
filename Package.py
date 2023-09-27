# Create class for packages
class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck_delivered = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.Deadline_time, self.weight, self.delivery_time,
                                                       self.status)
"""
    def update_status(self, convert_timedelta):
        if self.delivery_time and  self.delivery_time < convert_timedelta:
            self.status = "Delivered"
            #self.truck_delivered = truck_id
        elif self.departure_time and self.departure_time > convert_timedelta:
            self.status = "En route"
            #self.truck_delivered = truck_id
        else:
            self.status = "At Hub"
            #self.truck_delivered = None
"""        

   

        
        