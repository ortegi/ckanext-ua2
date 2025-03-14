import ckan.plugins.toolkit as tk
import ckanext.ua2.logic.schema as schema


@tk.side_effect_free
def ua2_get_sum(context, data_dict):
    tk.check_access(
        "ua2_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.ua2_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'ua2_get_sum': ua2_get_sum,
    }
