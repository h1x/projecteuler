#Each new term in the Fibonacci sequence is generated by
#adding the previous two terms. By starting with 1 and 2,
#the first 10 terms will be:
#
#       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose
#values do not exceed four million, find the sum of the
#even-valued terms.

first = 1;
second = 2;

def fib(fib1, fib2, result):
    if fib1 >= 4000000 or fib2 >= 4000000:
        print(result);
        return;
    else:
        next = fib1 + fib2;
        if next % 2 == 0:
            result += next;
        fib(fib2, next, result);

fib(first, second, second);