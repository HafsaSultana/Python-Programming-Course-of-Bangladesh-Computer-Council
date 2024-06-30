def find_longest_line(filename):
    with open(filename, encoding='utf-8') as file:
        longest_line = ''
        for line in file:
            if len(line) > len(longest_line):
                longest_line = line
        return longest_line

print(find_longest_line('input.txt'))
