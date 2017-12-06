
from trello import TrelloClient
import requests
import json

class trello:
    def __init__(self,apiKey,TOKEN):
        self.apiKey=apiKey
        self.token=TOKEN
        self.client = TrelloClient(
            api_key=apiKey,
            api_secret='your-secret',
            token=TOKEN,
            token_secret='your-oauth-token-secret'
        )


    def printTrello(self):
        all_boards = self.client.list_boards()
        last_board = all_boards[-1]
        print("Boards ")

        for board in all_boards:
            print("Board Name :",board.name," Board ID",board.id)
            for list in board.all_lists():
                print("\t","ListName :",list.name ,"listID :",list.id)
                for card in list.list_cards(""):
                    print("\t\t","cardName :",card.name ,"cardID :",card.id)

                    #for card in board.all_cards():
                    #   print("\tCard Name :",card.name," Card ID",card.id)
                ####### BOARD OPERATIONS

    def getBoard(self,boardID):
        self.board=self.client.get_board(board_id=boardID)
        return self.board

    def getBoardByName(self,boardName):
        all_boards = self.client.list_boards()
        for board in all_boards:
            if board.name==boardName:
                self.board=board
                return board
        return None;

    # close all boards
    def clearBoards(self):
        for board in self.client.list_boards():
            board.close()

    def createBoard(self,boardName,organizationID=None,permission_level="private"):
        self.board = self.client.add_board(board_name=boardName,source_board=None,organization_id=organizationID,permission_level=permission_level)
        for list in self.board.get_lists(None):
            self.board.get_list(list.id).close()
        self.createList("To Do:",self.board.id,1)
        self.createList("Doing:",self.board.id,2)
        self.createList("Build:",self.board.id,3)
        self.createList("Test:",self.board.id,4)
        self.createList("Deploy:",self.board.id,5)
        return self.board

    def closeBoardByName(self,boardName=None):
        if boardName!=None:
            all_boards = self.client.list_boards()
            for board in all_boards:
                if board.name==boardName:
                    return board.close()
        else:
            if self.board!=None:
                self.closeBoard(self.board.id);


    def closeBoard(self,boardId=None):
        if boardId!=None:
            return self.getBoard(boardID=boardId).close()
        else:
            if self.board!=None:
                self.board.close();
            else:
                return None;

    def boardList(self):
        return self.client.list_boards()
    ####### END BOARD OPERATIONS


    ####### LIST OPERATIONS

    def getList(self,listID,boardID):
        return self.client.get_board(board_id=boardID).get_list(list_id=listID)

    def getListByName(self,listID,boardID):
        return self.client.get_board(board_id=boardID).get_list(list_id=listID)

    def createList(self,listName,boardID,sira=None):
        board = self.client.get_board(boardID)
        addedlist= board.add_list(listName,sira)
        return addedlist

    def closeList(self,listID,boardID):
        return self.client.get_board(boardID).get_list(listID).close()

    def closeJustListID(self,listID): # unsafe
        url = "https://api.trello.com/1/lists/"+listID+"?closed=true&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)
        return response.text

    ####### END LIST OPERATIONS

    ####### CARD OPERATIONS

    def getCard(self,cardID):
        return self.client.get_card(card_id=cardID)

    def createCard(self,boardID,listID,cardName):
        self.getList(boardID=boardID,listID=listID).add_card(name=cardName,labels=None,due="",source=None,position=None)

    def removeCard(self,cardID):
        url = "https://api.trello.com/1/cards/"+cardID+"?key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)
        return response.text

    def moveCard(self,cardID,desListID):
        self.getCard(cardID=cardID).change_list(list_id=desListID)


    ####### END CARD OPERATIONS

    #######  TEAM MEMBER OPERATIONS

    def addMemberBoard(self,boardID,memberID):
        board = self.client.get_board(board_id=boardID)
        board.add_member(memberID)






    # ORGANIZATION OPERATIONS

    def getOrganization(self,organizationID):
        return self.client.get_organization(organizationID)

    def getOrganizationByName(self,organizationName):
        for organization in  self.listOrganizations():
            if organization.name=="":
                return organization
        return None;

    def listOrganizations(self):
        self.client.list_organizations()
        return self.client.list_organizations();

    def createOrganization(self,organizationName):
        url = "https://api.trello.com/1/organizations?displayName="+organizationName+"&desc="+organizationName+"&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("POST", url, params=querystring)
        organizationID=str.split(response.text,",")[0].split("\"")[3]
        return organizationID


    def addOrganizationMember(self,organizationID,mail,memberType="normal",fullName="member"):
        configuredMail=str.replace(mail,"@","%40")
        url = "https://api.trello.com/1/organizations/"+organizationID+"/members?email="+configuredMail+"&fullName="+fullName+"&type="+memberType+"&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)

        data = (json.loads(response.text))
        memberID = (data["memberships"][-1]["idMember"])
        return memberID

    def removeOrganizationMember(self,organizationID,memberID):
        url = "https://api.trello.com/1/organizations/"+organizationID+"/members/"+memberID+"?key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("DELETE", url, params=querystring)
        return response.text

    def removeOrganization(self,organizationID):
        url = "https://api.trello.com/1/organizations/"+organizationID+"?key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("DELETE", url, params=querystring)
        return response.text



        ####### END MEMBER OPERATIONS