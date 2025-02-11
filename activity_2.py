# Practice on list to list pop to append, to check if how it works.
def get_pop_item(sample_list:str) -> str:
    popped_word = []

    for word in sample_list[:]:
        sample_list.pop(sample_list.index(word))
        popped_word.append(word)
    
    return popped_word
