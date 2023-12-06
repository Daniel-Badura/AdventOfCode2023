import re

regex = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"


inputStrings = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]
def convert(number):
    number_dict = {
        "0":"0",
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        
    }
    return number_dict.get(number, number)
sum = 0

with open('data.txt', 'r') as data:
   
    for line in data:
        matches = re.findall(regex, line)
        converted = []
        for match in matches:
            converted += convert(match)
        print(converted)
        result = int(converted[0] + converted[-1])
        print(result)
        sum += result
    print(sum)
