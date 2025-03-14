"""Tests for helpers.py."""

import ckanext.ua2.helpers as helpers


def test_ua2_hello():
    assert helpers.ua2_hello() == "Hello, ua2!"
