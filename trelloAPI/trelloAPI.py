
from trello import TrelloClient

class trello:
    def __init__(self,apiKey,TOKEN):
        self.client = TrelloClient(
            api_key=apiKey,
            api_secret='your-secret',
            token=TOKEN,
            token_secret='your-oauth-token-secret'
        )

    def listPanos(self):
        all_boards = self.client.list_boards()
        last_board = all_boards[-1]
        print(last_board.name)




    def createPano(self):
        panoId="creaatePano"
        return panoId

    def removePano(self,panoID):
        print("")

    def getPanos(self):
        print("")