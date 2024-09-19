"""
Princeden Hom
PD - Princeden Hom and Danny Huang (5)
SoftDev
K06 -- CSV!
2024-09-19
time spent:
DISCO:

QCC:

HOW THIS SCRIPT WORKS: 
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