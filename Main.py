#Student ID = 011023634
# the follow up questions for this projects is found in the requirements.docx file in this folder

import csv
import datetime



from Truck import Truck  # Import the Truck class from the Truck.py file



from builtins import ValueError


# import from the hashTable 

from HashTable import HashTableMap


#import from the Packages
from Package import Package


#this fuction loads data and insert them into the hashtable 
def load_package_data(filename, package_hash_table):



    with open(filename, encoding="utf-8-sig") as package_info:  # Add 'utf-8-sig' encoding to handle hidden character
        package_data = csv.reader(package_info)
        next(package_data)  # Skip the header row
        for package in package_data:
            pID = package[0].strip()
            if not pID.isdigit():
                #print(f"Invalid package ID: {pID}. Skipping this row.")
                continue
            
            pID = int(pID)

            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            # Handle missing or invalid distance data by setting it to a default value (e.g., 0.0)
            pDeadline_time = package[5] if package[5] else "00:00:00"
            pWeight = package[6] if package[6] else "0"
            pStatus = "At Hub"
            # Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)
            # Insert data into hash table
            package_hash_table.insert(pID, p)





# Step 4: Create distanceData List



distanceData = []



# Step 5: Define loadDistanceData(distanceData) function


# Step 5: Define loadDistanceData(distanceData) function


def loadDistanceData(distanceData, filename):


    with open(filename, 'r') as csvfile:


        csvreader = csv.reader(csvfile)


        for row in csvreader:


            distanceData.append([float(cell) if cell != '' else 0.0 for cell in row])



# Call the function to load distance data from the CSV file


loadDistanceData(distanceData, "WGUPS Distance Table.csv")



# Create addressData List


addressData = []

# Define loadAddressData(addressData) function

def loadAddressData(addressData, filename):
    with open(filename, newline='') as csvfile:
        csv_address = csv.reader(csvfile)        
        for row in csv_address:
            if row:  # Ensure the row has at least three cells
              # Combine second and third cells
                address = row[0].strip()
                addressData.append(address)
                
# Call the function to load address data from the CSV file
loadAddressData(addressData, "Address_File.csv")

   


# Create hash table
package_hash_table = HashTableMap()
# Load packages into hash table 
load_package_data("WGUPS Package File.csv", package_hash_table)




# Define a function to return the distance between two addresses using indices
def distanceBetween(index1, index2):
    return distanceData[index1][index2]



# Create truck object truck1
truck1 = Truck(1,16, 18, None, [1, 13, 14, 15, 16,19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))


package_array1 = truck1.packages

for id in package_array1:
    pkg1 = package_hash_table.lookup(id)
    pkg1.departure_time = truck1.depart_time
    
    
for id in package_array1:
    pkg1 = package_hash_table.lookup(id)
    
    

# Create truck object truck2
truck2 = Truck(2,16, 18, None, [3, 6, 12, 17, 18, 9, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))


package_array2 = truck2.packages

for id in package_array2:
    pkg2 = package_hash_table.lookup(id)
    pkg2.departure_time = truck2.depart_time
    
    
for id in package_array2:
    pkg2 = package_hash_table.lookup(id)
    
    
    
