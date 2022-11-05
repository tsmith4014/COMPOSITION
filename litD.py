class LitDev:

    def __init__(self, text):
        self.text = text
        self.list_words = self.turn_text_into_list_words()

    def has_palindrome(self):  # return t/f
        bool_lst = [self._test_word_is_palindrome(
            w) for w in self.list_words]  # list of t/f
        # if True in bool_lst: return True
        return any(bool_lst)
        # if len([val for val in bool_lst if val]) > 0: return True

    def turn_text_into_list_words(self):
        return self.text.split(" ")

    @staticmethod
    def _test_word_is_palindrome(word):  # return t/f
        if len(word) <= 1:
            return True

        elif word[0] == word[-1]:
            return LitDev._test_word_is_palindrome(word[1:-1])
        else:
            return False

    def same_first_and_last(self):
        lst_words = self.list_words
        if lst_words[0] == lst_words[-1]:
            return True
        else:
            return False


txt = "I fell into a racecar"
id = LitDev(txt)
