import sys
import os
import csv
import openpyxl
from collections import defaultdict


class Reader:
    def __init__(self, data_file: str):
        self.datafile = data_file
        self.path = os.path.join(sys.path[0], self.datafile)
        self.data = defaultdict(list)
    
    def extract(self) -> list:
        if self.datafile.lower().endswith('csv'):
            with open(self.path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for key in row.keys():
                        self.data[key].append(row[key])

        elif self.datafile.lower().endswith('txt'):
            with open(self.path, 'r') as file:
                temp = file.read().splitlines()
                header = temp[0] # assuming first line is always first header
                i = 1 
                while i < len(temp):
                    while not temp[i].strip().endswith(':'):
                        if temp[i] !=  '':
                            self.data[header].append(temp[i])
                        i+=1
                        if i == len(temp):
                            return self.data
                    header = temp[i] # new header
                    i+=1
        else:
            wb = openpyxl.load_workbook(self.path)
            sheet = wb.active
            temp = [row for row in sheet.values]
            for i in range(len(temp[0])):
                for ind in range(1, len(temp)):
                    self.data[temp[0][i]].append(temp[ind][i])
        return self.data
    

test = Reader('test_data.txt')
data = test.extract()
print(data)