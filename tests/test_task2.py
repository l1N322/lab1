#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "tasks" / "task2"))

from flights_package.sort_module import sort_flights
from flights_package.search_module import search_flights
from flights_package.output_module import output_flights
from flights_package.input_module import input_flights


def test_sort_flights():
    flights = [
        {"place": "Москва", "number": 3, "plane": "Boeing"},
        {"place": "Лондон", "number": 1, "plane": "Airbus"},
        {"place": "Париж", "number": 2, "plane": "Boeing"},
    ]
    result = sort_flights(flights)
    assert result[0]["number"] == 1
    assert result[1]["number"] == 2
    assert result[2]["number"] == 3


def test_sort_empty():
    assert sort_flights([]) == []


def test_search_found():
    flights = [
        {"place": "Москва", "number": 1, "plane": "Boeing"},
        {"place": "Лондон", "number": 2, "plane": "Airbus"},
        {"place": "Москва", "number": 3, "plane": "Boeing"},
    ]
    result = search_flights(flights, "Москва")
    assert len(result) == 2


def test_search_not_found():
    flights = [{"place": "Москва", "number": 1, "plane": "Boeing"}]
    result = search_flights(flights, "Берлин")
    assert result == []


def test_output_flights():
    flights = [{"number": 1, "plane": "Boeing"}]
    captured = StringIO()
    with patch("sys.stdout", captured):
        output_flights(flights)
    assert "Boeing" in captured.getvalue()


def test_output_empty():
    captured = StringIO()
    with patch("sys.stdout", captured):
        output_flights([])
    assert "не найдено" in captured.getvalue()


def test_input_flights():
    user_input = ["1", "Москва", "100", "Boeing"]
    with patch("builtins.input", side_effect=user_input):
        result = input_flights()
    assert len(result) == 1
    assert result[0]["place"] == "Москва"
    assert result[0]["number"] == 100


def test_input_zero():
    with patch("builtins.input", side_effect=["0"]):
        result = input_flights()
    assert result == []