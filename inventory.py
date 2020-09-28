stuff = {'arrow': 12,
         'gold coin': 42,
         'rope': 1,
         'torch': 6,
         'dagger': 1}

def displayInventory(inventory):
    print('Inventory: ')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

# displayInventory(stuff)
          
def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory:
            inventory.setdefault(k, 1)
        else:
            inventory[k] += 1
    return inventory

loot = {'gold coin': 42, 'rope': 1, 'pearl': 5}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gold coin']


loot = addToInventory(loot, dragonLoot)
displayInventory(loot)
    
       
        
          
