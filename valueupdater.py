from urllib.request import urlopen
import json, os, sys

# Loads the current directory the script will be running in, adds a seperator depending on the operating system
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
if not BASE_DIR.endswith(os.path.sep):
    BASE_DIR += os.path.sep

# Loads all item's and value's into a dictionary
data = json.loads(urlopen("https://www.rolimons.com/itemapi/itemdetails").read().decode())

# Check for missing file exception
try:
    # Opens both the values and creates a new value file to update into
    with open(BASE_DIR + 'values', 'r') as reader, open(BASE_DIR + 'new_values', 'w') as writer:
        
        # Converts the values file into a list
        values_file = reader.readlines()
        
        # Create new list that will hold the updated values
        updated_values = ["old\n","\n"]
        
        # Loop through the old values list
        for line in values_file:
            
            # If the first letter is a digit, convert string into a list
            if line[0].isdigit():
                old_item = line.split(':')
                
                # Check if the item is in rolimons item data, then retrieve the updated value
                if old_item[0] in data['items']:
                    new_item_value = data['items'][old_item[0]][3]
                                                                
                    # Check if item has value (with -1), and if the value has been updated
                    # Then displays the item with it's old and new value while updating it
                    if new_item_value != -1 and new_item_value != int(old_item[1]):
                        print("Item {} with value of {} will be updated to {}".format(data['items'][old_item[0]][0], old_item[1], new_item_value))
                        old_item[1] = str(new_item_value)
                        
                # Add the updated item and value into the updated values list
                updated_values.append(':'.join(old_item))
        
        # Write all the updated values into the new_values text document
        writer.writelines(i for i in updated_values)
    
    # Remove the old values and rename the new values to values
    print("Replacing old values with new values...")
    os.remove(BASE_DIR + 'values')
    os.rename(BASE_DIR + 'new_values', BASE_DIR + 'values')
    print("Values changed!")
except:
    print("Error has occured, no values file found")
