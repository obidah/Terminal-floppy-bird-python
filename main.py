import keyboard
import os
import time
import random

# getting what charachter will the player choose to jump
def get_jump_button():
    print("Please press your jumping button on your keyboard")
    while True:
        if keyboard.read_key():
            BUTTON = keyboard.read_key()
            break
    return BUTTON

def game(BUTTON):
    SCORE = 0
    INCREASE = 0
    BIRD = "##"
    BOARD_SIZE = {"WIDTH":70,"HEIGHT":20}
    COLUMNS,LINES = os.get_terminal_size()
    BIRD_X = 70 // 4
    BIRD_Y = 20 // 2
    WALL = True
    while True:
        print(f"Score: {SCORE-1}")
        if WALL:
            RANDOM_HOLE = random.randrange(7,11)
            FIRST = random.randrange(19-RANDOM_HOLE)
            LAST = list(range(FIRST+RANDOM_HOLE,19))
            WALL_SPACES = BOARD_SIZE.get("WIDTH")-10
            WALL = False
            SCORE += 1
        time.sleep(0.05)
        os.system("cls")
        for i in range(BOARD_SIZE.get("HEIGHT")):
            for j in range(BOARD_SIZE.get("WIDTH")):
                if i == BIRD_Y and j == BIRD_X:
                    print(BIRD,end="")
                if (i in list(range(FIRST)) + LAST and j == WALL_SPACES-2) and i == BIRD_Y:
                    print("*",end="")
                elif (i in list(range(FIRST)) + LAST and j == WALL_SPACES) and i != BIRD_Y:
                    print("*",end="")
                if i == 0 or i == BOARD_SIZE.get("HEIGHT")-1:
                    print("*",end="")
                elif j == BOARD_SIZE.get("WIDTH")-3 and i == BIRD_Y:
                    print("*",end="")
                elif (j == 0 or j == BOARD_SIZE.get("WIDTH")-1) and i != BIRD_Y:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
        counter = 0
        if counter == 0 and keyboard.is_pressed(BUTTON):
            INCREASE += 1
            counter += 1
        elif INCREASE == 6:
            INCREASE = 0
            counter = 0
        elif INCREASE:
            BIRD_Y -= 1
            INCREASE += 1
        else:
            BIRD_Y += 1
        if BIRD_Y >= BOARD_SIZE.get("HEIGHT") or BIRD_Y <= 0:
            break
        if BIRD_X == WALL_SPACES and BIRD_Y in list(range(FIRST)) + LAST:
            break
        WALL_SPACES -= 1
        if WALL_SPACES == 0:
            WALL = True
# Starting the game by merging everything
def start_game():
    BUTTON = get_jump_button()
    os.system("cls")
    GAME_STATUS = True
    PRESS_COUNTER = 0
    while GAME_STATUS:
        print("Press your jumping button to start the game")
        os.system("cls")
        if PRESS_COUNTER == 0 and keyboard.is_pressed(BUTTON):
            game(BUTTON)
            time.sleep(2)
            GAME_STATUS = input("Do you wanna play again? (y/n): ")
            os.system("cls")
            if GAME_STATUS.lower().strip() == "y":
                GAME_STATUS = True
            else:
                print("Thank you for playing our game")
                time.sleep(3)
                GAME_STATUS = False
start_game()