# Longest Collatz sequence under 1,000,000

def collatz_progression(n, progression_length):
    while True:
        yield n

        if n < len(progression_length) and progression_length[n] != -1:
            return

        n = (3*n + 1) if n % 2 else (n // 2)

def main():
    up_to = 1000000

    progression_length = [-1] * up_to

    # Skip 0 and set 1
    progression_length[0] = 0
    progression_length[1] = 0

    for i in range(up_to):
        if progression_length[i] != -1:
            continue

        sequence = list(collatz_progression(i, progression_length))
        count = len(sequence) + progression_length[sequence.pop()]

        for val in sequence:
            if val < len(progression_length):
                progression_length[val] = count

            count -= 1

    max_count = max(progression_length[1:])
    max_value = progression_length.index(max_count)

    print("Number with longest collatz sequence: ", max_value)

if __name__ == "__main__":
    main()

    # 837799
