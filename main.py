########## IMPORT AREA #########
from trelloAPI import trelloAPI
from githubAPI import githubapi

from trello import TrelloClient



############# MAIN AREA ########



github = githubapi.github()
#github.main()



trello = trelloAPI.trello(apiKey="6a4fe89f7b7bd584332a3cecf685d25b",TOKEN="0c54fb091e9723f7696bbb2a9cdd405741d7b67ad2deeb9d653afe009c2a61a9")
print(trello.createPano())
print("test2")