# Create truck object truck3
truck3 = Truck(3,16, 18, None, [2, 4, 5, 6, 7, 8,  10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

package_array3 = truck3.packages

for id in package_array3:
    pkg3 = package_hash_table.lookup(id)
    pkg3.departure_time = truck3.depart_time
    
    
for id in package_array3:
    pkg3 = package_hash_table.lookup(id)
    

def minDistanceFrom(fromAddress, truckPackages):
    fromIndex = addressData.index(fromAddress)
    next_index = 0
    

    # Create a dictionary to map package IDs to their corresponding pAddress values
    package_to_address = {}
    for pID in truckPackages:
        package = package_hash_table.lookup(pID)  # Assuming package_hash_table is your package lookup table
        if package:
            package_to_address[pID] = package.address

    min_distance = float('inf')
    min_distance_index = None
    for pID, pAddress in package_to_address.items():
        # Find the index of the pAddress in the addressData list
        addressIndex = addressData.index(pAddress)
        

        distance = distanceBetween(fromIndex, addressIndex)
    
        if distance == 0:
            
            distance = distanceBetween(addressIndex, fromIndex)
            
            
        
        #print(f"distance: {distance}")
        if distance < min_distance:
            min_distance = distance
            min_distance_index = addressIndex
            next_index = pID

    return min_distance, min_distance_index, next_index

#fuction accepts a truck delivers the packages and calculates the miles together 
def deliverPackages(myTruck):
    miles = 0 
 
    #for truck in myTruck:
    fromAddress = "4001 South 700 East"
    myTruck_packages = myTruck.packages
    current_time = myTruck.depart_time
    #for  packages in myTruck_packages:
    while len(myTruck_packages)>0:
            #minDistance
        minimum, next_index, next_ID = minDistanceFrom(fromAddress, myTruck_packages)
        #print(f"\nClosest address to {fromAddress} for truck1: {minimum} and {next_index} and packageID: {next_ID}")
    
        miles += minimum
        time_delivered = (minimum/ 18) *60*60
        
        #date time object to be in seconds so that it will be updated 
        time_obj = datetime.timedelta(seconds=time_delivered)
        current_time += time_obj
        
        #myTruckDeparture = myTruck.depart_time
        #depart_time = myTruck.depart_time + time_obj
        
        myTruckNum = myTruck.truck_id
        fromAddress = addressData[next_index]
        
        package_delivered = package_hash_table.lookup(next_ID) 
        
        package_delivered.delivery_time = current_time
       
        package_delivered.status = "Delivered"    
        
        myTruck_packages.remove(next_ID)   
    return miles  
    
# Create a list of truck objects


# Call the deliverPackages function
truck1_miles = deliverPackages(truck1)
truck2_miles = deliverPackages(truck2)
truck3_miles = deliverPackages(truck3)



print(f"Total miles driven: {(truck1_miles+truck2_miles+truck3_miles)}") 



def output():
    while True:        
        user_input = input("""
        Please select an option below to begin or type 'quit' to quit:
        1. Print all packages with the total miles
        2. Get info for all packages at a particular time
        3. Get info for a single package at a particular time
        4. quit 
        """)
    
        if user_input == '1':
        
            for package_id in range(1, len(package_hash_table.list) + 1):
                package = package_hash_table.lookup(package_id)
                print(package)
            print(f"\nTotal miles driven: {(truck1_miles+truck2_miles+truck3_miles)}")

        elif user_input == '2':
            input_time_str = input('Enter time (HH:MM:SS): ')
            try:
                input_time = datetime.datetime.strptime(input_time_str, '%H:%M:%S').time()
                input_timedelta = datetime.timedelta(hours=input_time.hour, minutes=input_time.minute, seconds=input_time.second)
            except ValueError:
                print("Invalid time format. Please use HH:MM:SS.")
            else:
                print("Packages at or before", input_time_str, ":\n")

                for package_id in range(1, len(package_hash_table.list) + 1):
                    package = package_hash_table.lookup(package_id)
                    if package is not None and package.departure_time is not None:
                        if input_timedelta < package.departure_time:
                            if package_id == 9:
                                package.address = "300 State St"

                            package.status = "At Hub"
                            
                            print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.status} ")
                        elif package.departure_time <= input_timedelta <= package.delivery_time:
                            if package_id == 9:
                                package.address = "410 S. State St."
                            package.status = "In route"
                             
                            print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.status} ")
                            
                        elif input_timedelta > package.delivery_time:
                            package.status = "Delivered"
                            print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.delivery_time}, {package.status} ")
                        
        elif user_input == '3':
            package_id = input('Enter package ID: ')
            try:
                package_id = int(package_id)
            except ValueError:
                print("Invalid package ID format. Please enter a valid integer.")
                continue

            package = package_hash_table.lookup(package_id)
            if package is not None:
                input_time_str = input('Enter time (HH:MM:SS): ')
                try:
                    input_time = datetime.datetime.strptime(input_time_str, '%H:%M:%S').time()
                    input_timedelta = datetime.timedelta(hours=input_time.hour, minutes=input_time.minute, seconds=input_time.second)
                except ValueError:
                    print("Invalid time format. Please use HH:MM:SS.")
                else:
                    if input_timedelta < package.departure_time:
                        if package_id == 9:
                            package.address = "300 State St"
                        package.status = "At Hub"
                        
                        print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.status} ")
                        
                    elif package.departure_time <= input_timedelta <= package.delivery_time:
                        if package_id == 9:
                            package.address = "410 S. State St."
                        package.status = "In route"
                     
                        print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.status} ")
                        
                    elif input_timedelta > package.delivery_time:
                        package.status = "Delivered"
                        print(f"Package {package.ID}, {package.address}, {package.Deadline_time}, {package.delivery_time}, {package.status} ")
            else:
                print("Package not found.")
                           
        elif user_input.lower() == '4':
            print("Quitting...")
            break 
        else:
            print("Invalid input. Please select a valid option.")


if __name__ == "__main__":
    output()