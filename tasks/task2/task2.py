#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flights_package import *


def main():
    flights = input_flights()
    flights = sort_flights(flights)
    print("\nВсе рейсы (отсортированы по номеру): ")
    output_flights(flights)

    place = input("\nВведите пункт назначения: ")
    found = search_flights(flights, place)
    output_flights(found)


if __name__ == "__main__":
    main()
