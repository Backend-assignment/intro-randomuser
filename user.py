import requests
import json


def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'firstname': user firstname,
            'lastname': user lastname,
            'age': user age,
            'country': user country
        }
    '''
    firstname = user_data['results'][0]['name']['first']
    lastname = user_data['results'][0]['name']['last']
    age = user_data['results'][0]['dob']['age']
    country = user_data['results'][0]['nat']
    
    return {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'country': country
    }


def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    response = requests.get(url + f'?results={n}')
    users_data = json.loads(response.text)
    
    users = []
    for user_data in users_data['results']:
        users.append(get_user(user_data))
        
    return users
    

def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    url = 'https://randomuser.me/api/'
    users = get_users(url, n)
    
    with open(file_path, 'w') as file:
        for user in users:
            file.write(f"{user['firstname']} {user['lastname']}, {user['age']}, {user['country']}\n")




