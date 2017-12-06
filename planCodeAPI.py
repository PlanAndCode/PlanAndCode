from trelloAPI import Trello
from githubAPI import githubAPI

class planCodeAPI:
    def __init__(self, github_id="burakfurkanaksahin", password="software2017",organization_name="PlanAndCode",
                 trelloApiKey="6a4fe89f7b7bd584332a3cecf685d25b",trelloTOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4"):
        self.trello = Trello.Trello(apiKey=trelloApiKey,TOKEN=trelloTOKEN)
        self.github = githubAPI.GitHubAPI(github_id, password, organization_name)

    def trelloOrganizationList(self):
        self.trello.listOrganizations()

    def createTrelloOrganization(self,organizationName):
        self.trello.createOrganization(organizationName)

    def selectTrelloOrganization(self,organizationName):
        self.trello.selectOrganizationByName(organizationName)

    def createProject(self,projectName):
            if self.github.new_project(projectName, projectName, projectName):
                if(self.trello.organization!=None):
                    self.trello.createBoard(boardName=projectName,organizationID=self.trello.organization.id)
                else:
                    print("Organizasyon Seciniz !")

    def showProjects(self):
        return self.github.show_projects()

    def chooseProject(self,projectName):
        self.github.choose_project(projectName)
        self.trello.getBoardByName(projectName)

    def deleteProject(self):
        # We must verify if user really wants to delete a project!
        self.github.delete_project()
        self.trello.closeBoard()


    def showCommits(self):
        return self.github.show_project()


    # show board, lists, cards

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

    def showMembers(self):
        return_members = []
        return_members.append(self.github.list_members())
        # return_members.append(trello members)
        return return_members # 2 boyutlu array return_members[0] github memberları return_members[1] trello memberları


pc=planCodeAPI()
print(pc.showProjects())
pc.chooseProject("PlanAndCode")
print(pc.showCommits())
print(pc.showMembers())
