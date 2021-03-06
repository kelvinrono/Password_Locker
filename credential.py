class Credentials:
    
    credential_details = [] #initialize an array to store the credential details

    def __init__(self,credentials_account, credentials_username, credentials_password):
        '''
        This will initialize the credentials details required for the credentials class
        '''
        self.credentials_account = credentials_account
        self.credentials_username = credentials_username
        self.credentials_password = credentials_password

    def save_credentials(self):
        '''
        Save the credentials of a user
        '''
        Credentials.credential_details.append(self)

    def delete_credentials(self):
        """
        delete saved credentials in the credentials list
        """
        Credentials.credential_details.remove(self)

  
    @classmethod
    def display_credentials(cls):
            return cls.credential_details

    
    @classmethod
    def find_by_username(cls,account):
        '''
        this method takes in usernmame and returns a password that match that number 
        Args:
        account: password number to search for
        Returns :
        password of person that matches the number.
        '''
        for credential in cls.credential_details:
            if(credential.credentials_username == account):
                return credential

       

