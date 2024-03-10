
from colorama import Fore, Style
import random
import time

import pygame

pygame.init()
cheer_sound = pygame.mixer.Sound(r"C:\Users\melan\Downloads\cheer.mp3")
levelup_sound = pygame.mixer.Sound(r"C:\Users\melan\Downloads\level-up.mp3")

def ask_question(difficulty):
    while True:
        num1 = random.randint(1, difficulty * 10)
        num2 = random.randint(1, difficulty * 10)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            answer = num1 + num2
            symbol = '➕'
        elif operator == '-':
            answer = num1 - num2
            symbol = '➖'
        elif operator == '*':
            answer = num1 * num2
            symbol = '✖️'
        user_answer = float(input(f"{Style.BRIGHT}{Fore.CYAN}🧠🔢 What is {num1} {symbol} {num2}? {Style.RESET_ALL}"))
        if user_answer == answer:
            levelup_sound.play() 
            return True
        else:
            print(f"{Style.BRIGHT}{Fore.RED}🙈 Oh no! That's not quite right. The correct answer was: {answer}")
            print(f"{Style.BRIGHT}{Fore.YELLOW}🤔 Let's try again! You got this!{Style.RESET_ALL}")
            time.sleep(1)  # Wait for 1 second before retrying
            
def main():
    print(f"{Style.BRIGHT}{Fore.GREEN}👋 Hi! Let's improve your math skills together. Just type in your answer and press enter!")
    score = 0
    num_questions = 15
    for i in range(num_questions):
        print(f"{Style.BRIGHT}{Fore.MAGENTA}🎲 Question {i + 1}:")
        if ask_question(score // 2 + 1):
            print(f"{Style.BRIGHT}{Fore.GREEN}🎉 Yippeee, you got it!{Style.RESET_ALL}")
            score += 1
            time.sleep(0.5)  # Pause briefly for visual effect
    print(f"{Style.BRIGHT}{Fore.GREEN}🎉 Congratulations, you've leveled up!Way to go superstar 🌟 {Style.RESET_ALL}")
    cheer_sound.play()
    pygame.event.poll() 
    
if __name__ == "__main__":
    main()
