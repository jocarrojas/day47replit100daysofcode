# Top Trumps
import random, sys, os, time

print('''
🌟Top Trumps🌟

Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator
''')

characterDict={
  'Foucault':
  {
    'id':1,
    'Intelligence':10,
    'Handsomeness':12,
    'Baldness':100000000,
    'L33t':0
  },
   'Marx':    
  {
    'id':2,
    'Intelligence':5000,
    'Handsomeness':100,
    'Baldness':500,
    'L33t':2
  },
  'Goldman':
  {
    'id':3,
    'Intelligence':80000,
    'Handsomeness':680000,
    'Baldness':0,
    'L33t':1
  }
}

character={}

def prettyPrint():
  print()
  print('These are the characters available:')
  print()
  for key, value in characterDict.items():
    print(key, end=':\n')
    for subKey, subValue in value.items():
      print(f'| {subKey}: {subValue}')
    print()

def prettyPrintAll():
  for key, value in characterDict.items():
    print(key, end='\n ')
    for subKey, subValue in value.items():
      print(f'{subKey}')
  print()

# Character selection and creation
prettyPrint()
create=input('Do you want to create a new character?\n\n').lower()

# Character creation
if create=='y' or create=='yes':
  characterCount=int(3)
  x=0
  while True: 
    print()
    print('Creating a new character 💀...')
    print()
    name=input('Name your character: ')
    print()
    print('Input scores for each category:')
    print()
    intelligence=input('Intelligence score: ')
    handsomeness=input('Handsomeness score: ')
    baldness=input('Baldness level: ')
    l33t=input('L33t coding skills: ')
    characterCount+=1
    character[name]={'id':characterCount,'Intelligence':intelligence,'Handsomeness':handsomeness,'Baldness':baldness,'L33t':l33t}
    print()
    characterDict[name]=character[name]
    x+=1
    print()
    prettyPrint()
    print()
    
    # Repeat?
    repeat=input("Do you want to add another character?\n\n").lower()
    if repeat=='y' or repeat=="yes":
      continue
    else:
      break
else:
  pass
  
print('\nInput the number of the character you want to use:')  
while True:
  x=1
  for key,value in characterDict.items():
    print(f'{x}. {key}')
    x+=1
  break
print()

# Character selection
userCharacter=str()
userCharacterNum=int(input())
int(userCharacterNum)
# availableCharacters=len(characterDict)
# int(availableCharacters)

if userCharacterNum>characterCount:
  print(f'No character has the number you selected. Choose a number equal or minor than {characterCount}')
elif userCharacterNum<1:
  print(f"Ups! That's not a character number. Choose a number between 1 and {characterCount}")
else:
  while True:
    y=1
    for key,value in characterDict.items():
      if userCharacterNum==y:
        userCharacter=key
        break
      else:
        y+=1
    break
  print()
  print(f"Player 1 selected {userCharacter}\n\n")
  
# Game mode selector
gameMode=input("Press '1' to play against the machine\n Or press '2' to play against another human player...\n\n").lower()
if gameMode=='1':
  machineCharacterNum=random.choice(characterCount)
  while True:
    y=1
    for key,value in characterDict.items():
      if machineCharacterNum==y:
        machineCharacter=key
        break
      else:
        y+=1
    break
  break
elif gameMode=='2':
  print()
  while True:
    x=1
    for key,value in characterDict.items():
      print(f'{x}. {key}')
      x+=1
    break
  print()
  while True:
    user2CharacterNum=input("Player 2: Input the number of the character you want to use (or press 'r' to choose one randomly):\n\n")
    if user2CharacterNum=='r':
      print("Choosing random character...")
      user2CharacterNum=random.choice(characterCount)
      while True:
        y=1
        for key,value in characterDict.items():
          if user2CharacterNum==y:
            user2Character=key
            break
          else:
            y+=1
      print(f"Player 2: Your character is: {user2Character}")
      break
    elif user2CharacterNum>characterCount:
      print(f"No character has the number you selected. Choose a number equal or minor than {characterCount}")
      continue
    else:
      while True:
      y=1
      for key,value in characterDict.items():
        if user2CharacterNum==y:
          user2Character=key
          break
        else:
          y+=1
      break
      print(f"Player 2: Your character is: {user2Character}")
else:
  print("That's not an option, try again!")
  continue

  # Trump

