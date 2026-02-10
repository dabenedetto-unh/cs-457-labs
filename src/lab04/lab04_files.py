def read_csv(file):
    """Reads a CSV file and returns a list of lists
    does not use csv.reader, splits on commas, and does not handle quoted fields
    """
    result=[]
    with open(file, 'r') as f:
        for line in f:
            result.append(line.strip().split(','))
    return result

def read_csv_dict(file):
    """Reads a CSV file and returns a list of dictionaries
    uses the first line as the keys for the dictionaries
    does not use csv.DictReader, splits on commas, and does not handle quoted fields
    """
    result=[]
    with open(file, 'r') as f:
        keys = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            result.append(dict(zip(keys, values)))
    return result