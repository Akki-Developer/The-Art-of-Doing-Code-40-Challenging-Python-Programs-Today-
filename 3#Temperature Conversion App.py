print("Welcome to the Temperature Conversion App")
num = float(input("\nWhat is the given temperature in degrees fahrenheit: "))
count_res_c=round((5/9)*(num-32),4)
count_res_k=round((5/9)*(num+459.67),4)
print("Degrees Fahreneheit: "+str(round(num,4)))
print("Degrees Celsius: "+str(count_res_c))
print("Degrees Kelvin: "+str(count_res_k))