with open("data.txt", "r") as file:

    datas = file.read().split("\n")
# extract the data from the file and assign it to variables
    _, time = datas[0].split(": ")    
    _, distance = datas[1].split(": ")
    times = list(map(int, time.split()))
    distances = list(map(int, distance.split()))

    print(times)
    print(distances)
# create resulting variables
    possible = 0
    possibles = []
    #  loop through the races
    for time in times:
        # check all possible outcomes
        for i in range(1,time+1):
           if((i * (time - i))>distances[times.index(time)]):
               possible += 1
        else:
            possibles.append(possible)
            possible = 0
    multiplication = 1
    # multiply the possibilities
    for race in possibles:
        multiplication *= race
    print(possibles)
    print(multiplication)