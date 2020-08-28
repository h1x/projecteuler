# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into alphabetical
# order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
#  3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
#  obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

f = open("names.txt", "r");
names = f.read();
f.close();

nameList = names.split("\",\"");

nameList[0] = nameList[0].replace('"', "");
nameList[len(nameList) - 1] = nameList[len(nameList) - 1].replace('"\n', "");

nameList = sorted(nameList);
score = 0;

def calculateScore(name, positionInSortedList):
    result = 0;
    for letter in range(len(name)):
        result += ord(name[letter]) - 64;
    return result * positionInSortedList;

for i in range(len(nameList)):
    score += calculateScore(nameList[i], i + 1);

print(score);
