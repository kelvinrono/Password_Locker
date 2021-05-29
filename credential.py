class Credentials:
    
    credential_details = [] #initialize an array to store the credential details

    def __init__(self, username, password):
        '''
        This will initialize the credentials details required for the credentials class
        '''
        self.credentials_username = username
        self.credentials_password = password

    def save_credentials(self):
        '''
        Save the credentials of a user
        '''
        Credentials.credential_details.append(self)
