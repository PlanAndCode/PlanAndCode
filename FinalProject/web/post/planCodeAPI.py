from .Trello import Trello
from .githubAPI import GitHubAPI

class planCodeAPI:
    def __init__(self, github_id="burakfurkanaksahin", password="software2017",organization_name="PlanAndCode",
                 trelloApiKey="6a4fe89f7b7bd584332a3cecf685d25b",trelloTOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4"):
        self.trello = Trello(trelloApiKey,trelloTOKEN)
        self.github = GitHubAPI(github_id, password, organization_name)

    def trelloOrganizationList(self):
        return self.trello.listOrganizations()

    def createTrelloOrganization(self,organizationName):
        return self.trello.createOrganization(organizationName)

    def selectTrelloOrganization(self,organizationName):
        return self.trello.selectOrganizationByName(organizationName)

    def createProject(self,projectName):
                self.github.new_project(projectName, projectName, projectName)
                if(self.trello.organizationID!=None):
                    self.trello.createBoard(boardName=projectName)
                else:
                    print("Organizasyon Seciniz !")

    def showProjects(self):
        return self.github.show_projects()

    def chooseProject(self,projectName):
        self.github.choose_project(projectName)
        self.trello.selectBoard(projectName)

    def deleteProject(self):
        # We must verify if user really wants to delete a project!
        self.github.delete_project()
        self.trello.closeBoard()


    def showCommits(self):
        return self.github.show_project()


    # show board, lists, cards
    def showBoards(self):
        return self.trello.showBoards()

    def getTrelloToDoList(self): # id name
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

    def getTrelloToDoCardsString(self):
        str=""
        for x in self.getTrelloToDoCards():
            str+=x.id+" "+x.name+"\n"
        return str



    def getTrelloDoingCards(self):
        return self.trello.getDoingCards()

    def getTrelloDoingCardsString(self):
        str=""
        for x in self.getTrelloDoingCards():
            str+=x.id+" "+x.name+"\n"
        return str

    def getTrelloBuildCards(self):
        return self.trello.getBuildCards()

    def getTrelloBuildCardsString(self):
        str=""
        for x in self.getTrelloBuildCards():
            str+=x.id+" "+x.name+"\n"
        return str



    def getTrelloTestCards(self):
        return self.trello.getTestCards()

    def getTrelloTestCardsString(self):
        str=""
        for x in self.getTrelloTestCards():
            str+=x.id+" "+x.name+"\n"
        return str



    def getTrelloDeployCards(self):
        return self.trello.getDeployCards()

    def getTrelloDeployCardsString(self):
        str=""
        for x in self.getTrelloDeployCards():
            str+=x.id+" "+x.name+"\n"
        return str


    def sendSignalBuildComplated(self):
        if len(self.getTrelloToDoCards())<1 and len(self.getTrelloDoingCards())<1:
            print("GOnder Signal Codelari")



    def moveCard(self,cardID,destListID):
        self.trello.moveCard3(cardID,destListID)
        if destListID==self.getTrelloBuildList().id:
            self.sendSignalBuildComplated()

    def deleteCard(self,cardID):
        self.trello.trelloAPI.removeCard(cardID)


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


    def createCard(self,listID,cardName):
        self.trello.createCard(self.trello.board.id,listID,cardName)



    def moveAllCardToList(self,listID):
        for x in self.trello.board.all_cards():
            self.moveCard(x.id,listID)



    def moveAllCardToDOING(self):
        self.moveAllCardToList(self.getTrelloDoingList().id)

    def moveAllCardToTEST(self):
        self.moveAllCardToList(self.getTrelloTestList().id)

    def moveAllCardToDEPLOY(self):
        self.moveAllCardToList(self.getTrelloDeployList().id)


    def deleteCard(self,cardID):

        self.trello.deleteCard(cardID)

    def addCommendToCard(self,cardID,commendText):
        self.trello.addCommendToCard(cardID,commendText)

    def showMembers(self):
        return_members = []
        return_members.append(self.github.list_members())
        # return_members.append(trello members)
        return return_members # 2 boyutlu array return_members[0] github memberları return_members[1] trello memberları




