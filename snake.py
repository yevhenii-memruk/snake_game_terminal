import time
import os
import random

import keyboard

# Colors for terminal
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
reset = "\u001b[0m"
black = "\u001b[30m"

# Play Music - Multitheading
# import subprocess
# subprocess.Popen(r"C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe", "/music.mp3")

class Snake:
    def __init__(self):
        self.field = [
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
            ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
        ]
        self.status = "up"
        self.apple_position = [0, 5]
        self.snake = [[3, 5], [4, 5], [5, 5]]


    def random_apple(self) -> [int, int]:
        while True:
            row = random.randint(0, 9)
            column = random.randint(0, 9)
            if [row, column] not in self.snake:
                return [row, column]


    def keyboard_io(self, status: str) -> str:
        # Player can't change status to opposite one
        if keyboard.is_pressed("up"):
            if status == "down":
                status = "down"
            else:
                status = "up"
        elif keyboard.is_pressed("down"):
            if status == "up":
                status = "up"
            else:
                status = "down"
        elif keyboard.is_pressed("left"):
            if status == "right":
                status = "right"
            else:
                status = "left"
        elif keyboard.is_pressed("right"):
            if status == "left":
                status = "left"
            else:
                status = "right"

        return status


    def engine(self):
        while True:
            if self.snake[0][0] < 0:
                self.snake[0][0] = 9
            elif self.snake[0][0] > 9:
                self.snake[0][0] = 0
            elif self.snake[0][1] > 9:
                self.snake[0][1] = 0
            elif self.snake[0][1] < 0:
                self.snake[0][1] = 9

            # Bite of Snake (biting yourself)
            if self.snake[0] in self.snake[1:]:
                cut_snake = self.snake[1:].index(self.snake[0]) + 1
                self.snake = self.snake[:cut_snake]

            # Snake Depicturing
            print("","_"*30)
            for snake_block in self.snake:
                self.field[snake_block[0]][snake_block[1]] = f"{green}🐍{reset}"
            for line_pixels in self.field:
                print("|", end="")
                for pixel in line_pixels:
                    print(f"{black}{pixel}{reset} ", end="")
                print("|")
            print("","‾"*30)

            # Score Depicturing
            if len(self.snake) <= 3:
                score = 0
            else:
                score = len(self.snake)-3
            print(f"{yellow}Score: {score}{reset}")

            # Snake Cleaning
            for i in self.snake:
                self.field[i[0]][i[1]] = "⬜"

            # Snake Eating 
            if self.snake[0] == self.apple_position:
                self.snake.append([self.snake[-1][0] + 1, 5])
                self.apple_position = self.random_apple()

            # Apple Depicturing
            self.field[self.apple_position[0]][self.apple_position[1]] = f"{red}🍎{reset}"

            # Speed of Snake
            time.sleep(0.3) 

            self.status = self.keyboard_io(self.status)

            after_head = self.snake[0][:]  
            # Snake Engine
            for num in range(len(self.snake)):
                if num == 0:
                    if self.status == "up":
                        self.snake[0][0] -= 1
                    elif self.status == "down":
                        self.snake[0][0] += 1
                    elif self.status == "left":
                        self.snake[0][1] -= 1
                    elif self.status == "right":
                        self.snake[0][1] += 1
                if num == len(self.snake) - 1:
                    self.snake = self.snake[:-1]
                    self.snake.insert(1, after_head)

            os.system("cls")


def main():
    snake = Snake()
    snake.engine()


if __name__ == "__main__":
    main()