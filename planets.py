def weight_on_planets():
    #Get the user input for his/her weight
    userWeight = input("What do you weigh on earth?")

    userWeight = float(userWeight)
    # Calculations
    marsWeight = (userWeight * 0.38)
    jupiterWeight = (userWeight * 2.34)

    print("\n")
    print("On Mars you would weigh", marsWeight, "pounds.")
    print("On Jupiter you would weigh", jupiterWeight, "pounds.")


if __name__ == '__main__':
   weight_on_planets()
