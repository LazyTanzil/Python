# File-Name: Project_1_Rock_Paper_scissors
# Topic: Rock-Paper-Scissor-Game
# Author: Tanzil Islam
# Website: http://tislam.xyz
# Github : https://github.com/LazyTanzil
# Created-Date: 3/19/2021
# Created-Time: 11:45 PM

from random import choice  # need for choosing option automatic for bot player


def main_game():
    print("""
        Welcome to Rock-Paper-Scissor Game
        made by DarkCode
        (simple python project)
    """)
    # game 3 option for the game
    game_options = ['rock', 'paper', 'scissor']
    user_name = input("Enter your name: ")
    total_round = int(input("how many round you want to play"))

    # function that will take user valid choice option
    def takeOption(round_number):
        option = input(
            "Choice a option ( 1 for Rock, 2 for Paper, 3 for Scissor):\t\t\t{} of {} round\n".format(round_number + 1,
                                                                                                      total_round))
        if int(option) == 1:
            return "rock"
        elif int(option) == 2:
            return "paper"
        elif int(option) == 3:
            return "scissor"
        else:
            print("invalid option!! Please choice option between 1 to 3 only")
            takeOption(round_number)

    # decide winner base on user option
    def decideWinner(user_option):
        def subProcess():
            bot_option = choice(game_options)  # choosing computer option randomly
            if bot_option == user_option:
                subProcess()
            elif user_option == 'rock' and bot_option != 'paper' or user_option == 'paper' and bot_option != 'scissor' or user_option == 'scissor' and bot_option != 'rock':
                return 'user'
            else:
                return 'bot'

        return subProcess()

    # announce winner on round count
    def announceWinner(user_win, bot_win):
        if bot_win > user_win:
            print(f"{user_name} lose the game,\n computer win : {bot_win} times and user win : {user_win} times")
        elif user_win > bot_win:
            print(
                f"congratulation ! {user_win} Won the game,\n computer win : {bot_win} times and user win : {user_win} times")
        else:
            print(f"It's a draw match!,\n computer win : {bot_win} times and user win : {user_win} times")

            # game loop

    # game runs in a loop
    def game_loop(round_number):
        user_total_win = 0
        bot_total_win = 0

        for round_number in range(round_number):
            user_option = takeOption(round_number)  # choosing user option
            winner = decideWinner(user_option)

            if winner == "bot":
                bot_total_win += 1
                print("Ops Bot is the winner\n")
            elif winner == 'user':
                user_total_win += 1
                print("Congratulation! you are the winner.\n")
        announceWinner(user_total_win, bot_total_win)

    game_loop(total_round)


main_game()
