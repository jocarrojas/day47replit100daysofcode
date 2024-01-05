# Top Trumps
import random, sys, os, time

print('''
🌟Top Trumps🌟

Welcome to the Top Trumps 'Most Smart Human Critics' Simulator
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
contendingCharacters={}
characterCount=int(3)

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

# def prettyPrintContenders():
#   for key, value in characterDict.items():
#     if key==userCharacter or key==user2Character:
    
# Character selection and creation
prettyPrint()
create=input('Do you want to create a new character?\n\n').lower()

# Character creation
if create=='y' or create=='yes':
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
print()
while True:
  x=1
  for key,value in characterDict.items():
    print(f'{x}. {key}')
    x+=1
  break
print()

# Character selection
userCharacter=str()
while True:
  try:
    numInput=input()
    userCharacterNum=int(numInput)
    break
  except ValueError:
    print('Not a number')
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

# Statistic selection
print('Choose a statistic to fight:')
print()
while True:
  x=1
  for key,value in characterDict.items():
    if key==userCharacter:
      for subkey,subvalue in value.items():
        if not subkey=='id':
          print(f'{x}. {subkey}')
          x+=1
        else:
          continue
      # print(f'{value[subkey][subvalue]}')
    else:
      continue
  break
print()
statistic=input()
while True
      
characterCount=int(characterCount)
# print(characterCount)

# Game mode selector
print()
gameMode=input("Press '1' to play against the machine\nPress '2' to play against another human player...\n\n").lower()
if gameMode=='1':
  user2CharacterNum=random.randint(1, characterCount)
  while True:
    y=1
    for key,value in characterDict.items():
      if user2CharacterNum==y:
        user2Character=key
        break
      else:
        y+=1
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

  # Fight
print()
print("Let the fight begin!")
print()
print(f"{userCharacter} Vs. {user2Character}")
for key,value in character.items():
  if key==userCharacter:
    contendingCharacters[key]=value
  else:
    continue
print(contendingCharacters)

