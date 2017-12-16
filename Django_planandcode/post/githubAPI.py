import github3


class GitHubAPI:
    def __init__(self, github_id, password, organization_name):
        try:
            self.github = github3.login(github_id,password)
            self.organization = self.github.organization(organization_name)
            self.organization_name = organization_name
            if self.organization is None:
                print("There is no organization named:  " + organization_name +
                      "\nPlease create in your Github Account!")
            else:
                self.username = github_id
                self.admin = self.admin_team()
                self.project = None
        except github3.GitHubError:
            print("Please check GitHubID and/or GitHubPassword!")

    ################################################################
    #            PROJECT OPERATIONS                                #
    ################################################################
    def new_project(self, name, url, description):
        try:
            self.project = self.organization.create_repo(name,description,url,False,True,True,True,self.admin.id,True)
        except github3.GitHubError:
            print("Please check name of Project. There is an exist project named " + name)

    def choose_project(self, name):
        self.project = self.github.repository(self.organization_name,name)
        if self.project is None:
            print("There is no project named " + name + "\nPlease select from these projects:")
            self.show_projects()

    def show_project(self):
        try:
            if self.project is None:
                print("Please select from these projects to work on it")
                self.show_projects()
            else:
                #print(self.project)
                return self.list_activity()
        except github3.GitHubError:
            print("This repository might be empty!\n")

    def list_activity(self):
        return_activities = []
        for activity in self.project.iter_commits():
            return_activities.append(activity)
        return return_activities

    def show_projects(self):
        return_repos = []
        for repo in self.organization.iter_repos():
            return_repos.append(repo.name)
        return return_repos

    def delete_project(self):
        if self.project is None:
            print("Please select from these projects first to delete a project:")
            self.show_projects()
        else:
            self.project.delete()
            self.project = None


    ##################################################################
    #                       MEMBER OPERATIONS                        #
    ##################################################################
    def add_member(self, member_name):
        self.admin.invite(member_name)

    def delete_member(self, member_name):
        self.admin.remove_member(member_name)


    def admin_team(self):
        teams = self.organization.iter_teams();
        admin = None
        for team in teams:
            if team.name == "Admin":
                admin = team
        if admin is None:
            repo_names = ['None']
            self.organization.create_team("Admin", repo_names, "admin")
        return admin

    def list_members(self):
        return_members = []
        for member in self.organization.iter_members():
            return_members.append(str(member))
        return return_members


def exit_prompt():
    exit_cond = input("Do you want to continue (Y/N): ")
    if exit_cond == "Y" or exit_cond == "y":
        return True
    elif exit_cond == "N" or exit_cond == "n":
        return False
    else:
        return exit_prompt()


def manager_menu(github):
    manager_select = input("You logged in as Manager\n" +
                           "------------------------\n" +
                           "To Create Project : C\n" +
                           "To Show All Projects : A\n" +
                           "To Choose a Project: P\n" +
                           "To Show Current Project: S\n" +
                           "To Delete Current Project: D\n" +
                           "----------------------------\n" +
                           "To Add Member To Organization: O\n" +
                           "To Delete Member From Organization: Q\n" +
                           "To Update Member List For All Projects: U\n" +
                           "To List Members: L\n" +
                           "To Exit to Main Menu M: ")
    if manager_select == "C":
        project_name = input("Project name: ")
        github.new_project(project_name, project_name, project_name)
        return exit_prompt()
    elif manager_select == "A":
        github.show_projects()
        return exit_prompt()
    elif manager_select == "P":
        project_name = input("Project name: ")
        github.choose_project(project_name)
        return exit_prompt()
    elif manager_select == "S":
        github.show_project()
        return exit_prompt()
    elif manager_select == "D":
        github.delete_project()
        return exit_prompt()
    elif manager_select == "O":
        member_name = input("Member name: ")
        github.add_member(member_name)
        return exit_prompt()
    elif manager_select == "Q":
        member_name = input("Member name: ")
        github.delete_member(member_name)
        return exit_prompt()
    elif manager_select == "U":
        github.update_members()
        return exit_prompt()
    elif manager_select == "L":
        github.list_members()
        return exit_prompt()
    elif manager_select == "M":
        return False
    else:
        return manager_menu(github)


def interface():
    login_screen = True
    while login_screen:
        user_name = input("GitHub ID: ")
        user_password = input("Password: ")
        organization = input("Organization Name: ")
        github = GitHubAPI(user_name, user_password, organization)
        if github.organization is not None:
            print("Welcome " + github.username)
            user_screen = True
            while user_screen:
                user_type = input("Manager/Exit (M/E): ")
                if user_type == "M":
                    manager_screen = True
                    while manager_screen:
                        manager_screen = manager_menu(github)
                elif user_type == "E":
                    print("Logging out from " + user_name)
                    user_screen = False
                else:
                    print("Wrong input")
        login_screen = exit_prompt()
    print("System is closing...")


if __name__ == '__main__':
    interface()
