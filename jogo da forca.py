import random

palavras = ['leão', 'sapo', 'tartaruga', 'maça', 'melancia', 'laranja', 'mesa', 'fone', 'caderno']

palavra = random.choice(palavras)
palavra_oculta = []

for i in range(len(palavra)):
   palavra_oculta.append('*')
vida = 10
while True:
  if vida == 10:
    print('   ____')
    print('   |      |')
    print('          |')
    print('          |')
    print('          |')
    print('          |')
  elif vida == 9:
    print('   ___')
    print('   |       |')
    print('  (  )     |')
    print('           |')
    print('           |')
    print('           |')
  elif vida == 8:
    print('   ___')
    print('   |       |')
    print(' (°  )     |')
    print('           |')
    print('           |')
    print('           |')
  elif vida == 8:
    print('   ___')
    print('   |       |')
    print(' (° °)     |')
    print('           |')
    print('           |')
    print('           |')
  elif vida == 6:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('           |')
    print('           |')
    print('           |')
  elif vida == 5:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('   |       |')
    print('           |')
    print('           |')
  elif vida == 4:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('  /|       |')
    print('           |')
    print('           |')
  elif vida == 3:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('  /|\      |')
    print('           |')
    print('           |')
  elif vida == 2:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('  /|\      |')
    print('   |       |')
    print('           |')
  elif vida == 1:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('  /|\      |')
    print('   |       |')
    print('  /        |')
  elif vida == 0:
    print('   ___')
    print('   |       |')
    print(' (°_°)     |')
    print('  /|\      |')
    print('   |       |')
    print('  / \      |')
    break
  print('palavra secreta:', palavra_oculta)
  letra = input('digite uma letra\n\n:')

  if letra not in palavra:
    vida = vida -1
  else:
    if letra in palavra and letra in palavra_oculta:
      vida = vida -1
    else:
      for i in range(len(palavra)):
        if letra == palavra[i]:
          palavra_oculta[i] = palavra[i]

  if vida == 0:
    print('você perdeu')
  if '*' not in palavra_oculta:
    print ('PARABÉNS VOCÊ VENCEU!!!')
    print (f'palavra {palavra} descoberta')