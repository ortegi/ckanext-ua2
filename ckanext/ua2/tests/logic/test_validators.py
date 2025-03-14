"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.ua2.logic import validators


def test_ua2_reauired_with_valid_value():
    assert validators.ua2_required("value") == "value"


def test_ua2_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.ua2_required(None)
