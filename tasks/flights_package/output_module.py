def output_flights(flights):
    if not flights:
        print("Рейсов в указанный пункт назначения не найдено.")
        return

    print("\nНайденные рейсы:")
    print(f"{'Номер рейса':} {'Тип самолёта'}")
    print("-" * 30)
    for flight in flights:
        print(f"{flight['number']:} {flight['plane']}")
