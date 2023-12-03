def check_data(line):
    global correct
    global power_sum
    data = line.split(':')
    id = data[0].lstrip('Game').strip()
    pairs = data[1].replace(',', '').split(';')
    limits = {'red': 12, 'green': 13, 'blue': 14}
    counts = {'red': 0, 'green': 0, 'blue': 0}

    for pair in pairs:
        elements = pair.split()
        for i in range(0, len(elements), 2):
            if int(elements[i]) > counts[elements[i+1]]:
                counts[elements[i+1]] = int(elements[i])

    if counts['red'] <= limits['red'] and \
        counts['green'] <= limits['green'] and \
        counts['blue'] <= limits['blue']:
            correct.append(id)

    power_sum += counts["red"] * counts["green"] * counts["blue"]

def get_data():
    with open('data.txt', 'r') as dat:
        data = [line.strip() for line in dat]
        return data

if __name__ == '__main__':
    data = get_data()
    correct = []
    power_sum = 0
    
    for line in data:
        check_data(line)

    print(f'Part 1: {sum(map(int, correct))}')
    print(f'Part 2: {power_sum}')
