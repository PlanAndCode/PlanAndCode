"""
This example shows how to add new command to "Shell" build step
"""

from __future__ import print_function
from trelloAPI import Trello
from githubAPI import githubAPI

import sys
import json
import xml.etree.ElementTree as ET

import jenkins
import xmltodict

import request

class planCodeAPI:
    def __init__(self, github_id="burakfurkanaksahin", password="software2017",organization_name="PlanAndCode",
                 trelloApiKey="6a4fe89f7b7bd584332a3cecf685d25b",trelloTOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4"):
        self.trello = Trello.Trello(trelloApiKey,trelloTOKEN)
        self.github = githubAPI.GitHubAPI(github_id, password, organization_name)
        self.githubid = github_id
        self.githubpass = password
	

    def trelloOrganizationList(self):
        return self.trello.listOrganizations()

    def createTrelloOrganization(self,organizationName):
        return self.trello.createOrganization(organizationName)

    def selectTrelloOrganization(self,organizationName):
        return self.trello.selectOrganizationByName(organizationName)

    def createProject(self,projectName):
            #if self.github.new_project(projectName, projectName, projectName):
                if(self.trello.organizationID!=None):
                    self.trello.createBoard(boardName=projectName)
                else:
                    print("Organizasyon Seciniz !")

    def showProjects(self):
        return self.github.show_projects()

    def chooseProject(self,projectName):
        self.github.choose_project(projectName)
        self.trello.selectBoard(projectName)
        self.projectname=projectName

    def deleteProject(self):
        # We must verify if user really wants to delete a project!
        self.github.delete_project()
        self.trello.closeBoard()


    def showCommits(self):
        return self.github.show_project()


    # show board, lists, cards
    def showBoards(self):
        return self.trello.showBoards()

    def getTrelloToDoList(self):
        return self.trello.getToDoList()

    def getTrelloDoingList(self):
        return self.trello.getDoingList()

    def getTrelloBuildList(self):
        return self.trello.getBuildList()

    def getTrelloTestList(self):
        return self.trello.getTestList()
    def getTrelloDeployList(self):
        return self.trello.getDeployList()

    def getTrelloToDoCards(self):
        return self.trello.getToDoCards()

    def getTrelloDoingCards(self):
        return self.trello.getDoingCards()

    def getTrelloBuildCards(self):
        return self.trello.getBuildCards()

    def getTrelloTestCards(self):
        return self.trello.getTestCards()

    def getTrelloDeployCards(self):
        return self.trello.getDeployCards()

    def moveCard(self,cardID,destListID):
        self.trello.moveCard(cardID=cardID,desListID=destListID)


    def addMemberGitHub(self,member_name):
        self.github.add_member(member_name)


    def addMemberTrello(self,memberMail):
        self.trello.addMemberByMail(memberMail)

    def deleteMemberGitHub(self,member_name):
        self.github.delete_member(member_name)


    def deleteMemberTrello(self,memberID):
        return self.trello.deleteMember(memberID)

    def showTrelloMembers(self):
        return self.trello.showMembers()


    def createCard(self,boardID,listID,cardName):
        self.trello.createCard(boardID,listID,cardName)

    def addCommendToCard(self,cardID,commendText):
        self.trello.addCommendToCard(cardID,commendText)

    def showMembers(self):
        return_members = []
        return_members.append(self.github.list_members())
        # return_members.append(trello members)
        return return_members # 2 boyutlu array return_members[0] github memberları return_members[1] trello memberları

pc=planCodeAPI()

pc.chooseProject("PlanAndCode")



EMPTY_CONFIG_XML = '''<?xml version='1.0' encoding='UTF-8'?>
<project>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class='jenkins.scm.NullSCM'/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers class='vector'/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>

  <method_name></method_name>
  <github_login></github_login><!--Code-->
  <github_password></github_password><!--Code-->
  <repository_url></repository_url><!--Code&plan-->
  <project_name></project_name><!--Code&plan--><!--Build,Deployment-->
  <commit_id></commit_id><!--Code&plan--><!--Deployment-->
  <target_url></target_url><!--Code&plan--><!--Build,Test-->
  <card_id></card_id><!--Code-->

  <build_result></build_result><!--Build--><!--Code&plan(fail),Test(Pass)-->
  <build_result_detail></build_result_detail><!--Build--><!--Code&Plan(Fail)-->
  <test_result></test_result><!--Test--><!--Deployment(Pass), Code&plan(Fail)-->
  <test_result_detail></test_result_detail>
  <deploy_result></deploy_result>
  <deploy_result_detail></deploy_result_detail>
  <object_type></object_type>

</project>'''

TEST_JSON_RES = '''{  "$schema": "http://json-schema.org/draft-04/schema#",
       "title": "Response information",
       "type": "object",
       "description": "Contains operation(method) and its execution status with description",
       "properties": {
         "object_type": "tmp",
         "operation": "Build",
         "status": "TRUE",
         "description": "tmp",
         "project_name": "son",
		 "user_id": "gtusoftware2017",
		 "user_pass": "software2017",
		 "repository_url": "www.github.com/GtuDevOps/son",
         "method_name" : "move"
       }
}'''


def main_function(json_file):
	split_str = TEST_JSON_RES.split(',') #sys.argv[1].split(',')
	operation = ""
	status = ""
	description = ""
	project_name = ""
	user_id = ""
	user_pass = ""
	repository_url = ""
	method_name = ""

	for x in range(0, 13):
		if "operation" in split_str[x]:
			operation = split_str[x].strip()
			operation = operation.replace("operation","").replace(":","").replace('"','').replace(" ","")

		if "status" in split_str[x]:
			status = split_str[x].strip()
			status = status.replace("status","").replace(":","").replace('"','').replace(" ","")

		if "description" in split_str[x]:
			description = split_str[x].strip()
			description = description.replace("description","").replace(":","").replace('"','').replace(" ","")

		if "project_name" in split_str[x]:
			project_name = split_str[x].strip()
			project_name = project_name.replace("project_name","").replace(":","").replace('"','').replace(" ","")

		if "user_id" in split_str[x]:
			user_id = split_str[x].strip()
			user_id = user_id.replace("user_id","").replace(":","").replace('"','').replace(" ","")

		if "user_pass" in split_str[x]:
			user_pass = split_str[x].strip()
			user_pass = user_pass.replace("user_pass","").replace(":","").replace('"','').replace(" ","")

		if "repository_url" in split_str[x]:
			repository_url = split_str[x].strip()
			repository_url = repository_url.replace("repository_url","").replace(":","").replace('"','').replace(" ","")
			repository_url = repository_url.split("/")[1]

		if "method_name" in split_str[x]:
			method_name = split_str[x].strip()
			method_name = method_name.replace("method_name","").replace(":","").replace('"','').replace(" ","")


	print("LOGIN: " + user_id + " " + user_pass + " " + repository_url)
	pc=planCodeAPI(user_id, user_pass, repository_url)
	print("SELECTING PROJECT: " + project_name)
	pc.chooseProject(project_name)


main_function(TEST_JSON_RES)
