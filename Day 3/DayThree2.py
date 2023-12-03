import sys

def is_digit_or_dot(char):
    return char.isdigit() or char == "."

def find_adjacent_digits(line, idx, direction):
    count = 0
    while 0 <= idx < len(line) and is_digit_or_dot(line[idx]):
        count += 1
        idx += direction
    return count

def calculate_ratio(line, idx, direction):
    start_idx = idx
    end_idx = idx
    while 0 <= idx < len(line) and is_digit_or_dot(line[idx]):
        end_idx = idx
        idx += direction
    return int(line[start_idx:end_idx + 1])

def process_line(lines, linenum, idx, flag):
    ratio = 1
    if flag[0] == "1":
        direction = -1
    elif flag[2] == "1":
        direction = 1
    else:
        return 0

    start_idx = idx + direction
    while 0 <= start_idx < len(lines[linenum]) and is_digit_or_dot(lines[linenum][start_idx]):
        start_idx += direction

    end_idx = start_idx
    while 0 <= end_idx < len(lines[linenum]) and is_digit_or_dot(lines[linenum][end_idx]):
        end_idx += direction

    ratio *= int(lines[linenum][start_idx:end_idx + direction])

    if flag in flag2:
        start_idx = idx + direction
        while 0 <= start_idx < len(lines[linenum]) and is_digit_or_dot(lines[linenum][start_idx]):
            start_idx += direction

        end_idx = start_idx
        while 0 <= end_idx < len(lines[linenum]) and is_digit_or_dot(lines[linenum][end_idx]):
            end_idx += direction

        ratio *= int(lines[linenum][start_idx:end_idx + direction])

    return ratio

with open("data.txt", 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    total = 0
    ratio_sum = 0

    flag1 = ["001", "010", "100", "011", "110", "111"]
    flag2 = ["101"]

    for linenum, line in enumerate(lines):
        idx = 0
        while idx < len(line):
            if line[idx].isdigit():
                temp = 0
                start_idx = idx
                end_idx = idx
                while idx < len(line) and line[idx].isdigit():
                    end_idx = idx
                    temp = temp * 10 + int(line[idx])
                    idx += 1

                is_part = False

                if linenum - 1 >= 0:
                    i = start_idx - 1
                    while i <= end_idx + 1 and not is_part:
                        if 0 <= i < len(line):
                            check = lines[linenum - 1][i]
                            if not is_digit_or_dot(check):
                                is_part = True
                        i += 1

                if not is_part and linenum + 1 < len(lines):
                    i = start_idx - 1
                    while i <= end_idx + 1 and not is_part:
                        if 0 <= i < len(line):
                            check = lines[linenum + 1][i]
                            if not is_digit_or_dot(check):
                                is_part = True
                        i += 1

                if not is_part:
                    i = start_idx - 1
                    if 0 <= i < len(line) and not is_digit_or_dot(line[i]):
                        is_part = True

                    i = end_idx + 1
                    if 0 <= i < len(line) and not is_digit_or_dot(line[i]):
                        is_part = True

                if is_part:
                    total += temp
            elif line[idx] == "*":
                adjacent = 0
                check_above = False
                check_below = False
                check_in_line = False
                flag_above = ""
                flag_below = ""

                if linenum - 1 >= 0:
                    flag_above = "".join("1" if is_digit_or_dot(lines[linenum - 1][i]) else "0"
                                         for i in range(idx - 1, idx + 2))
                    if flag_above in flag1:
                        adjacent += 1
                        check_above = True
                    elif flag_above in flag2:
                        adjacent += 2
                        check_above = True

                if linenum + 1 < len(lines):
                    flag_below = "".join("1" if is_digit_or_dot(lines[linenum + 1][i]) else "0"
                                         for i in range(idx - 1, idx + 2))
                    if flag_below in flag1:
                        adjacent += 1
                        check_below = True
                    elif flag_below in flag2:
                        adjacent += 2
                        check_below = True

                adjacent += find_adjacent_digits(line, idx - 1, -1)
                adjacent += find_adjacent_digits(line, idx + 1, 1)

                if adjacent == 2:
                    ratio_sum += process_line(lines, linenum, idx, flag_above)
                    ratio_sum += process_line(lines, linenum, idx, flag_below)
                    ratio_sum += calculate_ratio(line, idx - 1, -1)
                    ratio_sum += calculate_ratio(line, idx + 1, 1)

            idx += 1

    print("Sum of part numbers =", total)
    print("Sum of gear ratio =", ratio_sum)
