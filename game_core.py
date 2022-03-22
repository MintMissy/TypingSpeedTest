import time
from typing import Dict, List

import words_utils
import typing_analizer
import leader_board

# This list contains all typing times for given word length
game_results: Dict[int, List[float]] = {}


def clear_console():
    print('\n' * 150)


def word_input(turn_word) -> str:
    return input(f"{turn_word}\n")


def word_request(turn_word):
    """
    This function takes and validates typed word by user
    :param turn_word: word that has to be typed in order to complete turn
    """
    typed_word = word_input(turn_word)
    while typed_word != turn_word:
        clear_console()
        typed_word = word_input(turn_word)


def play_turn(turn_word: str) -> float:
    """
    Play single turn. Returns time after word was correctly typed
    """
    typing_start_timestamp = time.time()
    word_request(turn_word)
    typing_time = time.time() - typing_start_timestamp
    return typing_time


def save_turn_score(typing_time, word):
    word_len = len(word)
    if word_len in game_results.keys():
        game_results[word_len].append(typing_time)
    else:
        game_results[word_len] = [typing_time]


def run(turns: int, game_length: str, nickname: str):
    words_to_type = words_utils.get_words(turns)

    for word in words_to_type:
        clear_console()
        typing_time = play_turn(word)
        save_turn_score(typing_time, word)

    clear_console()
    typing_analizer.print_scoreboard(game_results, words_to_type)
