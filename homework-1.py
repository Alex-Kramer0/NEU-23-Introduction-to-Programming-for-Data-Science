'''
    Alex Kramer
    DS 5010
    Homework 1
    Spring 2023
'''

'''
Problem 1
'''
def cummax(x):
    '''
    Function: Calculates and returns a list giving the cumulative maximum
    of elements of x
    Parameter: x ( a list of numbers )
    Return: The return value is a list with the same length as x
    '''

    max_list = []
    max_list.append(x[0])
    # appends first number from x list
    for num in x:
        if num > max_list[-1]:
            max_list.append(num)
        else:
            max_list.append(max_list[-1])
    max_list.remove(max_list[0])
    # removes the first number from x list so that we do not
    # have a duplicate
    return max_list


'''
Problem 2
'''
def cumsum(x):
    '''
    Function: Calculates and returns a list giving the cumulative sums of elements of x
    Parameter: x ( a list of numbers )
    Return: The return value is a list with the cumulative sums of x, and is same length as x
    '''

    new_list = []
    for index, number in enumerate(x):
        if index == 0:
            new_list.append(number)
        else:
            sum = number + new_list[index - 1]
            new_list.append(sum)
    return(new_list)


'''
Problem 3
'''
def tokenize(s):
    '''
    Function: tokenizes a string into a list of words
    Parameter: takes 's' a string
    Return: returns a list of strings with only alphanumeric characters
    that are suitable for caseless comparisons
    '''
    remove = ['!', '.', '@', ',', '?', '%', ':', ';', '*', '&',
              '#', '$', '^', '(', ')', '-', '_', '+', '=','~',
              '`', '<', '>']
    # list of characters to be removed

    new_list = []
    split = s.split()
    # splits the starting string into a list based off spaces
    for word in split:
        for character in word:
            if character in remove:
                word = word.replace(character, '')
                # loops through each character in a word and
                # replaces any characters that are in the remove list
        new_list.append(word.lower())
    return new_list


'''
Problem 4
'''
def count_words(s):
    '''
    Function:C ounts the occurences of unique words in a string
    Parameter: takes string s
    Return: returns the result as a dictionary
    '''
    s = tokenize(s)
    # calling a past function because it does the basics for how
    # to solve this problem
    dictionary = {}
    for word in s:
        if word in dictionary:
            x = 1
            # a placeholder, we do not use x
        else:
            count = s.count(word)
            dictionary[word] = count
    return dictionary


'''
Problem 5
'''
def ifelse(test, yes, no):
    '''
    Function: Chooses elements from yes or no based on the values of test
    Parameter: takes three lists, the first providing the choice, the rest
    where the choices are being taken on
    Return: The return value should be a list with the same length as x
    '''
    output = []
    for i in range(len(test)):
        if test[i] == True:
            output.append(yes[i])
        else:
            output.append(no[i])

    return output