
import github3

class GHApi:
    def __init__(self, githubid, password, organizationname):
        try:
            self.github=github3.login(githubid,password)
            self.organizationName = None
            if type(self.getOrganization(organizationname)) == type(None):
                print( "There is no organization named:  " + organizationname + "\n Please create in your Github Account!")
            else:
                self.organizationName = organizationname
                self.organization = self.getOrganization(organizationname)
                self.admin = self.getAdminTeam()
        except github3.GitHubError:
            print ("Please check GitHubID and/or GitHubPassword!")
    
    
    ################################################################
    #            PROJECT OPERATIONS                                #
    ################################################################
    def createNewProject(self, projectName, projectURL, projectDescription):
        try:
            self.github.create_repo(projectName, projectURL, projectDescription, False, True, True, True, True)
        except github3.GitHubError:
            print("Please check name of Repository. There is an exist repository named " + projectName)

            
    def deleteProject(self,projectName):
        project = self.github.repository(self.github.user(),projectName).delete()
        if project is None:
            print ("There is no project named " + projectName + "\nPlease select from these projects:")
            self.showProjects()
        return project
        

    def showProjects(self):
        for repo in self.github.iter_repos():
            print (repo)

    def chooseProject(self, projectName):
        project = self.github.repository(self.github.user(),projectName)
        if project is None:
            print ("There is no project named " + projectName + "\nPlease select from these projects:")
            self.showProjects()
        return project

    def currentProject(self, project):
        print (project)
    
    ##################################################################
    #                       MEMBER OPERATIONS                        #
    ##################################################################
    def addMemberToOrganization(self, memberID):
        self.admin.invite(memberID)
        for repo in self.github.iter_repos():
            repo.add_collaborator(memberID)

    def deleteMemberFromOrganization(self, memberID):
        self.admin.remove_member(memberID)
        for repo in self.github.iter_repos():
            repo.remove_collaborator(memberID)

    def grantAccessToAllMembers(self):
        for repo in self.github.iter_repos():
            for member in self.organization.iter_members():
                repo.add_collaborator(member)

    def getOrganization(self,organizationName):
        return self.github.organization(organizationName)

    def getAdminTeam(self):
        teams = self.organization.iter_teams();
        admin = None
        for team in teams:
            if team.name == "Admin":
                admin = team
        if admin is None:
            repo_names=['None']
            self.organization.create_team("Admin",repo_names,"admin")
        return admin
    
    def listMembers(self,username,projectname):
        for memb in self.github.repository(username,projectname).iter_collaborators():
            print memb
            
            
    def listAllActivities(self,username,projectname):
        for activity in self.github.repository(username, projectname).iter_commits():
            print activity
            
def main():
    deneme = GHApi("<githubid>","<githubpassword>","<organizationname>")
    if deneme.organizationName is None:
        exit(1)
    else:
        deneme.showProjects()
        project = deneme.chooseProject("Project")
        deneme.listMembers("PlanAndCode","PlanAndCode")
        deneme.listActivity("PlanAndCode","PlanAndCode")
        print ("----------------")
        print (project)





