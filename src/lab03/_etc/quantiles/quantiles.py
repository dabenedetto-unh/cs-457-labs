import random
import statistics as stats
import math
import pandas as pd

def median(data):
    n = len(data)
    mid = n//2

    if n%2 == 0:
        return (data[mid-1] + data[mid])/2
    else:
        return data[mid]

def quartile(data,k, method='exclusive'):
    '''
    stats library uses 'exclusive' method
    pandas uses 'standard' method
    '''

    data = sorted(data)
    n = len(data)

    if method == 'exclusive':
        # Formula: (n+1) * q
        # Convert to 0-based: index = ((n+1) * k/4) - 1
        idx_float = (k * (n + 1) / 4) - 1
    elif method == 'standard':
        # Formula: (n-1) * q
        # Already 0-based: index = (n-1) * k/4
        idx_float = k * (n - 1) / 4
    else:
        raise Exception("invalid method")

    # Correct way to get lower/upper bounds for any float index
    l = math.floor(idx_float)
    u = math.ceil(idx_float)
    dec = idx_float - l

    # Boundary safety
    if l < 0: return data[0]
    if u >= n: return data[-1]

    return data[l] + (data[u] - data[l]) * dec

def quartiles_interpolate(data, method='exclusive'):

    q1 = quartile(data,1,method)
    q2 = quartile(data,2,method)
    q3 = quartile(data,3,method)

    return q1,q2,q3

def quartiles_medians(data):

    data = sorted(data)
    # print(data)

    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        # Even: Split exactly in half
        low_half = data[:mid]
        high_half = data[mid:]
    else:
        # exclusive - ignore median
        low_half = data[:mid]
        high_half = data[mid+1:]

    # print(data)
    # print(low_half)
    # print(high_half)

    q1 = median(low_half)
    q2 = median(data)
    q3 = median(high_half)
    
    return q1, q2, q3
    
def test_five_number(data, method='medians'):

    n = len(data)
    print(method, n)
    # print(sorted(data))

    if method=='medians':

        summary = quartiles_medians(data)

        if n%2==0:
            series = pd.Series(data)
            if n%4==0:
                # each half is even
                q1 = series.quantile(0.25, interpolation='midpoint')     
                q2 = series.quantile(0.5, interpolation='midpoint') 
                q3 = series.quantile(0.75, interpolation='midpoint') 
            else:
                # each half is odd
                q1 = series.quantile(0.25, interpolation='lower')     
                q2 = series.quantile(0.5, interpolation='midpoint') 
                q3 = series.quantile(0.75, interpolation='higher') 
            qts = q1,q2,q3
        else:
            # compare to exclusive method
            qts = stats.quantiles(data)

        # print(summary)
        # return

    elif method=='exclusive':

        summary = quartiles_interpolate(data)
        qts = stats.quantiles(data)

    elif method=='standard':

        summary = quartiles_interpolate(data,method='standard')

        series = pd.Series(data)
        qts = series.quantile([0.25,0.5,0.75], interpolation='linear')
        qts = qts.values
        # qts = q1,q2,q3  

    # elif method=='midpoint':

    #     summary = quartiles_interpolate(data,method='standard')

    #     series = pd.Series(data)
    #     q1 = series.quantile(0.25, interpolation='linear')
    #     q2 = series.quantile(0.5, interpolation='linear')
    #     q3 = series.quantile(0.75, interpolation='linear')
    #     qts = q1,q2,q3  



    print(summary)
    print(qts)

    # assert summary == qts
    for s, q in zip(summary, qts):
        assert math.isclose(s, q)     

if __name__=="__main__":

    for _ in range(10):
        n = random.randint(10,20)

    # for n in [7,9]:

        # get some random data
        random.seed(42)
        data = [random.randint(0, 100) for _ in range(n)]
        # f9 = data[:9]

        if n%2==0:
            print("########## EVEN N ###############")
        else:
            print("########## ODD N ###############")

        print("n =",n)
        print(sorted(data))

        # for even n
        test_five_number(data, method='medians')    # PASS
        test_five_number(data,method='exclusive') # PASS
        test_five_number(data,method='standard') # PASS
            
        # # for odd n
        # test_five_number(f9, method='medians') # PASS
        # test_five_number(f9,method='exclusive') # PASS
        # test_five_number(f9,method='standard') # PASS

        # # for odd n, medians equals exclusive