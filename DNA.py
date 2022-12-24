### DNA PROCESSING (23/12/2023)


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

    total = 0

    for char in dna:
        if char in nucleotide:
            total = total + 1

    return total


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence (dna):

    """ (str) -> bool

    Return True if and only if the DNA sequence is valid(that
    is, it contains no characters other than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence ('CCATGG')
    True
    >>> is_valid_sequence ('ATCGAH')
    False

    """
     
    for char in dna:
        if not (char in 'atcgATCG'):
            return 'False'

    return 'True'


def insert_sequence (seq1, seq2, insert):

    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA
    sequence into the first DNA sequence at the given index - (insert);

    >>> insert_sequence ('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence ('ATCG','AH',4)
    'ATCGAH'
    """ 

    dna = seq1[:insert]+ seq2 + seq1[insert:]
    
    return dna

def get_complement (nuc):

    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement ('A')
    'AT'
    >>> get_complement ('G')
    'GC'
    """

    
    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'
    else:
        return 'Insert a valid nucleotide\'s type.'
    

def get_complementary_sequence (complement):

    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence ('AT')
    'TA''
    >>> get_complementary_sequence ('CG')
    'GC'
    """

    s = ''

    for nuc in complement:
        s = s + get_complement (nuc)

    return s


     



        
    


    

    

        
