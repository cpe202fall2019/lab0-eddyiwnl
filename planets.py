def weight_on_planets():
    #Get the user input for his/her weight
    print("What do you weigh on earth?", end = '')
    userWeight = input()

    userWeight = float(userWeight)
    # Calculations
    marsWeight = (userWeight * 0.38)
    jupiterWeight = (userWeight * 2.34)


    print(" \n" + "On Mars you would weigh", marsWeight, "pounds." + "\n"  "On Jupiter you would weigh", jupiterWeight, "pounds.")

    #expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."

if __name__ == '__main__':
   weight_on_planets()
