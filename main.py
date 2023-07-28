# Top Trumps
print('''
🌟Top Trumps🌟

Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator
''')

character={}

def charachterCreator():
  print('Creating a new character💀...')
  print()
  name=input('Name your charachter: ')
  print('Input scores for each category:')
  print()
  intelligence=input('Intelligence score: ')
  handsomeness=input('Handsomeness score: ')
  baldness=input('Baldness level: ')
  l33t=input('L33t coding skills: ')
  charachter[name]={'intelligence':intelligence,'handsomeness':handsomeness,'baldness':baldness,'l33t':l33t}
  
print('Available charachters:')