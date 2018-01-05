from .trelloAPI import trello


class Trello:
    def __init__(self,apiKey,token):
        self.trelloAPI = trello(apiKey, token)
        self.board=None
        self.organizationID=None

    def createOrganization(self,organizationName):
        self.organizationID = self.trelloAPI.createOrganization(organizationName)

    def listOrganizations(self):
        return self.trelloAPI.listOrganizations()


    def selectOrganizationByID(self,organizationID):
        return self.trelloAPI.getOrganization(organizationID=organizationID)

    def selectOrganizationByName(self,organizationName):
        # return Organization or None
        self.organizationID = self.trelloAPI.getOrganizationByName(organizationName=organizationName).id
        if self.organizationID==None:
            return False
        return True

    def createBoard(self,boardName):
        self.board = self.trelloAPI.createBoard(boardName,self.organizationID)
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
        if(self.organizationID==None or self.board==None):
            return False # select board and organization
        self.trelloAPI.addOrganizationMember(self.organizationID,memberMail,"admin")
        organizationMembers = self.trelloAPI.getOrganization(self.organizationID).get_members()
        organizationMembers.pop(-1).username
        for mem in organizationMembers:
            self.board.add_member(mem)
        return True

    def addMemberByID(self,memberID):
        if self.board!=None:
            self.board.add_member(self.trelloAPI.client.get_member(memberID))
            return True
        return False

    def deleteMember(self,memberID):
        self.trelloAPI.removeOrganizationMember(self.organizationID,memberID)





    def showMembers(self):
        if(self.board!=None):
            return self.board.get_members()


    def showBoardActions(self):
        return self.trelloAPI.getBoard(self.board.id).actions




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

    def createCard(self,boardID,listID,cardName):
        self.trelloAPI.createCard(boardID,listID,cardName)

    def deleteCard(self,cardID):

        self.trelloAPI.removeCard(cardID)


    def addCommendToCard(self,cardID,commendText):
        self.trelloAPI.addCommendToCard(cardID,commendText)
    
    def moveCard3(self,cardID,destListID):

        self.trelloAPI.moveCard2(cardID=cardID,desListID=destListID)














