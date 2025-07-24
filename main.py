from random import randint
from colorama import Fore, Style

random_number = randint(1,10)
count = 0

while True:

    count += 1

    player = int(input(f'\n{Fore.MAGENTA}Ədəd daxil edin : {Style.RESET_ALL}'))

    if player == random_number:
        print(f'\n{Fore.GREEN}Tapdınız!{Style.RESET_ALL}')
        print(f'{Fore.BLUE}{count} dəfə yoxladınız!{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}Ədəd dəyişdirildi!{Style.RESET_ALL}')

        random_number = randint(1,10)

    elif player > random_number and player <= 10:
        print(f'\n{Fore.CYAN}Daha kiçik!{Style.RESET_ALL}')

    elif player < random_number and player >= 1:
        print(f'\n{Fore.CYAN}Daha böyük!{Style.RESET_ALL}')

    else:
        count -= 1
        print(f'\n{Fore.YELLOW}1-10 arasında ədəd daxil edin!{Style.RESET_ALL}')