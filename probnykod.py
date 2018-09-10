import os
import csv
import sys
sys.version
sys.version_info
#from collections import defaultdict
#from contextlib import suppress
path= "/home/patryk/Dokumenty/repositorybp/progbasics-python-game-inventory-PatrykMandrak"
os.chdir(path)

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}

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
    for key, value in count_and_item_name.iteritems():
        print "%6s %*s" % (value,max_width_second, key)

    print q.rjust(20, " ")

    if order==None:
        for key, value in inventory.iteritems():
            print "%6d %*s" % (value,max_width_second, key)

    if order=="count,asc":
        for key, value in sorted(inventory.iteritems(), key=lambda (k, v): (v, k)):
            print "%6d %*s" % (value,max_width_second, key)

    if order=="count,desc":
        for key, value in sorted(inventory.iteritems(), key=lambda (k, v): (v, k), reverse=True):
            print "%6d %*s" % (value,max_width_second, key)

    print q.rjust(20, " ")
    #print("")
    print "Number of items is: ",
    print (sum(inv.values())),


def import_inventory(inventory, filename="import_inventory.csv"):
    file = open(filename, 'r')
    data = file.readline().split(',')
    for item in data:
        item = item.strip()
        if item in inv:
            inventory.update({item: inventory[item]+1})
        else:
            inventory.update({item: 1})
    return inventory

#import_inventory(inv)
print_table(inv)
