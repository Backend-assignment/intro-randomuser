import requests


class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'

    def get_randomuser(self) -> dict:
        '''get full data from randomuser
        
        Returns:
            dict: full data
        '''
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return Exception('Request to randomuser API failed with status code {}'.format(response.status_code))
    
    def get_cell(self) -> str:
        '''get user cell from randomuser
        
        Returns:
            str: user cell
        '''
        user = self.get_randomuser()
        return user['results'][0]['cell']
    def get_city(self) -> str:
        '''get user city from randomuser
        
        Returns:
            str: user city
        '''
        user = self.get_randomuser()
        return user['results'][0]['location']['city']
    
    def get_dob(self) -> dict:
        '''get user dob from randomuser
        
        Returns:
            dict: user dob
        '''
        user = self.get_randomuser()
        return user['results'][0]['dob']
        
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        user = self.get_randomuser()
        return user['results'][0]['email']
  
    def get_first_name(self) -> str:
        '''get user first name from randomuser
        
        Returns:
            str: user first name
        '''
        user = self.get_randomuser()
        return user['results'][0]['name']['first']
    
    def get_last_name(self) -> str:
        '''get user last name from randomuser
        
        Returns:
            str: user last name
        '''
        user = self.get_randomuser()
        return user['results'][0]['name']['last']
    
    def get_full_name(self) -> str:
        '''get user full name from randomuser
        
        Returns:
            str: user full name
        '''
        user = self.get_randomuser()
        return user['results'][0]['name']['title'] + ' ' + user['results'][0]['name']['first'] + ' ' + user['results'][0]['name']['last']

    
    def get_gender(self) -> str:
        '''get user gender from randomuser
        
        Returns:
            str: user gender
        '''
        user = self.get_randomuser()
        return user['results'][0]['gender']
    
    def get_id(self) -> dict:
        '''get user id from randomuser
        
        Returns:
            dict: user id
        '''
        user = self.get_randomuser()
        return user['id']
    
    def get_id_number(self) -> str:
        '''get user id number from randomuser
        
        Returns:
            str: user id number
        '''
        data = self.get_id()
        return data['value']
    
    def get_info(self) -> dict:
        '''get user info from randomuser
        
        Returns:
            dict: user info
        '''
        data = self.get_randomuser()
        return data['info']
    
    def get_nat(self) -> str:
        '''get user nat from randomuser
        
        Returns:
            str: user nat
        '''
        data = self.get_randomuser()
        return data['nat']
    
    def get_picture(self) -> dict:
        '''get user picture from randomuser
        
        Returns:
            dict: user picture
        '''
        data = self.get_randomuser()
        return data['picture']


randomuser = RandomUser()
print(randomuser.get_randomuser())
print(randomuser.get_picture())