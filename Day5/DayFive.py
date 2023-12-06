with open("data.txt", "r") as data_file:
    seeds_str, *block_lines = data_file.read().split("\n\n")
    seeds = list(map(int, seeds_str.split(":")[1].split()))

for block_str in block_lines:
    block_ranges = []
    for line in block_str.splitlines()[1:]:
        dest, src, rng = list(map(int, line.split()))
        block_ranges.append((dest, src, rng))

    result_list = []
    for seed_value in seeds:
        for dest, src, rng in block_ranges:
            if src <= seed_value < src + rng:
                result_list.append(seed_value - src + dest)
                break
        else:
            result_list.append(seed_value)

    seeds = result_list

print(min(seeds))
