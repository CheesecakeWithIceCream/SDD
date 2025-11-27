from dataclasses import dataclass
@dataclass
class TEMP():
    day : int = 0
    dayTemp : float = 0.0

temp_details = [TEMP() for index in range(14)]
def set_record():
    for index in range(14):
        temp_details[index].day = index +1

average = 0
def avg(TEMP):
    average = 0
    for index in range(14):
        average += temp_details[index].dayTemp
    average = average/14
    with open ("avgTemp.txt", "w") as writefile:
            writefile.write(str(average))
            print(average, "is average")
            return average
    

def mini(TEMP):
    mini = temp_details[0].dayTemp
    for index in range(13):
        if mini < temp_details[index].dayTemp:
            mini = temp_details[index].dayTemp
    print(mini, "is minimum")
    return mini

def maxi(TEMP):
    max = temp_details[0].dayTemp
    for index in range(13):
        if max > temp_details[index].dayTemp:
            max = temp_details[index].dayTemp
    print(max, "is max")
    return max


def get_data():
    for index in range(14):
        temp_details[index].dayTemp = float(input("Enter day's temperature: "))
        while temp_details[index].dayTemp  > 50 or temp_details[index].dayTemp < -20:
            print("Error message, enter temperature between -20 and 50")
            temp_details[index].dayTemp = float(input("What tempearture would you like to add: "))

set_record()
get_data()
avg(TEMP)
mini(TEMP)
maxi(TEMP)