'''
Alex Kramer
Homework 3
DS 5010
'''

# SOURCES:
# https://www.section.io/engineering-education/run-length-encoding-algorithm-in-python/
# https://docs.python.org/3/tutorial/classes.html

'''
PROBLEM 1
'''
def rle_encode(x):
    '''
    Encodes an input iterable x using run-length encoding (RLE)
    :param x: a sequence of numbers, strings or characters
    :return: a tuple with a list of the run values and a list
    of the run lengths
    '''
    encoded_message = []
    run_length = []
    current = ''
    run_counter = 0
    for i in range(len(x)):
        if i == 0:
            current = x[i]
            run_counter = 1
        else:
            if x[i] == current:
                run_counter += 1
            else:
                encoded_message.append(current)
                run_length.append(run_counter)
                current = x[i]
                run_counter = 1
    encoded_message.append(current)
    run_length.append(run_counter)
    return (tuple(encoded_message), run_length)

'''
PROBLEM 2
'''
def rle_decode(values, lengths):
    '''
    Function decodes a list of run values and a list of run lengths.
    :param values: a tuple containing the encoded message
    :param lengths: a list containing the run lengths of each value
    :return: a list of the decoded values
    '''
    decoded = []
    for i in range(len(values)):
        item = values[i]
        item_length = lengths[i]
        for l in range(item_length):
            decoded.append(values[i])

    return decoded


class Rle:
    '''
    PROBLEM 3 - 5
    '''
    def __init__(self, values, lengths = None):
        '''
        Method creates self.lengths & self.values within the Rle class
        this function calls on the encode method below
        :param values:  a list of actual items
        :param lengths: a list of values corresponding to items, if None,
        this function will take just the values and encode them in RLE
        :returns: nothing, sets the classes self.values and self.lengths
        '''
        if lengths == None:
            Rle.encode(self, values)
        else:
            self.values = values
            self.lengths = lengths

    def encode(self, x):
        '''
        Method is a helper function with the same code as in the encode
        function above - just wanted to contain it inside the class Rle
        :parameter x: takes a list
        :returns: no returns, adjusts the self.values and self.lengths
        '''
        encoded_message = []
        run_length = []
        current = ''
        run_counter = 0
        for i in range(len(x)):
            if i == 0:
                current = x[i]
                run_counter = 1
            else:
                if x[i] == current:
                    run_counter += 1
                else:
                    encoded_message.append(current)
                    run_length.append(run_counter)
                    current = x[i]
                    run_counter = 1
        encoded_message.append(current)
        run_length.append(run_counter)

        self.values = encoded_message
        self.lengths = run_length

    def decode(self):
        '''
        Method is a helper function with the same code as in the decode
        function above - just wanted to contain it inside the class Rle
        this method is called on in later methods
        :parameter x: takes a list
        :returns: returns decoded
        '''
        decoded = []
        for i in range(len(self.values)):
            item = self.values[i]
            item_length = self.lengths[i]
            for l in range(item_length):
                decoded.append(self.values[i])
        return decoded

    def __getitem__(self, i):
        '''
        Method returns the item at the offset i of the decoded sequence
        :param i: the index that we will grab our item from
        :return: returns a single item from the data
        '''
        # returns the item at the index i from the encoded list
        decode = self.decode()
        return decode[i]

    def append(self, value):
        '''
        Method appends a new item value to the run-length encoded object
        :param value: takes in a new value aka the item to add
        :return: mutates the data, no return
        '''
        decoded = Rle.decode(self)
        decoded.append(value)
        Rle.encode(self, decoded)