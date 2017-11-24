import github3
from github3 import login

def login(id,password):
    g = github3.login(id,password)
    return g

def createNewProject(login,projectName,projectURL,projectDescription):
    login.create_repo(projectName, projectURL, projectDescription, False, True, True, True, True)
    #Trello code

def showProjects(login):
    for repo in login.iter_repos():
        print (repo)
    #Trello code

def chooseProject(login,projectName):
    return login.repository(login.user(),projectName)
    #Trello code

def currentProject(project):
    print (project)
    #Trello code

def addMemberToOrganization(login,memberID):
    organization = getOrganization(login, "PlanAndCode")
    admin = getAdminTeam(login, organization, "Admin")
    admin.invite(memberID)
    for repo in login.iter_repos():
        repo.add_collaborator(memberID)

def grantAccessToAllMembers(login):
    organization = getOrganization(login, "PlanAndCode")
    for repo in login.iter_repos():
        for member in organization.iter_members():
            repo.add_collaborator(member)

def getOrganization(login,organizationName):
    return login.organization(organizationName)

def getAdminTeam(g,organization,adminteamname):
    teams = organization.iter_teams();
    admin = None
    for team in teams:
        if team.name == adminteamname:
            admin = team
    return admin



def main():
    github=login("<githubid>","<githubpassword>")
    project = chooseProject(github,"Project")
    currentProject(project)


main()