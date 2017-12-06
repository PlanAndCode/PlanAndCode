from trelloAPI import trelloAPI

class Trello:
    def __init__(self,apiKey,token):
        self.trelloAPI = trelloAPI.trello(apiKey,token)
        self.board=None
        self.organization=None

    def createOrganization(self,organizationName):
        self.organization = self.trelloAPI.createOrganization(organizationName)

    def selectOrganization(self,organizationName):
        # return Organization or None
        self.organization= self.trelloAPI.getOrganizationByName(organizationName=organizationName)
        if self.organization==None:
            return False
        return True

    def createBoard(self,boardName):
        self.board = self.trelloAPI.createBoard(boardName)
        return True

    def selectBoard(self,boardName):
        self.board = self.trelloAPI.getBoardByName(boardName)
        if self.board==None:
            return False
        return True

    def showBoards(self):
        boardList = self.trelloAPI.boardList()
        return boardList

    def closeBoard(self):
        if self.board!=None:
            self.board.close();
            return True;
        return False;

    def addMemberByMail(self,memberMail):
        if(self.organization==None or self.board==None):
            return False # select board and organization
        self.trelloAPI.addOrganizationMember(self.organization.id,memberMail,"admin")
        organizationMembers = self.trelloAPI.getOrganization(self.organization.id).get_members()
        organizationMembers.pop(-1).username
        for mem in organizationMembers:
            self.board.add_member(mem)
        return True

    def addMemberByID(self,memberID):
        if self.board!=None:
            self.board.add_member(self.trelloAPI.client.get_member(memberID))
            return True
        return False

    def getToDoList(self):
        if( self.board!=None):
            return self.board.get_lists(None)[0]

    def getDoingList(self):
        if( self.board!=None):
            return self.board.get_lists(None)[1]

    def getBuildList(self):
        if( self.board!=None):
            return self.board.get_lists(None)[2]

    def getTestList(self):
        if( self.board!=None):
            return self.board.get_lists(None)[3]

    def getDeployList(self):
        if( self.board!=None):
            return self.board.get_lists(None)[4]


    def getToDoCards(self):
        if( self.board!=None):
            return self.board.get_lists(None)[0].list_cards()

    def getDoingCards(self):
        if( self.board!=None):
            return self.board.get_lists(None)[1].list_cards()

    def getBuildCards(self):
        if( self.board!=None):
            return self.board.get_lists(None)[2].list_cards()

    def getTestCards(self):
        if( self.board!=None):
            return self.board.get_lists(None)[3].list_cards()

    def getDeployCards(self):
        if( self.board!=None):
            return self.board.get_lists(None)[4].list_cards()

    
    def moveCard(self,cardID,destListID):
        self.trelloAPI.moveCard(cardID=cardID,desListID=destListID)












