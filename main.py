# Top Trumps
import random, sys, os, time

user1Character=str()
user2Character=str()
gameMode=int()
statistic=int(0)
menuChoice=str()
contendingCharacters={}
character={}
statsCount=4
characterCount=int(3)
fights=0
executed=0
player1=0
player2=0
t='test'

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

def statStore(user1, user2, stat, userCharacter1, userCharacter2):
    # Find and store stat
    global contendingCharacters
    global statistic
    global user1Character
    global user2Character
    y=1
    print()
    while True:
        for key, value in characterDict.items():
            if userCharacter1==key:
                for subkey,subvalue in value.items():
                    if statistic==1:
                        statistic+=1
                        y+=1
                        continue
                    else:
                        contendingCharacters[user1]=userCharacter1, subvalue
                        print(f'You have chosen {subkey} to fight')
                        break
            else:
                y+=1
                continue
        break
    x=1
    while True:
        for key, value in characterDict.items():
            if userCharacter2==key:
                for subkey,subvalue in value.items():
                    if x==1:
                        x+=1
                        continue
                    else:
                        contendingCharacters[user2]=userCharacter2, subvalue
                        return contendingCharacters
                        break
            else:
                x+=1
                continue
            break

def gameMode():
    global gameModeSelected
    print()
    gameModeSelected=input("Press '1' to play against the machine...\nPress '2' to play against another human player...\n\n> ").lower()
    return gameModeSelected

def characterCreator():
  global characterCount
  create=input('Do you want to create a new character?\n\n> ').lower()
  if create=='y' or create=='yes':
    x=0
    while True: 
      print()
      print('Creating a new character 💀...')
      print()
      name=input('Name your character:\n\n> ')
      print()
      print('Input scores for each category:')
      print()
      intelligence=input('Intelligence:\n\n> ')
      print()
      handsomeness=input('Handsomeness:\n\n>  ')
      print()
      baldness=input('Baldness level:\n\n>  ')
      print()
      l33t=input('L33t coding skills:\n\n>  ')
      print()
      characterCount+=1
      character[name]={'id':characterCount,'Intelligence':intelligence,'Handsomeness':handsomeness,'Baldness':baldness,'L33t':l33t}
      print()
      characterDict[name]=character[name]
      x+=1
      print()
      prettyPrint()
      print()

      # Repeat?
      repeat=input("Do you want to add another character?\n\n> ").lower()
      if repeat=='y' or repeat=="yes":
        continue
      else:
        break
  else:
    pass

def user1CharacterSel():
    print('\nInput the number of the character you want to use: ')
    print()
    global user1Character
    global contendingCharacters
    while True:
        x=1
        for key,value in characterDict.items():
            print(f'{x}. {key}')
            x+=1
        print()
        numInput=input('> ')
        user1CharacterNum=int(numInput)
        if user1CharacterNum>characterCount or user1CharacterNum<1:
            print(f'Error! Choose a number equal or minor than {characterCount}')
            continue
        else:
            for key,value in characterDict.items():
                for subkey,subvalue in value.items():
                    if subkey=='id':
                        if user1CharacterNum==subvalue:
                            user1Character=key
                            break
                        else:
                            pass
                    else:
                        pass
            print()
            os.system('clear')
            print(f"Player 1 selected {user1Character}\n\n")
            return user1Character
        break



def scoreReset():
    player1=0
    player2=0

def scorePrint():
    print("Score:")
    print()
    print(f"     Player 1: {player1}")
    print(f"     Player 2: {player2}")
    print()

def statInput():
    global statsCount
    global statistic
    print('Choose a statistic to fight: (Press the number only)')
    while True:
        print(f'1. Intelligence\n2. Handsomeness\n3. Baldness\n4. L33t\n\n')
        statistic=int(input())
        if statistic>0 and statistic<=statsCount:
            return statistic
            break
        else:
            print()
            print(f'Pick a number between 1 and {statsCount}')
            print()
            continue       

