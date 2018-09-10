import os
import csv

path= "/home/patryk/Dokumenty/repositorybp/progbasics-python-game-inventory-PatrykMandrak"
os.chdir(path)

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}
# Displays the inventory.
def display_inventory(inventory):
    #inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}
    print("Inventory:")
    for key, value in inv.items():
            print (value, key)
    print("")
    print ("Number of items is: ", sum(inv.values()))
    #print (sum(inv.values())),


def add_to_inventory(inventory, added_items):
    for item in added_items:
        item_count=inventory.get(item, 0)
        inventory[item]=item_count + 1
    return inventory

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#add_to_inventory(inv, dragon_loot)
inv = add_to_inventory(inv, dragon_loot)
#display_inventory(inv)

x=max(inv, key=lambda x: len(x.split()))
y=len(x)

n = "-"
q = n * (y+10)

def print_table(inventory, order=None):
    count_and_item_name= {"item name": "count"}
    longest_key=max(inventory, key=len)
    max_width=len(longest_key)
    max_width_second=max_width + 4
    print("Inventory:")
    print("")
    for key, value in count_and_item_name.items():
        print ("%6s %*s" % (value,max_width_second, key))

    print (q.rjust(20, " "))

    if order==None:
        for key, value in inventory.items():
            print ("%6d %*s" % (value,max_width_second, key))

    if order=="count,asc":
        for key, value in sorted(inventory.items(), key=lambda kv: (kv[1],kv[0])):
            print ("%6d %*s" % (value,max_width_second, key))

    if order=="count,desc":
        for key, value in sorted(inventory.items(), key=lambda kv: (kv[1],kv[0]), reverse=True):
            print ("%6d %*s" % (value,max_width_second, key))

    print (q.rjust(20, " "))
    #print("")
    print ("Number of items is: ", sum(inv.values()))
print_table(inv)



def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as file:
        added_items=file.read()
    added_items=added_items.split(',')
    updated_inventory=inventory
    for item in added_items:
        if item in updated_inventory:
            updated_inventory[item]+=1
        else:
            updated_inventory[item]=1
    return updated_inventory



#print_table(inv)
