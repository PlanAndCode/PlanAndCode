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
        return self.github.show_projects()

    def chooseProject(self,projectName):
        self.github.choose_project(projectName)
        self.trello.getBoardByName(projectName)

    def deleteProject(self):
        # We must verify if user really wants to delete a project!
        self.github.delete_project()
        self.trello.closeBoard()


    def showCommits(self):
        return self.github.show_project()


    # show board, lists, cards

    def addMemberGitHub(self,member_name):
        self.github.add_member(member_name)

    #add member trello


    def deleteMemberGitHub(self,member_name):
        self.github.delete_member(member_name)

    #delete_member Trello

    def showMembers(self):
        return_members = []
        return_members.append(self.github.list_members())
        # return_members.append(trello members)
        return return_members # 2 boyutlu array return_members[0] github memberları return_members[1] trello memberları


pc=planCodeAPI()
print(pc.showProjects())
pc.chooseProject("PlanAndCode")
print(pc.showCommits())
print(pc.showMembers())