def user2CharacterSel():
  # Player 2 character selection
  global gameModeSelected
  global user2Character
  global contendingCharacters
  if gameModeSelected=='1':
    user2CharacterNum=random.randint(1, characterCount)
    y=1
    while True:
      for key,value in characterDict.items():
        if user2CharacterNum==y:
          user2Character=key
          return user2Character
          break
        else:
          y+=1
      break
  elif gameModeSelected=='2':
    print()
    while True:
      x=1
      for key,value in characterDict.items():
        print(f'{x}. {key}')
        x+=1
      break
    print()
    while True:
        user2CharacterNum=input("Player 2: Input the number of the character you want to use (or press 'r' to choose one randomly):\n\n> ")
        if user2CharacterNum=='r':
            print("Choosing random character...")
            user2CharacterNum=random.choice(characterCount)
            while True:
              y=1
              for key,value in characterDict.items():
                if user2CharacterNum==y:
                  user2Character=key
                  return user2Character
                  break
                else:
                  y+=1
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
                        return user2Character
                        break
                    else:
                        y+=1
                break
    print(f"Player 2: Your character is: {user2Character}")
    return user2Character
  else:
    print("That's not an option, try again!")

def fight():
    global contendingCharacters
    global user1Character
    global user2Character
    global player1
    global player2
    print()
    for key,value in contendingCharacters.items():
      #  for subkey,subvalue in value.items():
        print(f'{key}: {value[0]} has {value[1]} of this statistic.')
    print()
    print("Let the fight begin!")
    print()
    print(f"{user1Character} Vs. {user2Character}")
    print()
    if contendingCharacters['Player 1'][1]==contendingCharacters['Player 2'][1]:
        print("It's a tie!")
    elif contendingCharacters['Player 1'][1]>contendingCharacters['Player 2'][1]:
        print(f"{user1Character} wins!")
        player1+=1
    elif contendingCharacters['Player 1'][1]<contendingCharacters['Player 2'][1]:
        print(f"{user2Character} wins!")
        player2+=1
    else:
        print("Something went wrong!")

def menu():
    global menuChoice
    print('''Press:\n\n
    - 'n' for another fight.\n
    - 'c' to see and create characters.\n
    - 'm' to start again.\n
    - 'q' to quit the game.\n\n
    ''')
    menuChoice=input('> ').lower()
    return(menuChoice)

# Execution
while True:
    if executed==0:
        # First run
        print('''
        🌟Top Trumps🌟\n\n   
        Welcome to the Top Trumps 'Best Human Critics' Simulator\n\n
        ''')
        gameMode()
        os.system('clear')
        prettyPrint()
        characterCreator()
        os.system('clear')
        user1CharacterSel()
        statInput()
        user2CharacterSel()
        statStore('Player 1', 'Player 2', statistic, user1Character, user2Character)
        os.system('clear')
        fight()
        time.sleep(3)
        executed+=1
        os.system('clear')
        continue
    else:
        while True:
            executed+=1
            print('''
            🌟Top Trumps🌟
            ''')
            scorePrint()
            menu()
            if menuChoice=='m':
                os.system('clear')
                print()
                print('Start again:')
                print()
                scoreReset()
                scorePrint()
                gameMode()
                os.system('clear')
                prettyPrint()
                characterCreator()
                os.system('clear')
                user1CharacterSel()
                statInput()
                user2CharacterSel()
                statStore('Player 1', 'Player 2', statistic, user1Character, user2Character)
                os.system('clear')
                fight()
                time.sleep(3)
                os.system('clear')
                continue
            elif menuChoice=='c':
                os.system('clear')
                print()
                print('Create character')
                print()
                prettyPrint()
                characterCreator()
                os.system('clear')
                user1CharacterSel()
                statInput()
                user2CharacterSel()
                statStore('Player 1', 'Player 2', statistic, user1Character, user2Character)
                os.system('clear')
                fight()
                time.sleep(3)
                os.system('clear')
                continue
            elif menuChoice=='n':
                os.system('clear')
                print()
                print('Another fight...')
                print()
                scorePrint()
                user1CharacterSel()
                statInput()
                user2CharacterSel()
                statStore('Player 1', 'Player 2', statistic, user1Character, user2Character)
                os.system('clear')
                fight()
                time.sleep(3)
                os.system('clear')
                continue
            elif menuChoice=='q':
                os.system('clear')
                print()
                confirmQuit=input("Press 'q' again to close the game.\n\nPress any other letter to return to the game')").lower()
                print()
                print("> ")
                print()
                if confirmQuit=='q':                    
                    print('Game finished!')
                    time.sleep(1)
                    exit()
                else:
                    continue
            else:
                print("That's not an option. Try again!")
                continue