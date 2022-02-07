def traffic():
    num_of_roads = eval(input("How many roads were surveryed?:"))
    vehicles_accumulator = 0

    for days in range(num_of_roads):
        print("How many days was road", days + 1, " surveyed?")
        num_of_days = eval(input(""))
        cars_accumulator = 0

        for roads in range(num_of_days):
            print("How many cars traveled on day", roads + 1, "surveyed?")
            cars_traveled = eval(input(""))
            cars_accumulator = cars_accumulator + cars_traveled
            vehicles_accumulator = vehicles_accumulator + cars_traveled
        print("Road", days + 1, "average vehicles per day:" , cars_accumulator / num_of_days)

    print("total number of vehicles traveled on all roads:", vehicles_accumulator)
    print("average  cars traveled on all roads:", vehicles_accumulator / num_of_roads)

traffic()
