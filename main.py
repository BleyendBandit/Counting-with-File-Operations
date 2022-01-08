import string

chars = 0 # Total characters
alphs = 0 # Total alphabetic characters
nums = 0 # Total digit characters
vowels = 0 # Total vowels
uppers = 0 # Total uppercase
lowers = 0 # Total lowercase
puncs = 0 # Total punctuation
char50 = 0 # Counter for every 50th character
vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
p = string.punctuation

print("Every 50th character:", sep='', end='')
f = open("input.txt", 'r')

for line in f:
  for x in line:
    chars += 1
    char50 += 1

    if char50 == 50:
      if x != '\ ' and x != '\t' and x != '\n':
        print(x, ' ', sep='', end='')
        char50 = 0

    if x.isalpha():
      alphs += 1
      nums += 1
    elif x in p:
      puncs += 1
    
    if x in vowelList:
      vowels += 1
    elif x.isupper():
      uppers += 1
    elif x.islower():
      lowers += 1
    
f.close()

print("\nTotal characters:", chars, "\nTotal alphabetic characters:", alphs, "\nTotal digits:", nums, "\nTotal vowels:", vowels, "\nTotal uppercase:", uppers, "\nTotal lowercase:", lowers, "\nTotal punctuation:", puncs)