#***************************************************************************************************************
#   libraries
#***************************************************************************************************************
import json
import auth

import bitbucket
from github import github
import launchpad
import sourceforage
import beanstalk
import githubActions
import jenkins
import circleCI
import gitlab

#***************************************************************************************************************
#   class collect will retrieve activity data from sources for which there is a known user account.
#   It expects to receive a dictionary containing key-value pairs. For each key-value pair for which
#   there is an associated username:
#       1. call class, pass username and auth tokens to class
#       2. Initiate function to collect activity data
#       3. append data to a JSON object
#   It will return JSON object 
#***************************************************************************************************************

class collect:
    def __init__(self, sitesUserNames):
        self.sitesUserNames = sitesUserNames
        self.data = {}

    def getData(self):
        #for each site with a known username:
        for site in self.sitesUserNames:
            if self.sitesUserNames.get(site):
                username = self.sitesUserNames.get(site)
                
                #find matching class:
                if site == 'bitbucket':
                    collect._bitbucket(self, username)
        print(self.data)

    def _bitbucket(self, username):
        #setup the class
        token = auth.github_access_token
        bitbucket = bitbucket(username, token)
        #collect the data
        res = bitbucket.getData()
        #if result then save the results
        if res != '':
            dict = {'bitbucket': res.text}
            self.data.update(dict)


            


#***************************************************************************************************************
#   script execution
#***************************************************************************************************************

if __name__ == "__main__":

    sitesUserNames = {
        'github':'professorJordan',
        'bitbucket':'Prathyusha_Rayapati',
        'launchpad':'',
        'sourceforage':'',
        'beanstalk':'',
        'githubActions':'professorJordan',
        'jenkins':'',
        'circleCI':'',
        'gitLab':''}

    Collect = collect(sitesUserNames)
    Collect.getData()