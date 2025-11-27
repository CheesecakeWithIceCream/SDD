names = ["John","Joan","Mark","Michael"]
ages = [23,35,23,8]
birth = ["June","May","December","July"]


with open("names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + "," + str(ages[counter]) + "," + birth[counter] + "\n")
