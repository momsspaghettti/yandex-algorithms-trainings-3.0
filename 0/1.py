if __name__ == '__main__':
    letters_frequencies = {}
    with open('input.txt', 'r') as reader:
        line = reader.readline()
        while line:
            for l_ in line:
                if l_ == ' ' or l_ == '\n':
                    continue
                if l_ not in letters_frequencies:
                    letters_frequencies[l_] = 0
                letters_frequencies[l_] += 1
            line = reader.readline()

    max_hist_height = max(letters_frequencies.values())

    letters = list(letters_frequencies.keys())
    letters.sort()
    letters_count = len(letters)

    result_lines = [[' ' for _ in range(letters_count)] for _ in range(max_hist_height)]
    for i in range(letters_count):
        for j in range(letters_frequencies[letters[i]]):
            result_lines[max_hist_height - j - 1][i] = '#'
    for line in result_lines:
        print(''.join(line))
    print(''.join(letters))
