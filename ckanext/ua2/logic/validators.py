import ckan.plugins.toolkit as tk


def ua2_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "ua2_required": ua2_required,
    }
