#***************************************************************************************************************
#   libraries
#***************************************************************************************************************

import requests
import auth

#***************************************************************************************************************
#   class github will retrieve activity information from github repo
#***************************************************************************************************************

class github:
    def __init__(self, username, token):
        self.username = username
        self.token = token
    
    def getData(self):
        url = 'https://api.github.com/users/'+ self.username + '/events'
        head = {'Authorization': 'Bearer' + self.token}
        response = requests.get(url, headers=head)
        #Need to extract time data and save it to a smaller, organized json object
        print(url)
        return "I got It


#***************************************************************************************************************
#   script execution
#***************************************************************************************************************

if __name__ == "__main__":

    token = auth.github_access_token
    username = 'professorJordan'

    #instantiate a class object & run function
    Github = github(username, token)
    res = Github.getData()

    #output results
    print(res.json)
    print(res.text)
