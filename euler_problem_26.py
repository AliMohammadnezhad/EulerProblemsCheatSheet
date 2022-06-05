# Reciprocal cycles - Problem 26
# Problem 26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# Answer: 983
 
def main():
   max_cycle = 0
   max_d = 0
   for d in range(1, 1000):
       cycle = get_cycle(d)
       if cycle > max_cycle:
           max_cycle = cycle
           max_d = d
   print(max_d)

def get_cycle(d):
    remainder = 1
    remainder_list = []
    while remainder not in remainder_list:
        remainder_list.append(remainder)
        remainder *= 10
        remainder %= d
    return len(remainder_list)



if __name__ == '__main__':
    main()