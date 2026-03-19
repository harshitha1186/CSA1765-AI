# Vacuum Cleaner Problem
# Two rooms: A and B

def vacuum_cleaner():
    # Initial environment (can change as needed)
    environment = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    # Initial position of vacuum
    position = 'A'

    print("Initial State:")
    print("Room A:", environment['A'])
    print("Room B:", environment['B'])
    print("Vacuum is in Room", position)
    print("----------------------------")

    # Run until both rooms are clean
    while environment['A'] == 'Dirty' or environment['B'] == 'Dirty':
        
        if environment[position] == 'Dirty':
            print("Room", position, "is Dirty. Cleaning...")
            environment[position] = 'Clean'
        else:
            print("Room", position, "is already Clean.")
            
            # Move to other room
            if position == 'A':
                position = 'B'
            else:
                position = 'A'
            
            print("Moving to Room", position)
        
        print("Current State:")
        print("Room A:", environment['A'])
        print("Room B:", environment['B'])
        print("Vacuum is in Room", position)
        print("----------------------------")

    print("Both rooms are clean. Task completed!")


# Run the program
vacuum_cleaner()
