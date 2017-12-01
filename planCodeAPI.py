
from trelloAPI import trelloAPI
from githubAPI import githubAPI

class planCodeAPI:
    def __init__(self, github_id="burakfurkanaksahin", password="software2017",organization_name="PlanAndCode",
                 trelloApiKey="6a4fe89f7b7bd584332a3cecf685d25b",trelloTOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4"):
        self.trello = trelloAPI.trello(apiKey=trelloApiKey,TOKEN=trelloTOKEN)
        self.github = githubAPI.GitHubAPI(github_id, password, organization_name)

    def createProject(self,projectName):
        if self.github.new_project(projectName, projectName, projectName):
            self.trello.createBoard(boardName=projectName)


    def showProjects(self):
        self.github.show_projects()

    def chooseProject(self,projectName):
        self.github.choose_project(projectName)
        self.trello.getBoardWithName(projectName)

pc=planCodeAPI()
pc.trello.clearBoards()

pc.createProject("testProject5")
pc.showProjects()