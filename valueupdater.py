from urllib.request import urlopen
import json, os, sys

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
data = json.loads(urlopen("https://www.rolimons.com/itemapi/itemdetails").read().decode())

try:
    with open(BASE_DIR + '\\values', 'r') as reader, open(BASE_DIR + '\\new_values', 'w') as writer:
        values_file = reader.readlines()
        updated_values = ["old\n","\n"]
        for line in values_file:
            if line[0].isdigit():
                old_item = line.split(':')
                if old_item[0] in data['items']:
                    new_item_value = data['items'][old_item[0]][3]
                    if new_item_value != -1 and new_item_value != int(old_item[1]):
                        print(f"Item {data['items'][old_item[0]][0]} with value of {old_item[1]} will be updated to {new_item_value}")
                        old_item[1] = str(new_item_value)
                updated_values.append(':'.join(old_item))
        writer.writelines(i for i in updated_values)

    print("Replacing old values with new values...")
    os.remove(BASE_DIR + '\\values')
    os.rename(BASE_DIR + '\\new_values', BASE_DIR + '\\values')
    print("Values changed!")
except:
    print("Error has occured, no values file found")