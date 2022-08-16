from multiprocessing.connection import wait
from telnetlib import AO
from turtle import left


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Ilha do Tesouro")
print("Sua missão é achar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
escolha1 = input('Qual\'direção você vai "left" ou "right".').lower()

if escolha1 == "left":
        escolha2 = input(' Voce \'chega proximo a um lago com bote no meio você nada  até o bote "swin" ou espera o bot se aproximar mais "wait"').lower()
else: 
        print('Caiu num buraco\nGame Over')
if escolha2 == "wait":
        escolha3 = input('Depois de atravessar o lago você ver 3  portas \'"Red","Yellow","Blue" qual você ira escolher ?').lower()
else:
        print("Atacado por piranhas.\nGame Over")
if escolha3 == "Red":
        print("Queimado pelo fogo\nGame Over")
elif escolha3 == "Blue":
        print("Comido pelas Bestas\nGame Over")
elif escolha3 == "Yellow":
        print("You Win 💰")
else:
        print("Game Over.")

