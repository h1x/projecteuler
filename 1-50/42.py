# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value. For example, the word value
# for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle words?

f = open("words.txt", "r");
names = f.read();
f.close();

nameList = names.split("\",\"");

nameList[0] = nameList[0].replace('"', "");
nameList[len(nameList) - 1] = nameList[len(nameList) - 1].replace('"', "");

triangleNumbers = [0] * 49;
for i in range(1, 50):
    triangleNumbers[i - 1] += int(0.5 * i * (i + 1));

def calculateWordValue(word):
    value = 0;
    for i in range(len(word)):
        value += ord(word[i]) - 64;
    return value;

result = 0;

for i in nameList:
    if calculateWordValue(i) in triangleNumbers:
        result += 1;

print(result);
