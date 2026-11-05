def input_flights():
    flights = []
    n = int(input("Введите количество рейсов: "))

    for i in range(n):
        print(f"\nРейс {i + 1}:")
        place = input("Название пункта назначения: ")
        number = int(input("Номер рейса: "))
        plane = input("Тип самолёта: ")

        flight = {"place": place, "number": number, "plane": plane}
        flights.append(flight)

    return flights
