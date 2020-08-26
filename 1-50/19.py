# You are given the following information, but you may prefer to do some research for yourself.
#
#   - 1 Jan 1900 was a Monday.
#   - Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#   - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
sundayCount = 0;
nextfirst = 0;

for i in range(1900, 2001):
    for j in range(12):
        if j == 0 and i == 1900:
            nextFirst = 1;
        elif j != 1:
            nextFirst = (nextFirst + monthDays[j]) % 7 + 1;
            if nextFirst == 7:
                sundayCount += 1;
        else:
            if (i % 4 == 0 and i % 400 == 0) or i % 4 != 0:
                nextFirst = (nextFirst + monthDays[j]) % 7 + 1;
                if nextFirst == 7:
                    sundayCount += 1;
            else:
                nextFirst = (nextFirst + monthDays[j] + 1) % 7 + 1;
                if nextFirst == 7:
                    sundayCount += 1;

print(sundayCount);
