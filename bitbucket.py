#***************************************************************************************************************
#   libraries
#***************************************************************************************************************

import requests
import auth

#***************************************************************************************************************
#   class bitbucket will retrieve activity information from bitbucket repo
#***************************************************************************************************************

class bitbucket:
    def __init__(self, username, token):
        self.username = username
        self.token = token
       

    def getData(self):
        url="https://api.bitbucket.org/2.0/users/{user}/{emails}"
        #url = "https://api.bitbucket.org/2.0/user/emails/"+self.username+
        #url = 'https://api.bitbucket.org/2.0/users/'+ self.username + '/emails '
        #url = "https://api.bitbucket.org/2.0/user/emails"
        
        head = {'Authorization': 'Bearer' + self.token}
        #response = requests.get(url, headers=head)
        response = requests.request(
         "GET",
         url,
         headers=head
        )
        
        #Need to extract time data and save it to a smaller, organized json object
        print(url)
        return response


#***************************************************************************************************************
#   script execution
#***************************************************************************************************************

if __name__ == "__main__":

    token = auth.bitbucket_access_token
    username = 'Prathyusha_Rayapati'

    #instantiate a class object & run function
    Bitbucket = bitbucket(username, token)
    res = Bitbucket.getData()
    print(res)
    #print(Bitbucket.getData.text)