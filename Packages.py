# Brian Guevara
# StudentID: 001003681

# Packages.py
# This package calls our input data, data structure + algorithm, our distance functions, and more
# This class will pack the trucks, get calculate the total distance across the trucks and
# register the time of delivery


import datetime
from Binary_Tree import get_size, truck_bt
from Distances import find_time_difference, distance_between, find_closest_place
from InputDataCSV import get_first_addresses, get_first_packages, get_second_addresses, \
    get_second_packages, get_third_addresses, get_third_packages

# the times below represent the times that each truck leaves the hub
first_time = '8:00:00'
second_time = '9:10:00'
third_time = '11:00:00'

# These values will be our total distance for each truck
first_total_distance = float()
second_total_distance = float()
third_total_distance = float()

# Trucks initial binary trees and final lists
first_packages = get_first_packages()
first_addresses = get_first_addresses()

second_packages = get_second_packages()
second_addresses = get_second_addresses()

third_packages = get_third_packages()
third_addresses = get_third_addresses()


#  This method sets the 'leave' time for every package in a truck
# Big-O: O(log N)
def set_initial_time(start_node, time_package_leaves_hub):
    if start_node is None:
        return
    set_initial_time(start_node.left, time_package_leaves_hub)
    start_node.data[9] = time_package_leaves_hub
    set_initial_time(start_node.right, time_package_leaves_hub)


# This method sets the delivery time for every applicable package
# Big-O: O(log N)
def set_delivery_time(Node, address_id, time_package_is_delivered):
    # If Node is empty then return
    if Node is None:
        return
    else:
        # If address ID of package equals the address id of this location, then set the time

        if Node.data[1] == address_id:
            Node.data[10] = str(time_package_is_delivered)
        # Continue to set the delivery time for other nodes
        set_delivery_time(Node.left, address_id, time_package_is_delivered)
        set_delivery_time(Node.right, address_id, time_package_is_delivered)


# Set the leave time for all the packages in every truck
set_initial_time(first_packages.root, first_time)
set_initial_time(second_packages.root, second_time)
set_initial_time(third_packages.root, third_time)

# The loops will run through the address binary trees until they are empty.
# It will find the next stop, remove it from the address, add up the distance to the location
# get the time difference to the location, and then set it as the current location
# Big-O: O(N) for all 3 loops

current = 0
while get_size(first_addresses.root) != 0:
    # Find the closest place
    next_stop = find_closest_place(first_addresses.root, current, 10)
    # Add stop to our address queue

    # Remove this stop from the tree, so we can continue searching from the location
    # (without it in the 'map')
    first_addresses.remove_add_id(next_stop)

    # Add distance to sum
    first_total_distance += distance_between(next_stop, current)

    # Get the difference in time between current stop and found/next stop
    difference_in_time = find_time_difference(distance_between(next_stop, current), [first_time])

    # Set the delivery time for packages that will be delivered to this address
    set_delivery_time(first_packages.root, next_stop, difference_in_time)

    # Update the time
    first_time = str(difference_in_time)

    # Set the next address
    current = next_stop
# Finally, we will add the distance and time it takes from the last stop to the hub
first_total_distance += distance_between(current, 0)
first_time = str(find_time_difference(distance_between(current, 0), [first_time]))

current = 0



# We will make 24 our first stop on the trip. Otherwise, it is the last stop
# and this package will end up late.
second_addresses.remove_add_id(24)
second_total_distance += distance_between(24, current)
difference_in_time = find_time_difference(distance_between(24, current), [second_time])
set_delivery_time(second_packages.root, 24, difference_in_time)
second_time = str(difference_in_time)
current = 24

# While loops for second and third truck addresses are ran the same as the first.
while get_size(second_addresses.root) != 0:
    next_stop = find_closest_place(second_addresses.root, current, 10)

    second_addresses.remove_add_id(next_stop)

    second_total_distance += distance_between(next_stop, current)

    difference_in_time = find_time_difference(distance_between(next_stop, current), [second_time])

    set_delivery_time(second_packages.root, next_stop, difference_in_time)

    second_time = str(difference_in_time)

    current = next_stop
second_total_distance += distance_between(current, 0)
second_time = str(find_time_difference(distance_between(current, 0), [second_time]))

current = 0
while get_size(third_addresses.root) != 0:
    next_stop = find_closest_place(third_addresses.root, current, 10)

    third_addresses.remove_add_id(next_stop)

    third_total_distance += distance_between(next_stop, current)

    difference_in_time = find_time_difference(distance_between(next_stop, current), [third_time])

    set_delivery_time(third_packages.root, next_stop, difference_in_time)

    third_time = str(difference_in_time)

    current = next_stop
third_total_distance += distance_between(current, 0)
third_time = str(find_time_difference(distance_between(current, 0), [third_time]))


# Following methods return the time of return of the 3 trucks (2 trucks, one with 2 trips)
# Big-O: O(1)
def get_first_finish_time():
    return first_time


# Big-O: O(1)
def get_second_finish_time():
    return second_time


# Big-O: O(1)
def get_third_finish_time():
    return third_time


# Last function returns the total miles of all 3 trucks
# Big-O: O(1)
def total_distance():
    return first_total_distance + second_total_distance + third_total_distance
