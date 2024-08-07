print("WELCOME TO NIM GAME --->>> \n")
print('''THE GAME HAS TWO VERSIONS   
     1. STANDARD VERSION: PLAYER TO PICK LAST STONE WINS
     2. MISERE VERSION: PLAYER WHO PICKS LAST STONE LOSES
RULES:
      YOU CAN PICK STONES FROM ONE STONE PILE AT A TIME 
      RED STONE PILE HAS 3 STONES
      BLUE STONE PILE HAS 5 STONES
      EACH RED STONE GIVES 2 POINTS
      EACH BLUE STONE GIVES 3 POINTS 
      YOU CAN REMOVE MAXIMUM OF 3 STONES AT A TIME
      ''')

print("PRESS ENTER TO CONTINUE!!!")
input(" ")

print("SELECT YOUR OPPONENT: ")
print("1. COMPUTER")
print("2. ANOTHER PLAYER")

opp = int(input())

while opp not in [1, 2]:
    print("PLEASE ENTER VALID OPTION")
    opp = int(input())

print("CHOOSE GAME MODE")
print("1. STANDARD MODE")
print("2. MISERE MODE")
mode = int(input())

while mode not in [1, 2]:
    print("PLEASE ENTER VALID OPTION")
    mode = int(input())

if opp == 1:
    import computer
    computer.start_game(mode)
elif opp == 2:
    import human 
