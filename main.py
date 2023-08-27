# Top Trumps
import random, sys, os, time

print('''
🌟Top Trumps🌟

Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator
''')

characterDict={'Foucault':{'Intelligence':10,'Handsomeness':12,'Baldness':100000000,'L33t':0},
               'Marx':{'Intelligence':5000,'Handsomeness':100,'Baldness':500,'L33t':2},
               'Goldman':{'Intelligence':80000,'Handsomeness':680000,'Baldness':0,'L33t':1}}
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
if create=='y' or create=='yes':
  x=0
  while True: 
    # Character creation
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
    character[name]={'Intelligence':intelligence,'Handsomeness':handsomeness,'Baldness':baldness,'L33t':l33t}
    characterDict[name]={f'{name}':character}
    x+=1
    
    # prettyPrint
    prettyPrint()
    print()
    # prettyPrintAll()
    
    # Repeat?
    repeat=input("Do you want to add another character?\n\n").lower()
    if repeat=='y' or repeat=="yes":
      continue
    else:
      break
else:
  print('Input the number of the character you want to use:')  
  while True:
    x=1
    for key,value in characterDict.items():
      print(f'{x}. {key}')
      x+=1
    break
  userCharacter=input()
  availableCharacters=len(characterDict)
  print(availableCharacters)
  if userCharacter>availableCharacters
    print(f'No character has the number you selected. Choose a number equal or minor than {availableCharacter}')
  elif userCharacter<1:
    print(f"Ups! That's not a character number. Choose a number between 1 and {availableCharacter}")
  else:
    userCharacter=characterDict[userCharacter-1]
    print(f"Player 1 selected {userCharacter}\n\n")
    gameMode=input("Press '1' to play against the machine or any other key to play against a human player...\n\n").lower()
  if gameMode==1:
    machineCharacter=random.choice(characterDict)
  else:
    user2Character=input("Player 2: Input the number of the character you want to use (press 'r' to choose one randomly)"):\n\n')
    if user2
    
