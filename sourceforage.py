#***************************************************************************************************************
#   libraries
#***************************************************************************************************************

import requests
import auth

#***************************************************************************************************************
#   class bitbucket will retrieve activity information from bitbucket repo
#***************************************************************************************************************

class sourceforage:
    def __init__(self, username, token):
        self.username = username
        self.token = token
       

    def getData(self):
        url="https://sourceforage.net/rest/u/"+self.username+"/sessions/"
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

    token = auth.sourceforage_access_token
    username = 'platform-sec'

    #instantiate a class object & run function
    Sourceforage = sourceforage(username, token)
    res = Sourceforage.getData()
    print(res.text)