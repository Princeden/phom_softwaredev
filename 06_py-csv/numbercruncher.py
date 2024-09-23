"""
Princeden Hom
PD - Princeden Hom and Danny Huang (5)
SoftDev
K06 -- CSV!
2024-09-19
time spent: .2
DISCO:
the csv reader is very convenient 
QCC:
relies on the specific formatting of the data, and how all the data is rounded

HOW THIS SCRIPT WORKS: 
Make a 1,000 length list with each job having a weighted amount of entries within the list
"""
import csv
import pandas
csvFile = pandas.read_csv('occupations.csv')
print(csvFile)
all_occupations = []
with open('occupations.csv', mode='r') as file:
    lines = file.readlines()
    lines=lines[1:-1]
print(lines)