with open("data.txt", "r") as file:

    datas = file.read().split("\n")
# extract the data from the file and assign it to variables
    _, time = datas[0].split(": ")    
    _, distance = datas[1].split(": ")
    times = list(map(int, time.split()))
    distances = list(map(int, distance.split()))
    print(distance[1].replace(" ", ""))
    big_time = [int(time.replace(" ", ""))]
    big_distance = [int(distance.replace(" ", ""))]
# create resulting variables
    
    #  loop through the races
    def calculate(times_list, distance_list):
        possible = 0
        possibles = []
        for time in times_list:
            # check all possible outcomes
            for i in range(1,time+1):
                if((i * (time - i))>distance_list[times_list.index(time)]):
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

    calculate(times, distances)
    calculate(big_time, big_distance)