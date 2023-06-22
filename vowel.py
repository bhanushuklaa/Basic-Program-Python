#WAP to count the number of each vowel from string

str1 = input("Write a String :")
count = 0
for x in str1:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count = count+1
print("There are ",count, "vowels in the string")
