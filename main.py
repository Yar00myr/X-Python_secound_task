def convert_distance(feet):

    conversion_factors = {"inches": 12, "yards": 1 / 3, "miles": 0.000189393939}

    inches = feet * conversion_factors["inches"]
    yards = feet * conversion_factors["yards"]
    miles = feet * conversion_factors["miles"]

    return inches, yards, miles


while True:
    user_input = input("Введіть відстань у футах (або натисніть Enter для виходу): ")

    if user_input == "":
        break

    try:
        feet = float(user_input)
        inches, yards, miles = convert_distance(feet)

        print(f"{feet} футів = {inches} дюймів")
        print(f"{feet} футів = {yards} ярдів")
        print(f"{feet} футів = {miles} миль")
    except ValueError:
        print("Будь ласка, введіть дійсне число.")
