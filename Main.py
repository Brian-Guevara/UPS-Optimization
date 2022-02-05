# Brian Guevara
# StudentID: 001003681


# Main.py
# This is our main class. The program will be executed from this python file.
# The main methods in this class are printing a package's info, and the main input program.
# The main input program will take 2 values: one is a string for looking up a package or getting all packages
# at a specific time. The other field is the timestamp the user inputs.

# First, we must import our hash map w/ package info, finish times, and total distance
from InputDataCSV import get_hash_map
from Packages import total_distance, get_first_finish_time, get_second_finish_time, get_third_finish_time
import datetime


# This is a simple print method to use when we want to print the info for packages.
# Big-O: O(1)
def print_lines(cur_package):
    print('{: <5}'.format('ID:' + cur_package[0]),
          '|   Street address:', '{: <66}'.format(cur_package[2] + ' ' +
                                                  cur_package[3] + ', ' + cur_package[4] +
                                                  ' ' + cur_package[5]),
          '{: <18}'.format('| Weight: ' + cur_package[7] + ' kg'),
          '{: <37}'.format('|  Delivery Time: ' + cur_package[6]),
          '{: <28}'.format('|  Truck ' + cur_package[9]),
          '|  Package', cur_package[10])


# This is our main method. It calls the results from the processes of the other scripts. The main method exclusively
# uses the hash table entry as it is most convenient and data is already altered by our Binary Tree algorithms
# Big-O: O(N)
def main():
    # Prints the total number of miles it took for the route.
    print('The packages were successfully delivered in', "{0:.2f}".format(total_distance(), 2), 'miles.')

    # Ask the user if they want a timestamp of all packages, to check the status of one package, or to exit the program
    user_input = input("\nType 'package' to look for an individual package at a specific time.\n"
                       "Type 'time' to see the status of all packages at a specific time.\n"
                       "Type 'exit' to quit out.\n\n")

    # We will look through the hash map to print out packages and to grab their time of delivery
    # Big-O: O(N)
    # if user types 'time' then they are prompted for a time.
    if user_input.lower().__contains__('time'):
        try:
            # Grabs and parses the time value from the user
            timestamp_input = input('Please enter a time in the HH:MM:SS format: ')
            (h, m, s) = timestamp_input.split(':')
            timestamp_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # Print the times the trucks make it from their trips
            print('First truck arrived/will arrive at:', get_first_finish_time())
            print('Second truck arrived/will arrive at:', get_second_finish_time())
            print('Third truck arrived/will arrive at:', get_third_finish_time())

            # Look through the hash map. We will use a range of integers that the hash map will process to give
            # use the correct package
            for count in range(1, 41):
                package = get_hash_map().get(str(count))
                try:
                    # Get the times the package leave thee station and the time it is delivered

                    package_leaves_hub = package[9]
                    package_delivery_time = package[10]
                    # convert the time values
                    (h, m, s) = package_leaves_hub.split(':')
                    time_truck_leaves = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                    (h, m, s) = package_delivery_time.split(':')
                    time_of_delivery = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass
                # First, we check for packages that have a leave time that is equal to or less than the input time.
                if time_truck_leaves >= timestamp_time:
                    package[10] = 'still at station'
                    package[9] = 'leaves at ' + package_leaves_hub
                    print_lines(package)
                # Next, check if the leave time is less than the timestamp time. This tells us the package has left.
                elif time_truck_leaves <= timestamp_time:
                    # Check to see if input time is less than the calculated time of delivery
                    if timestamp_time < time_of_delivery:
                        package[10] = 'on way to destination'
                        package[9] = 'left at ' + package_leaves_hub
                        print_lines(package)
                    # For those that have a timestamp that is equal to or greater than the expected time of delivery,
                    # mark it as delivered
                    else:
                        package[10] = 'delivered at ' + package_delivery_time
                        package[9] = 'left at ' + package_leaves_hub
                        print_lines(package)
            exit()
            # Program ends after successful print
        except ValueError:
            print("Format is incorrect. Please try again. \n")


    # If 'package' is selected than the user is prompted for a package ID followed by a timestamp
    # Once that information is entered then the user will be shown a particular package at a given time
    # Steps and procedure are similar to the 'time' functions
    elif user_input.lower().__contains__('pack'):
        try:
            count = input('Please enter a package ID to lookup: ')

            package = get_hash_map().get(str(count))

            package_leaves_hub = package[9]
            package_delivery_time = package[10]

            timestamp_input = input('Please enter a time in the HH:MM:SS format: ')

            (h, m, s) = timestamp_input.split(':')
            timestamp_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            (h, m, s) = package_leaves_hub.split(':')
            time_truck_leaves = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            (h, m, s) = package_delivery_time.split(':')
            time_of_delivery = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            # First checks if the package has left the hub yet
            if time_truck_leaves >= timestamp_time:
                package[10] = 'still at station'
                package[9] = 'leaves at ' + package_leaves_hub
                print_lines(package)
            elif time_truck_leaves <= timestamp_time:
                # Then checks if the package has left the hub but has not been delivered yet
                if timestamp_time < time_of_delivery:
                    package[10] = 'on way to destination'
                    package[9] = 'left at ' + package_leaves_hub
                    print_lines(package)
                # If the package has already been delivered than it displays the time
                else:
                    package[10] = 'delivered at ' + package_delivery_time
                    package[9] = 'left at ' + package_leaves_hub
                    print_lines(package)
            exit()

        # Error that can be thrown when the time format is incorrect
        except ValueError:
            print("Format is incorrect. Please try again. \n")
        # Error that can be thrown when putting in a value outside the range of the hash map
        except TypeError:
            print("Enter a package ID within the range. Please try again. \n")
    elif user_input.lower().__contains__('exit'):
        exit()
    else:
        print('Invalid entry! Closing program.')
        exit()


if __name__ == '__main__':
    main()
