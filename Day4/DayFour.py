with open('data.txt', 'r') as file:
    card_lines = file.readlines()

total_points = 0
total_scratch_cards = 0
line_copies_dict = {i: 1 for i in range(len(card_lines))}

for line_number, card_line in enumerate(card_lines):
    semi_colon_idx = card_line.index(':')
    bar_idx = card_line.index('|')

    winning_numbers = [num for num in card_line[semi_colon_idx:bar_idx].split() if num.isdigit()]
    own_numbers = [num for num in card_line[bar_idx:-1].split() if num.isdigit()]
    matching_numbers = [x for x in winning_numbers if x in own_numbers]
    matching_numbers_len = len(matching_numbers)

    total_scratch_cards += 1
    scratch_copies = line_copies_dict[line_number]

    if matching_numbers_len > 0:
        total_points += 2 ** (matching_numbers_len - 1)
        total_scratch_cards += (matching_numbers_len * scratch_copies)

    for i in range(line_number, line_number + matching_numbers_len):
        line_copies_dict[i + 1] = line_copies_dict.get(i + 1, 0) + (1 * scratch_copies)

print('Part 1:', total_points)
print('Part 2:', total_scratch_cards)
