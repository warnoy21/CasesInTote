print(""" Packaging Metric: number of cases in a tote
""")

while True:
    oz = (input("Enter the weight of the tote from the barcode(Oz): "))

    if not oz.isdigit():
        print("Enter a numerical value or convert it to nearest non-decimal number.")

    else:
        break

oz_to_kg = 35

conv = int(oz) / oz_to_kg

kg = (conv) * 1000

integer = (round(kg, -3))

intt = round(integer)

print(f"{intt} kg per tote (converted from actual weight {conv} x 1000 = {kg} kg )")

while True:
    num_case = (input("Enter the number of cartons in a case :  "))
    if not num_case.isdigit():
        print("This only accepts a numerical value without decimal, try again ")


    else:
        break




while True:
    carton = (input("Enter the weight of a carton in grams: "))
    if not carton.isdigit():
        print("This only accepts a numerical value without decimal,try again ")


    else:
        break

weight_case = int(num_case) * int(carton)

we_ca_rounded = (weight_case)


cases_in_totes = kg / we_ca_rounded

case_count = round(cases_in_totes)

print(f"""          {str(case_count)}  cases per tote approximately          """)


ex = input("press enter to exit")

print(ex)