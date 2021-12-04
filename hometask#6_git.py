break_condition = ""

while break_condition != "exit":

    car_model = input("Enter model of the car ")
    if car_model in ("mondeo", "focus", "kuga"):
        print("ford")
    elif car_model in ("tipo", "panda","500"):
        print("fiat")
    elif car_model in ("clio", "megan", "duster"):
        print("renault")
    else:
        print("I don't know such a car, enter another model")

    break_condition = input("If you want to leave enter 'exit' ")