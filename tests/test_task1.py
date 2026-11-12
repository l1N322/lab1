#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "tasks" / "task1"))

from make_list import make_list


def test_name_replace():
    f = make_list(["строка1", "строка2", "строка3", "строка4"])
    result = f()

    assert "<li>строка1</li>" in result
    assert "<li>строка4</li>" in result


def test_html_structure():
    f = make_list(["a", "b"])
    result = f()

    assert result.startswith("<ol>")
    assert result.endswith("</ol>")
    assert result.count("<li>") == 2


def test_empty_list():
    f = make_list([])
    result = f()

    assert result == "<ol>\n</ol>"


def test_single_item():
    f = make_list(["test"])
    result = f()

    assert "<li>test</li>" in result
    assert result.count("<li>") == 1