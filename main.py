########## IMPORT AREA #########
from trelloAPI import trelloAPI
from githubAPI import githubapi

from trello import TrelloClient



############# MAIN AREA ########



github = githubapi.github()
#github.main()



trello = trelloAPI.trello(apiKey="6a4fe89f7b7bd584332a3cecf685d25b",TOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4")
#print(trello.createBoard("bordAPI"))
trello.listTrello()
#trello.closeBoardName("bordAPI")

#trello.addMember()
print( trello.listMems())



