names = []
times = []

with open("names.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        name, time = line.split(",")
        names.append(name)
        times.append(float(time))  
        line = readfile.readline().rstrip('\n')

position = 0
mini = times[0] 
for index in range(1, len(times)):
	if mini > times[index]:
		mini = times[index]
		position = index
print(names[position], "Got the fastest time to run 100m of", mini)