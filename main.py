from activity_1 import get_anagram
from activity_2 import get_pop_item
from activity_3 import remove_e
from activity_4 import sum_two_for_target

anagram_user_input_1 = 'FirEd'
anagram_user_input_2 = 'fRiEd'
 
random_list = ['apple', 'pineapple', 'Toyota', 'Honda']

random_sentence = 'If I weRE to LiVe THIS wOrld WithOut U.'

random_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

if __name__== '__main__':
    #print(get_anagram(anagram_user_input_1, anagram_user_input_2))
    #print(get_pop_item(random_list))
    #print(remove_e(random_sentence))
    print(sum_two_for_target(random_num, target))