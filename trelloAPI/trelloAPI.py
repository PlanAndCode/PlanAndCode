
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

    def listTrello(self):
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


    def getBoard(self,boardName):
        all_boards = self.client.list_boards()
        for board in all_boards:
            if board.name==boardName:
                return board.id

    def createBoard(self,boardName,organizationID=None):
        # return name of board
        board = self.client.add_board(board_name=boardName,source_board=None,organization_id=organizationID,permission_level="private")

    def closeBoardName(self,boardName):
        all_boards = self.client.list_boards()
        for board in all_boards:
            if board.name==boardName:
                self.closeBoard(boardId=board.id)

    def closeBoard(self,boardId):
        url = "https://api.trello.com/1/boards/"+boardId+"?closed=true&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)
        return response.text

    ####### END BOARD OPERATIIONS


    ####### LIST OPERATIIONS

    def getList(self,listID,boardID):
        return self.client.get_board(board_id=boardID).get_list(list_id=listID)

    def createList(self,listName,boardID,num):
        board = self.client.get_board(boardID)
        board.add_list(list,num)

    def closeList(self,listID):
        url = "https://api.trello.com/1/lists/"+listID+"?closed=true&key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)
        return response.text

    ####### END LIST OPERATIIONS

    ####### CARD OPERATIIONS
    def getCard(self,cardID):
        self.client.get_card(card_id=cardID)

    def createCard(self,boardID,listID,cardName):
        self.getList(boardID=boardID,listID=listID).add_card(name=cardName,labels=None,due="",source=None,position=None)

    def removeCard(self,cardID):
        url = "https://api.trello.com/1/cards/"+cardID+"?key="+self.apiKey+"&token="+self.token
        querystring = {}
        response = requests.request("PUT", url, params=querystring)
        return response.text

    def moveCard(self,cardID,sourceListID,desListID):
        self.client.get_board("").get_list("").move(position=5)


    ####### END CARD OPERATIIONS

    #######  MEMBER OPERATIIONS

    def addMember(self,boardID,memberID):
        board = self.client.get_board(board_id=boardID)
        board.add_member(memberID)

    def listMems(self):
        return self.client.list_organizations()

    ####### END MEMBER OPERATIIONS