import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def ua2_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "ua2_get_sum": ua2_get_sum,
    }
