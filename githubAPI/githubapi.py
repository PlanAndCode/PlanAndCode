import github3
from github3 import login

class github:
    def __init__(self):
        print("github init")

    def login(self,id,password):
        g = github3.login(id,password)
        return g

    def createNewProject(self,login,projectName,projectURL,projectDescription):
        login.create_repo(projectName, projectURL, projectDescription, False, True, True, True, True)
        #Trello code

    def showProjects(self,login):
        for repo in login.iter_repos():
            print (repo)
        #Trello code

    def chooseProject(self,login,projectName):
        return login.repository(login.user(),projectName)
        #Trello code

    def currentProject(self,project):
        print (project)
        #Trello code

    def addMemberToOrganization(self,login,memberID):
        organization = self.getOrganization(login, "PlanAndCode")
        admin = self.getAdminTeam(login, organization, "Admin")
        admin.invite(memberID)
        for repo in login.iter_repos():
            repo.add_collaborator(memberID)

    def grantAccessToAllMembers(self,login):
        organization = self.getOrganization(login, "PlanAndCode")
        for repo in login.iter_repos():
            for member in organization.iter_members():
                repo.add_collaborator(member)

    def getOrganization(self,login,organizationName):
        return login.organization(organizationName)

    def getAdminTeam(self,g,organization,adminteamname):
        teams = organization.iter_teams();
        admin = None
        for team in teams:
            if team.name == adminteamname:
                admin = team
        return admin



    def main(self):
        github=login("<githubid>","<githubpassword>")
        project = self.chooseProject(github,"Project")
        self.currentProject(project)



