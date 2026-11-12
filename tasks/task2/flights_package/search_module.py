def search_flights(flights, place):
    result = []
    for flight in flights:
        if flight["place"] == place:
            result.append(flight)
    return result
