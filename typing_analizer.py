from typing import Dict, List
from functools import reduce


def speed_per_word(game_results: Dict[int, List[float]], turns) -> float:
    total_typing_time = get_total_typing_time(game_results.copy())
    return total_typing_time / turns


def speed_per_letter(game_results: Dict[int, List[float]], words: List[str]) -> float:
    total_typing_time = get_total_typing_time(game_results.copy())
    letters_amount = reduce((lambda accumulator, item: accumulator + item), map(lambda word: len(word), words.copy()))
    return total_typing_time / letters_amount


def get_total_typing_time(game_results: Dict[int, List[float]]) -> float:
    total_typing_time = reduce((lambda accumulator, item: accumulator + sum(item)), [0] + list(game_results.values()))
    return total_typing_time


def print_scoreboard(game_results: Dict[int, List[float]], words: List[str]):
    print("\n░█─── ░█▀▀▀ ─█▀▀█ ░█▀▀▄ ░█▀▀▀ ░█▀▀█ 　 ░█▀▀█ ░█▀▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▄"
          "\n░█─── ░█▀▀▀ ░█▄▄█ ░█─░█ ░█▀▀▀ ░█▄▄▀ 　 ░█▀▀▄ ░█──░█ ░█▄▄█ ░█▄▄▀ ░█─░█"
          "\n░█▄▄█ ░█▄▄▄ ░█─░█ ░█▄▄▀ ░█▄▄▄ ░█─░█ 　 ░█▄▄█ ░█▄▄▄█ ░█─░█ ░█─░█ ░█▄▄▀"
          )
    # TODO generate leaderboard

    print("\n"
          "\n▀▀█▀▀ ░█──░█ ░█▀▀█ ▀█▀ ░█▄─░█ ░█▀▀█ 　 ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ▀▀█▀▀ ░█▀▀▀█"
          "\n─░█── ░█▄▄▄█ ░█▄▄█ ░█─ ░█░█░█ ░█─▄▄ 　 ─▀▀▀▄▄ ─░█── ░█▄▄█ ─░█── ─▀▀▀▄▄"
          "\n─░█── ──░█── ░█─── ▄█▄ ░█──▀█ ░█▄▄█ 　 ░█▄▄▄█ ─░█── ░█─░█ ─░█── ░█▄▄▄█"
          )
    print(
        f"\nAverage word typing speed: {round(speed_per_word(game_results, len(words)), 2)}s"
        f"\nAverage letter typing speed: {round(speed_per_letter(game_results, words), 2)}s"
        f"\n"
    )
