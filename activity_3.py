# Random algorithm exercise.
def remove_e (sentence: str) -> str:
    """
    Removing letter 'e' in the sentence.
    """
    sen_low = sentence.lower()
    sen_len = len(sen_low)
    let_ctr = 0
    new_sen = ''

    while sen_len - 1 >= let_ctr:
        if sen_low[let_ctr] != 'e':
            new_sen += sen_low[let_ctr]
        let_ctr += 1

    return new_sen