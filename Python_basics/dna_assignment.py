
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count += 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    pos = dna1.find(dna2)
    if pos >= 0:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """
    (str) --> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than
    'A', 'T', 'C', 'G'.
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGP')
    False
    >>> is_valid_sequence('ATCGGc')
    False

    """
    for char in dna:
        if char.islower() or char not in 'ATCG':
            return False
    return True


def insert_sequence(dna1, dna2, ind):
    """
    (str, str, int) --> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the
    first DNA sequence at the given index.
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('AAAG', 'CC', -3)
    ACCAAG
    >>> insert_sequence('AG', 'TT', 0)
    TTAG

    """
    dna = ""
    if ind > 0:
        dna = dna1[:ind] + dna2 + dna1[ind:]
    elif ind < 0:
        ind1 = len(dna1) + ind
        dna = dna1[:ind1] + dna2 + dna1[ind1:]
    else:
        dna = dna2 + dna1
    return dna


def get_complement(dna):
    """
    (str) --> str

    Return the nucleotide's complement.(A <-> T, C <-> G)
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C

    """
    if dna == 'A': return 'T'
    elif dna == 'T': return 'A'
    elif dna == 'C': return 'G'
    elif dna == 'G': return 'C'


def get_complementary_sequence(dna):
    """

    (str) --> str
    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('ATGG')
    TACC
    >>> get_complementary_sequence('CCCAAA')
    GGGTTT

    """
    dna_seq = ''
    for nucleotide in dna:
        dna_seq += get_complement(nucleotide)
    return dna_seq



