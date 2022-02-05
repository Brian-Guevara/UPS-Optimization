# Brian Guevara
# StudentID: 001003681

# Distances.py
# This class has our main methods for: calculating distance, time difference, and our greedy algorithm
# Overall, this is the class that finds the distances between locations.

import csv
import datetime

# This opens the custom DistanceData file, reads each line on the file and separates each value by the ',' character
# Big-O: O(N)
with open('WGUDistanceData.csv') as csvfile:
    distCSV = csv.reader(csvfile, delimiter=',')
    distCSV = list(distCSV)

# This is a separate CSV file with the names of the buildings and their own IDs
# Big-O: O(N)
with open('WGUDistanceNameData.csv') as csv_name_file:
    name_readCSV = csv.reader(csv_name_file, delimiter=',')
    address_names = list(name_readCSV)


# Gets the distance between 2 places
# Big-O: O(1)
def distance_between(row, col):
    distance = distCSV[row][col]
    if distance is '':
        distance = distCSV[col][row]
    return float(distance)


# Adds the time taken it takes to cross 'distance' and add to the time
# Big-O: O(1)
def find_time_difference(distance, time_list):
    # Gets the total number of hours by dividing the distance by 18
    hours = (distance / 18)
    # Grabs the remaining number of minutes
    minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(hours * 60, 60))

    # Add the current number of minutes needed
    final_time = minutes + ':00'
    time_list.append(final_time)

    # Parse data for the time
    time_difference = datetime.timedelta()
    # This for loop is hard coded. That is why this Big-O is not O(N) for this method.
    for i in time_list:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        time_difference += d
    return time_difference


# # # # # # # # # # # # # # #     A L G O R I T H M     # # # # # # # # # # # # # # #
# This is our greedy algorithm. The process involves checking and comparing the distances to the remaining addresses
# to the current address. The current address with the current lowest distance will have its distance recorded and
# passed down. The method will return our address ID as an integer
# Big-O: O(log N)
def find_closest_place(Node, current_location, lowest_value):
    # this value will be our next stop/address. It requires a global keyword because otherwise, the program could
    # return several integers after several recursions.
    global destination

    # If the current node is None, then go back/leave
    if Node is None:
        return
    else:
        # Get the address ID
        address_id = int(Node.data)
        # If the distance between this address and current location is less than the current lowest value
        if distance_between(address_id, current_location) <= lowest_value:
            # Assign a new lowest value
            lowest_value = distance_between(address_id, current_location)
            # Set this address as our destination, for now
            destination = address_id

        # Recursively call the method. Our global value will be carried on without issue
        find_closest_place(Node.left, current_location, lowest_value)
        find_closest_place(Node.right, current_location, lowest_value)
    return destination




# Returns list of addresses
# Big-O: O(1)
def get_Address():
    return address_names

