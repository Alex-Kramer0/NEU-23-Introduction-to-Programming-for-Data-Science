'''
Alex Kramer
DS 5010
Homework 2
Spring 2022
'''

'''
Problem 1
'''
def median(x):
    '''
    Function: calculates the median value of an iterable x
    Parameters: x is a list of numeric elements
    Returns: the median value of the list
    '''
    x.sort()
    mid_index = (len(x) // 2)
    if len(x) % 2 == 0:
        # if length is even
        median = (x[mid_index] + x[mid_index - 1]) / 2
    else:
        # if length is odd
        median = x[mid_index]

    return median

'''
Problem 2
'''
def iqr(x):
    '''
    Function: Calculates the interquartile range of an iterable x
    Parameter: takes x, a list of numbers
    Returns: the IQR
    '''
    x.sort()
    if len(x) <= 1:
        return 0

    elif len(x) % 2 ==0:
        # length is even
        Q1 = median(x[:len(x) // 2])
        Q3 = median(x[len(x) // 2:])
        IQR = Q3 - Q1
        return IQR
    else:
        # lenth is odd
        Q1 = median(x[:(len(x) // 2) + 1 ])
        Q3 = median(x[len(x) // 2:])
        IQR = (Q3 - Q1)
        return IQR
'''
Problem 3
'''
def fivenum(x):
    '''
    Function: Calculates the Tukey's five number summary of an iterable x
    Parameter: takes x, a list of numbers
    Return: tukey's five number summary
    '''
    x.sort()

    if len(x) % 2 ==0:
        # length is even
        Q1 = median(x[:len(x) // 2])
        Q3 = median(x[len(x) // 2:])

    else:
        # lenth is odd
        Q1 = median(x[:(len(x) // 2) + 1 ])
        Q3 = median(x[len(x) // 2:])

    tukey = [x[0], Q1, median(x), Q3, x[-1]]
    # creating the list to be returned, this list
    # contains five summary statistics: the minimum, Q1,
    # the median, Q3, and the maximum of the dataset

    return tukey

'''
Problem 4
'''
def order(x):
    '''
    Function: Returns a list giving the indicies of the elements of
    x as sorted in order from least to greatest
    Parameter: takes x, a list of numbers
    Returns: a list
    '''
    sorted_x = x.copy()
    sorted_x.sort()
    index_list = []
    for e in sorted_x:
        index = x.index(e)
        index_list.append(index)

    return index_list

'''
Problem 5
'''
def rank(x):
    '''
    Function: returns a list giving the sample ranks of the
    corresponding elements of x
    Parameter: takes x, a list of numbers
    Returns: a list
    '''
    sorted_x = x.copy()
    sorted_x.sort()
    rank_list = []
    for e in x:
        index = sorted_x.index(e)
        rank_list.append(index + 1)
    return rank_list