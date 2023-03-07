# 1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.
a = open('file_handling.txt','r')
count = 0
word = 0
character = 0
for line in a:
    wd = line.split()
    for j in wd:
        character = character + len(j)
    word = word + len(wd)
    count += 1
print('lines:',count)
print('Words:',word)
print('Characters:',character)
a.close()


# 2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.
dict = {}
b = open('Book1.csv','r')
for line in b:
    c = line.split(',')
    d = c[1].split('\n')
    dict[c[0]] = d[0]
print(dict)
b.close()
#Another way
import csv
k = open('Book1.csv','r')
dic = {}
data = csv.reader(k)
dic = {row[0]:row[1] for row in data}
print(dic)
k.close()


# 3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.
with open('slick.bin', 'rb') as f:
    hexdata = f.read().hex()
txt = open('text.txt','w')
txt.write(hexdata)
f.close()
txt.close()


# 4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.
numbers = open('num.txt','r')
sum1 = 0
for line in numbers:
    sum1 += int(line)
print(sum1)


# 5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.
with open('file_handling - Copy.txt','r') as rd:
    ls = rd.readlines()

with open('file_handling - Copy.txt','w') as rd:
    for line in ls:
        a = line.replace(' ','')
        rd.write(a)