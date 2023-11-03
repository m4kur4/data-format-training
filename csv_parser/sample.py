import csv
import pprint

FILE_PATH = './sample.csv'

if __name__ == '__main__':
    with open(FILE_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

