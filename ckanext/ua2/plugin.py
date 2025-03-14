from __future__ import annotations
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from typing import Any, Optional, cast
from ckan.types import AuthResult, Context, AuthFunction, ContextValidator, DataDict 


import ckanext.ua2.cli as cli
import ckanext.ua2.helpers as helpers
import ckanext.ua2.views as views
from ckanext.ua2.logic import ( action, auth, validators)


def group_create(
        context: Context,
        data_dict: Optional[dict[str, Any]] = None) -> AuthResult:
    
    
    user_name = str = context.get('user')
    

    try:
        members = toolkit.get_action('member_list')(
            {},
            {'id': 'curators', 'object_type': 'user'})
    except toolkit.ObjectNotFound:
        # The curators group doesn't exist.
        return {'success': False,
                'msg': "The curators groups doesn't exist, so only sysadmins "
                       "are authorized to create groups."}

    member_ids = [member_tuple[0] for member_tuple in members]
    
    convert_user_name_or_id_to_id = cast(
        ContextValidator,
        toolkit.get_converter('convert_user_name_or_id_to_id'))
    
    user_id = convert_user_name_or_id_to_id(user_name, context)
    
    print('User ID:', user_id)
    if user_id in member_ids:
        print('User is a curator')
        return {'success': True}
    else:
        print('User is not a curator')
        return {'success': False,
                'msg': 'Only curators are allowed to create groups'}
    
  


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        {}, {'sort': 'package_count desc', 'all_fields': True})

    print("ola")
    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups


class Ua2Plugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "ua2")

    
    
    def get_auth_functions(self):
        return {'group_create': group_create}
    # IAuthFunctions

    def get_auth_functions(self):
        return auth.get_auth_functions()

    # IActions

    def get_actions(self):
        return action.get_actions()

    # IBlueprint

    def get_blueprint(self):
        return views.get_blueprints()

    # IClick

    def get_commands(self):
         return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):
        return {'example_theme_most_popular_groups': most_popular_groups}


    # IValidators

    def get_validators(self):
        return validators.get_validators()
    
