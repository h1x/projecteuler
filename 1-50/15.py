# Starting in the top left corner of a 2×2 grid, and only being
# able to move to the right and down, there are exactly 6 routes
# to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def fact(number):
    if number == 0 or number == 1:
        return 1;
    else:
        return fact(number - 1) * number;

size = 20;
paths = (fact(2 * (size))) / (fact(size) * fact(size));

print(int(paths));
