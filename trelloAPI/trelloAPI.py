
from trello import TrelloClient

class trello:
    def __init__(self,apiKey,TOKEN):
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


    def createBoard(self,board_name):
        # return name of board
        return self.client.add_board(board_name=board_name,source_board=None,organization_id=None,permission_level="private")

    def removeBoard(self,panoID):
        print("")



    def listMems(self):
        return self.client.list_organizations()

    def getBoard(self):
        print("")