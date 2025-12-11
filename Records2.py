from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(5)] # DECLARE BMIDetails(5) AS PERSON

for index in range(5):
    BMIdetails[index].height  = float(input("Enter height"))
    BMIdetails[index].weight  = float(input("Enter weight"))
    BMIdetails[index].bmi = BMIdetails[index].weight / (BMIdetails[index].height ** 2)

for index in range(5):
    print(BMIdetails[index])
