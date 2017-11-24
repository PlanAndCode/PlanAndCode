########## IMPORT AREA #########
from trelloAPI import trelloAPI
from githubAPI import githubapi




############# MAIN AREA ########



github = githubapi.github()
#github.main()



trello = trelloAPI.trello("asdasd","asdasd")
print(trello.createPano())
print("test2")




