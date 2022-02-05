# Brian Guevara
# StudentID: 001003681

# InputDataCSV.py
# File imports the csv class, map object from the Hash file, and some Binary Tree functions

import csv

import Distances
from Binary_Tree import Node, has_package, get_size
from Binary_Tree import truck_bt, address_bt
from Hash import Map

# opens the custom WGUInputData csv file and creates a delimiter for it to read the values.
# Big-O: O(N^2) . We have 2 for loops in this method

with open('WGUInputData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # After opening the file, we will create a hash table and BSTs for our trucks. The 3rd truck is just the 1st truck
    # taking its second trip. Each truck has a Binary Tree for
    Hash_Map = Map()
    initial_package_first = truck_bt()
    initial_address_first = address_bt()

    initial_package_second = truck_bt()
    initial_address_second = address_bt()

    initial_package_third = truck_bt()
    initial_address_third = address_bt()

    # The values in the CSV value are parsed by the delimiter and assigned to the correct fields as noted below
    # this is done for every line in the input file (every package)
    # Big-O: O(N^2)
    for col in readCSV:
        package_ID = col[0]
        street_address = col[1]
        city = col[2]
        state = col[3]
        zip_code = col[4]
        delivery_time = col[5]
        mass_kg = col[6]
        note = col[7]
        address_id = ''
        for address in Distances.get_Address():
            if street_address == address[2]:
                address_id = int(address[0])

        # value is our package object. Notice that we moved the address ID to the second field.
        # The last two values are the time the packages leaves the hub and the time it is delivered
        value = [package_ID, address_id, street_address, city, state,
                 zip_code, delivery_time, mass_kg, note, '', '']

        # Hash Key of the package is the ID itself
        key = package_ID

        # From this point, we will add the packages to binary trees. Our algorithm will use binary trees and
        # recursion to find the shortest paths

        # If the package with the wrong address appears, then fix it and add to the third truck
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            value[1] = 19
            initial_package_third.insert(Node(value))
            initial_address_third.insert(Node(address_id))

        # packages that can only be in the second truck (special note or delay)
        elif 'Can only be' in value[8]:
            initial_package_second.insert(Node(value))
            initial_address_second.insert(Node(address_id))
        elif 'Delayed' in value[8]:
            initial_package_second.insert(Node(value))
            initial_address_second.insert(Node(address_id))

        # Packages that are due before EOD and must be in the first truck. This includes
        # the lump of packages that must be delivered together
        elif value[6] != 'EOD' and ('Must' in value[8] or 'None' in value[8]):
            initial_package_first.insert(Node(value))
            initial_address_first.insert(Node(address_id))

        # packages in the same zip code as a mandatory delivery for the third truck
        elif '84104' in value[5] and '10:30' not in value[6]:
            initial_package_third.insert(Node(value))
            initial_address_third.insert(Node(address_id))

        # Add to the lesser of the second and third truck
        else:
            if get_size(initial_package_second.root) > get_size(initial_package_third.root):
                initial_package_third.insert(Node(value))
                initial_address_third.insert(Node(address_id))
            else:
                initial_package_second.insert(Node(value))
                initial_address_second.insert(Node(address_id))
        # Add package to our hash table
        Hash_Map.insert(key, value)

    def get_first_packages():
        return initial_package_first


    def get_second_packages():
        return initial_package_second


    def get_third_packages():
        return initial_package_third


    def get_first_addresses():
        return initial_address_first


    def get_second_addresses():
        return initial_address_second


    def get_third_addresses():
        return initial_address_third


    def get_hash_map():
        return Hash_Map
