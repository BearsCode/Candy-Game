import random

def candy_game():
    cand_on_table = 120
    while cand_on_table > 0:
        
        player_move = int(input("Сколько вы хотите взять (не более 28)?: "))
        if player_move > 28:
            print("Недопустимый ход. Пожалуйста, берите не более 28")
            continue
        cand_on_table -= player_move
        print("Конфеты, оставленные на столе:", cand_on_table)
        if cand_on_table <= 0:
            print("Ты победил!")
            return

        bot_move = random.randint(1,28)
        if bot_move > cand_on_table:
            bot_move = cand_on_table
        print(bot_move, "конфет получено ботом")
        cand_on_table -= bot_move
        print("Конфеты, оставленные на столе:", cand_on_table)
        if cand_on_table <= 0:
            print("Бот победил!")

candy_game()
