import random

from src.const import RUS_ENG

LANGUAGE_QUESTION, LANGUAGE_ANSWER, TOPIC_ANSWER, DIRECTION_ANSWER, TRANSLATION_ANSWER, END = range(6)


class UserState:
    def __init__(self):
        self.state = LANGUAGE_QUESTION
        self.lang = None
        self.topic = None
        self.words = None
        self.translation_index = None  # index of word used as translation for word
        self.current_pair_index = None

    def wait_language(self):
        self.state = LANGUAGE_ANSWER

    def choose_lang(self, lang):
        self.state = TOPIC_ANSWER
        self.lang = lang

    def choose_topic(self, topic, words):
        self.state = DIRECTION_ANSWER
        self.topic = topic
        self.words = words

    def choose_direction(self, direction):
        self.state = None
        self.translation_index = 0 if direction == RUS_ENG else 1
        self._next_word()

    def get_current_word(self):
        return self.words[self.current_pair_index][1 - self.translation_index]

    def get_current_translation(self):
        return self.words[self.current_pair_index][self.translation_index]

    def get_foreign_word(self):
        return self.words[self.current_pair_index][0]

    def next_word(self, skip):
        if not skip:
            self.words.pop(self.current_pair_index)
        if len(self.words) == 0:
            return False
        self._next_word()
        return True

    def _next_word(self):
        self.current_pair_index = random.randrange(0, len(self.words))
        self.state = TRANSLATION_ANSWER

    def is_valid_answer(self, text: str):
        # todo: make smart comparison
        return self.get_current_translation().lower() == text.lower()
