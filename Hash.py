# Brian Guevara
# StudentID: 001003681

# Hash.py
# This file is a generic hash table. After creating the package object (in InputDataCSV) and putting it
# into the right queue, it is added into this basic hash table.

# Methods in the map class are to return instances, insert, update, or delete instances as well.
class Map:
    # Space-time complexity: O(N)
    def __init__(self, capacity=10):
        self.map = []
        for i in range(capacity):
            self.map.append([])

    # Returns the hash number (not the actual object)
    # Big-O: O(1)
    def getHash(self, key):
        return int(key) % len(self.map)

    # Inserts an object in the hash table.
    # Big-O: O(N)
    def insert(self, key, value):
        # Make our hash key
        key_hash = self.getHash(key)
        # Create hash object = key + package object
        key_value = [key, value]

        # If the hash spot is empty
        if self.map[key_hash] is None:
            # Make a new list object
            self.map[key_hash] = list([key_value])
            return True
        # Else, check for each value in the map
        # if the package is the equivalent to an existing, then replace with new data
        else:
            for val in self.map[key_hash]:
                if val[0] == key:
                    val[1] = key_value
                    return True
            # Otherwise, add the package object to this hash spot
            self.map[key_hash].append(key_value)
            return True

    # Updates an object in the hash table
    # Big-O: O(N)
    def update(self, key, value):
        key_hash = self.getHash(key)
        if self.map[key_hash] is not None:
            for val in self.map[key_hash]:
                if val[0] == key:
                    val[1] = value
                    return True

        else:
            print("Key could not be found.")

    # Returns the object in the hash
    # Big-O: O(N)
    def get(self, key):
        # get hash key of package id
        key_hash = self.getHash(key)
        # if area has data, then check for
        # each value for one we are looking for
        if self.map[key_hash] is not None:
            for val in self.map[key_hash]:
                if val[0] == key:
                    # Val[0] is the hash-key (package ID). Val [1] is the package object (list object)
                    return val[1]
        return None

    # Deletes an object in the hash table
    # Big-O: O(N)
    def delete(self, key):
        key_hash = self.getHash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
