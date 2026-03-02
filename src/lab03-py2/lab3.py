def my_sum(data):
    '''
    Calculate the sum 
    Don't use built-in functions, except for len
    
    :param data: list
    returns sum
    '''

def mean(data):
    '''
    Calculate the mean
    calls my_sum
    
    :param data: list
    returns float
    '''


def median(data):
    '''
    get the median
    
    :param data: list
    returns float
    '''


def quartiles(data):
    '''
    From a list of values, identify the first, second, and third quartiles

    use the "method of medians" to calculate the quartiles
    first get the median, then split the data into two halves, and get the median of each half.
    if the number of values is odd, exclude the median from both halves when calculating the quartiles.

    returns tuple (q1, q2, q3)
    '''



# def batch_min_max_scaler(data):
#     '''
#     Take a list of raw values and return a *new* list where every value has been scaled between 0 and 1.

#     returns list
#     '''

# def batch_sentiment_binner(data):
#     '''
#     Take a list of satisfaction scores and convert them into a list of strings: `"Low"`, `"Medium"`, or `"High"`.

#     returns a list
#     '''