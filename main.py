contraseña = ['estudiante']

correcta = input('deseas adivinar la contraseña (s/n) ')

while correcta == 's':
  adiv_contraseña = (input('introducir la contraseña correcta :'))
  if adiv_contraseña == contraseña[0]:
    print('contraseña correcta')
  else:
    print('contraseña incorrecta')
  correcta = input('deseas seguir jugando para adivinar la contraseña (s/n) ')
  print('gracias por participar en este juego ')


