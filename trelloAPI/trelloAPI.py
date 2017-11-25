
from trello import TrelloClient
import requests

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



####### BOARD OPERATIIONS

    def getBoard(self,boardID):
        return self.client.get_board(board_id=boardID)

    def getBoardWithName(self,boardName):
        all_boards = self.client.list_boards()
        for board in all_boards:
            if board.name==boardName:
                return board

    def createBoard(self,boardName,organizationID=None):
        board = self.client.add_board(board_name=boardName,source_board=None,organization_id=organizationID,permission_level="private")
        return board

    def closeBoardWithName(self,boardName):
        all_boards = self.client.list_boards()
        for board in all_boards:
            if board.name==boardName:
                return board.close()

    def closeBoard(self,boardId):
        return self.getBoard(boardID=boardId).close()

    def boardList(self):
        return self.client.list_boards()
    ####### END BOARD OPERATIIONS


    ####### LIST OPERATIIONS

    def getList(self,listID,boardID):
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

    ####### END LIST OPERATIIONS

    ####### CARD OPERATIIONS

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


    ####### END CARD OPERATIIONS

    #######  TEAM MEMBER OPERATIIONS

    def addMember(self,boardID,memberID):
        board = self.client.get_board(board_id=boardID)
        board.add_member(memberID)

    def listMems(self):
        return self.client.list_organizations()

    def createOrganization(self,organizationName):
        url = "https://api.trello.com/1/organizations?displayName="+organizationName+"&desc="+organizationName+"&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("POST", url, params=querystring)
        organizationID=str.split(response.text,",")[0].split("\"")[3]
        return organizationID




    ####### END MEMBER OPERATIIONS