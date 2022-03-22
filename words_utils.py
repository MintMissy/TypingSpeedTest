import json
import random
from typing import List


def get_words_from_file() -> List[str]:
    file = open('data/words.json')
    words_json = json.loads(file.read())
    return words_json["words"]


def get_words(amount: int) -> List[str]:
    words = get_words_from_file()
    random_words = []
    for i in range(amount):
        random_words.append(words.pop(random.randint(0, len(words) - 1)))
    return random_words
