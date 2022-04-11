#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Living Room' : { #from bedroom
                  'south' : 'Kitchen',
                  'north' : 'Balconey',

                  'east'  : 'BedRoom', #W living
                  'item'  : 'Room key'
                },

            'Kitchen' : {
                  'north' : '"Living Room', #living
                  'item'  : 'ghost',
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'north' : 'Living Room',
                  
               },
            'Balcony' : {
                  'southwest' : 'Living Room',
                  'Southeast' : 'BedRoom'

               },
             'BedRoom' : {
                  'west' : 'Living Room',
                  'south' : 'Bathroom',
                  'item'  : 'Holy Book'

               },    
               
            'Bathroom' : {
                  'north' : 'BedRoom',
                  'item' : 'Ghost',
            }
         }

#start the player in the Living Room
currentRoom = 'Living Room'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('Nothing that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Dining Room' and 'Room Key' in inventory and 'Holy Book' in inventory:
    print('The room door opens!\nYou escaped room 1217. one less soul claimed by room.')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'ghost' in rooms[currentRoom]['item']:
    print('You Feel the room get bone chilling cold, \nas you look up, \ncold dead hands pull you into the floor ... \nGAME OVER!')
    break



