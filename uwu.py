import random
import re
from functools import partial

WORD_REPLACE = {
    "small": "smol",
    "cute": "kawaii~",
    "fluff": "floof",
    "love": "luv",
    "stupid": "baka",
    "idiot": "baka",
    "what": "nani",
    "meow": "nya~",
    "roar": "rawrr~",
}

EMOJIS = [
    "rawr x3",
    "OwO",
    "UwU",
    "o.O",
    "-.-",
    ">w<",
    "σωσ",
    "òωó",
    "ʘwʘ",
    ":3",
    "XD",
    "nyaa~~",
    "mya",
    ">_<",
    "rawr",
    "uwu",
    "^^",
    "^^;;",
]

REGEX_WORD_REPLACE = re.compile(r"(?<!w)[lr](?!w)")

REGEX_PUNCTUATION = re.compile(r"[.!?\r\n\t]")

REGEX_STUTTER = re.compile(r"(\s)([a-zA-Z])")
SUBSTITUTE_STUTTER = r"\g<1>\g<2>-\g<2>"

REGEX_NYA = re.compile(r"n([aeou][^aeiou])")
SUBSTITUTE_NYA = r"ny\1"

REGEX_EMOJI = re.compile(r"<(a)?:(\w+?):(\d{15,21}?)>", re.ASCII)


class Uwu:
    def __init__(self, input_string):
        self.input = input_string

    def _word_replace(self, input_string: str) -> str:
        for word, replacement in WORD_REPLACE.items():
            input_string = input_string.replace(word, replacement)
        return input_string

    def _char_replace(self, input_string: str) -> str:
        """Replace certain characters with 'w'."""
        return REGEX_WORD_REPLACE.sub("w", input_string)

    def _stutter(self, strength: float, input_string: str) -> str:
        """Adds stuttering to a string."""
        return REGEX_STUTTER.sub(
            partial(self._stutter_replace, strength=strength), input_string, 0
        )

    def _stutter_replace(self, match: re.Match, strength: float = 0.0) -> str:
        """Replaces a single character with a stuttered character."""
        match_string = match.group()
        if random.random() < strength:
            return f"{match_string}-{match_string[-1]}"  # Stutter the last character
        return match_string

    def _nyaify(self, input_string: str) -> str:
        """Nyaifies a string by adding a 'y' between an 'n' and a vowel."""
        return REGEX_NYA.sub(SUBSTITUTE_NYA, input_string, 0)

    def _uwuify(
        self,
        input_string: str,
        *,
        stutter_strength: float = 0.2,
        emoji_strength: float = 0.1,
    ) -> str:
        """Takes a string and returns an uwuified version of it."""
        input_string = input_string.lower()
        input_string = self._word_replace(input_string)
        input_string = self._nyaify(input_string)
        input_string = self._char_replace(input_string)
        input_string = self._stutter(stutter_strength, input_string)
        return input_string

    def run(self):
        return self._uwuify(self.input)
