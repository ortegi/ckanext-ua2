"""Tests for views.py."""

import pytest

import ckanext.ua2.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "ua2")
@pytest.mark.usefixtures("with_plugins")
def test_ua2_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("ua2.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, ua2!"
