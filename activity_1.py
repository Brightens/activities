# Anagram
def get_anagram(word_1: str, word_2: str) -> str:
    anagram_word_1 = []
    anagram_word_2 = []
    word_1_fix = ''.join(word_1.lower().split())
    word_2_fix = ''.join(word_2.lower().split())
    word_1_len = len(word_1_fix)
    word_2_len = len(word_2_fix)
    letter_counter = 0
    anagram_YoN = False

    while letter_counter <= word_1_len -1:
        anagram_word_1.append(word_1_fix[letter_counter])
        letter_counter += 1

    letter_counter = 0
    while letter_counter <= word_2_len -1:
        anagram_word_2.append(word_2_fix[letter_counter])
        letter_counter += 1

    anagram_word_2.sort()
    anagram_word_1.sort()
    if anagram_word_2 == anagram_word_1:
        anagram_YoN = True

    return anagram_YoN