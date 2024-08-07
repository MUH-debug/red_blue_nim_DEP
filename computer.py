import math

num_stones = [3, 5]
player = 2  # Assuming computer is player 2

def minimax(num_stones, depth, alpha, beta, is_maximizing):
    if num_stones[0] == 0 and num_stones[1] == 0:
        return 1 if is_maximizing else -1

    if depth == 0:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(2):
            if num_stones[i] > 0:
                for take in range(1, min(3, num_stones[i]) + 1):
                    new_stones = num_stones[:]
                    new_stones[i] -= take
                    eval = minimax(new_stones, depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            if num_stones[i] > 0:
                for take in range(1, min(3, num_stones[i]) + 1):
                    new_stones = num_stones[:]
                    new_stones[i] -= take
                    eval = minimax(new_stones, depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(num_stones, depth):
    best_move = None
    best_value = -math.inf
    for i in range(2):
        if num_stones[i] > 0:
            for take in range(1, min(3, num_stones[i]) + 1):
                new_stones = num_stones[:]
                new_stones[i] -= take
                move_value = minimax(new_stones, depth - 1, -math.inf, math.inf, False)
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, take)
    return best_move

def start_game(mode):
    global num_stones, player
    while True:
        if player % 2 == 1:
            # Player's turn
            print("PLAYER TURN")
            print("THE NUMBER OF STONES ARE:")
            print(f"1. RED : {num_stones[0]}")
            print(f"2. BLUE : {num_stones[1]}")

            st = int(input("WHICH STACK DO YOU WANT TO REMOVE STONES FROM? 1_RED 2_BLUE: ")) - 1

            while st not in [0, 1] or num_stones[st] == 0:
                if st not in [0, 1]:
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
        else:
            # Computer's turn
            print("COMPUTER TURN")
            move = best_move(num_stones, 3)
            if move:
                st, rem = move
                # Ensure the computer follows the same constraint
                if rem > min(3, num_stones[st]):
                    rem = min(3, num_stones[st])
                num_stones[st] -= rem
                print(f"Computer removes {rem} stone(s) from stack {st + 1}")

        if num_stones[0] == 0 and num_stones[1] == 0:
            print("Game has ended!")
            if mode == 1:
                if player % 2 == 1:
                    print("PLAYER WINS!")
                else:
                    print("COMPUTER WINS!")
            else:
                if player % 2 == 1:
                    print("COMPUTER WINS!")
                else:
                    print("PLAYER WINS!")
            break

        player = 3 - player  # Alternate between 1 and 2
