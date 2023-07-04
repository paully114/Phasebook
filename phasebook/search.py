from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    search_id = args.get('id')
    search_name = args.get('name')
    search_age = args.get('age')
    search_occupation = args.get('occupation')

    matching_users = []
    
    for user in USERS:
        if search_id and user['id'] == search_id:
            matching_users.append(user)
        elif search_name and search_name.lower() in user['name'].lower():
            matching_users.append(user)
        elif search_age and check_age_match(user['age'], search_age):
            matching_users.append(user)
        elif search_occupation and search_occupation.lower() in user['occupation'].lower():
            matching_users.append(user)

    return matching_users

def check_age_match(user_age, search_age):
    try:
        age_diff = abs(int(user_age) - int(search_age))
        return age_diff <= 1
    except ValueError:
        return False
