import requests
import json


def get_randomuser():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()
        return data
    return False

def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'fullname': user fullname,
            'age': user age,
            'country': user country
        }
    '''
    data = user_data['results'][0]
    return {
        'fullname': f'{data["name"]["first"]} {data["name"]["last"]}',
        'age': data['dob']['age'],
        'country': data['location']['country']
    }

def get_users(n: int) -> list:
    '''get n users from url
    
    Args:
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    users = [] # list of users
    while len(users) != n:
        user = get_randomuser()
        if user:
            if user['results'][0]['gender'] == 'male':
                users.append(get_user(user))

    return users
    
def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    users = get_users(n)
    with open(file_path, 'w') as f:
        users_json = json.dumps(users, indent=4)
        f.write(users_json)


write_users_to_file('users.json', 5)