def read_csv(file):
    """Reads a CSV file and returns a list of lists
    does not use csv.reader, splits on commas, and does not handle quoted fields
    """

def write_csv(data, file):
    '''
    Writes a CSV file with some sample data
    does not use csv.writer, joins on commas, and does not handle quoted fields
    '''

def read_csv_dict(file):
    """Reads a CSV file and returns a list of dictionaries
    uses the first line as the keys for the dictionaries
    does not use csv.DictReader, splits on commas, and does not handle quoted fields
    """

def write_dict_csv(dict, file):
    '''
    Writes a CSV file with some sample data from a list of dictionaries
    uses the keys of the first dictionary as the header row
    does not use csv.DictWriter, joins on commas, and does not handle quoted fields
    '''
