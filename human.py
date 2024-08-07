total_score = 21
players_score = 0
player = 1
num_stones = [3, 5]
stones = [0, 1]

print("CHOOSE GAME MODE")
print("1. STANDARD MODE")
print("2. MISERE MODE")
mode = int(input())

while mode not in [1, 2]:
    print("PLEASE ENTER VALID OPTION")
    mode = int(input())

while True:
    if player % 2 == 0:
        print("PLAYER 1 TURN")
    else:
        print("PLAYER 2 TURN")

    print("THE NUMBER OF STONES ARE:")
    print(f"1. RED : {num_stones[0]}")
    print(f"2. BLUE : {num_stones[1]}")

    st = int(input("WHICH STACK DO YOU WANT TO REMOVE STONES FROM? 1_RED 2_BLUE: ")) - 1

    while st not in stones or num_stones[st] == 0:
        if st not in stones:
            print("INVALID MOVE! PLEASE ENTER AGAIN.")
        else:
            print("STACK IS EMPTY! PLEASE CHOOSE ANOTHER STACK.")
        st = int(input("WHICH STACK DO YOU WANT TO REMOVE STONES FROM? 1_RED 2_BLUE: ")) - 1

    print(f"How many stones to remove? Current in stack {num_stones[st]}")
    rem = int(input())

    while rem < 1 or rem > min(3, num_stones[st]):
        print("INVALID NUMBER OF STONES! PLEASE ENTER AGAIN.")
        print(f"How many stones to remove? Current in stack {num_stones[st]}")
        rem = int(input())

    num_stones[st] -= rem

    if num_stones[0] == 0 and num_stones[1] == 0:
        print("Game has ended!")
        if mode == 1:
            if player % 2 == 0:
                print("PLAYER 1 WINS!")
            else:
                print("PLAYER 2 WINS!")
        else:
            if player % 2 == 0:
                print("PLAYER 2 WINS!")
            else:
                print("PLAYER 1 WINS!")
        break

    player += 1
