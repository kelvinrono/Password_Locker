from credential import Credentials
from user import User
import unittest # Importing the unittest module
class TestCredential(unittest.TestCase):

    def setUp(self):
          
        
            self.new_credentials = Credentials('Facebook', 'kelvinrono', '12345')
    def test_init(self):

            '''
            This is a test that confirm that the objects 
            in the credentials cass have been initialized properly
            '''
            self.assertEqual(self.new_credentials.credentials_account, "Facebook")
            self.assertEqual(self.new_credentials.credentials_username, "kelvinrono")
            self.assertEqual(self.new_credentials.credentials_password, "12345")
    
    # def setUp(self):
    #    self.new_user = User('Kelvin', 'Rono', 'kevo', 1234)
    # def test_init(self):

    #         '''
    #         This is a test that confirm that the objects 
    #         in the credentials cass have been initialized properly
    #         '''
    #         self.assertEqual(self.new_user.firstName, "Facebook")
    #         self.assertEqual(self.new_user.lastName, "kelvinrono")
    #         self.assertEqual(self.new_user.username, "kevo")
    #         self.assertEqual(self.new_user.password, 1234)
    
      
    def test_save_credentials(self):
            '''
            This is a test than run and check if the contact has been 
            actually saved
            '''
            self.new_credentials.save_credentials()
            self.assertEqual(len(Credentials.credential_details), 1)

    
    # def test_save_user(self):
    #         '''
    #         This is a test than run and check if the contact has been 
    #         actually saved
    #         '''
    #         self.new_credentials.save_credentials()
    #         self.assertEqual(len(Credentials.credential_details), 1)

    def tearDown(self):
        Credentials.credential_details = []

    def test_delete_credential(self):
            """
            test method to test if we can remove an account credentials from our credentials_list
            """
            self.new_credentials.save_credentials()
            test_credentials = Credentials('Twitter','djchep','12343')
            test_credentials.save_credentials()
            
            
            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credential_details),1)

    


if __name__ == '__main__':
    unittest.main()