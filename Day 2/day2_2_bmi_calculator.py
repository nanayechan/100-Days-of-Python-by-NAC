weight = input('enter your weight in kg:')
height = input("enter your height in m: ")
#weight_as_int = int(weight)
#height_as_float = float(height)
#bmi = weight_as_int / height_as_float **2
#bmi_as_int = int(bmi)
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)