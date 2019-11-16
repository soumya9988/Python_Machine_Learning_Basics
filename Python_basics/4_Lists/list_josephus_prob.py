def josephus_count(no_of_ppl, step):
    """
    (int, int) --> list of int
    Input data will contain number of people(no_of_ppl) and the counting step(step).
    Function will remove the person at the position marked by step and return the last person
    remaining. Initial numbering starts from 1.
    >>> josephus_count(20, 4)
    [17]
    >>> josephus_count(10, 2)
    [11]
    """
    list_ppl = [i for i in range(1, no_of_ppl + 1)]
    pos = step - 1
    while len(list_ppl) > 1:
        if pos >= len(list_ppl):
            pos = pos % len(list_ppl)
        pop_no = list_ppl.pop(pos)
        pos = pos + step -1

    return list_ppl


print(josephus_count(17, 3))