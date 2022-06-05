# Power digit sum - Problem 16
# Created by: John Gawlik
# Date: 10/22/15
# Description:
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def main():
    print(sum(int(i) for i in str(2**1000)))

if __name__ == '__main__':
    main()
