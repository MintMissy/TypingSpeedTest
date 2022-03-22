import game_core
import json

# INITIALIZE game settings
settings = json.loads(open('config.json').read())
available_difficulties = ['short', 'normal', 'long']
game_turns = {
    'short': settings["TURNS_PER_SHORT_GAME"],
    'normal': settings["TURNS_PER_NORMAL_GAME"],
    'long': settings["TURNS_PER_LONG_GAME"],
}


def game_duration_input() -> str:
    return input("Pick one of 3 available game durations: 'short', 'normal', 'long'\n")


def game_duration_request() -> str:
    game_duration = game_duration_input()
    while game_duration not in available_difficulties:
        game_duration = game_duration_input()
    return game_duration


game_core.clear_console()
print("\n░█▀▀▀ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ 　 ░█▄─░█ ▀█▀ ░█▀▀█ ░█─▄▀ ░█▄─░█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ "
      "\n░█▀▀▀ ░█░█░█ ─░█── ░█▀▀▀ ░█▄▄▀ 　 ░█░█░█ ░█─ ░█─── ░█▀▄─ ░█░█░█ ░█▄▄█ ░█░█░█ ░█▀▀▀ "
      "\n░█▄▄▄ ░█──▀█ ─░█── ░█▄▄▄ ░█─░█ 　 ░█──▀█ ▄█▄ ░█▄▄█ ░█─░█ ░█──▀█ ░█─░█ ░█──░█ ░█▄▄▄"
      )
nickname = input('\n')

game_core.clear_console()
print("\n░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ░█▀▀▄ ░█─░█ ░█▀▀█ ─█▀▀█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▄─░█ "
      "\n░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀ 　 ░█─░█ ░█─░█ ░█▄▄▀ ░█▄▄█ ─░█── ░█─ ░█──░█ ░█░█░█ "
      "\n░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄ 　 ░█▄▄▀ ─▀▄▄▀ ░█─░█ ░█─░█ ─░█── ▄█▄ ░█▄▄▄█ ░█──▀█")

print(f"\nHello {nickname}!")
selected_game_length = game_duration_request()

# Initialize words
game_core.run(game_turns[selected_game_length], selected_game_length, nickname)
