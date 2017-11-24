import github3
from github3 import login

def my_two_factor_function():
    code = ''
    while not code:
        # The user could accidentally press Enter before being ready,
        # let's protect them from doing that.
        code = input('Enter 2FA code: ')
    return code

def login(id,token):
    g = github3.login(id,token,
                      two_factor_callback=my_two_factor_function)
    return g

def getOrganization(g,organizationName):
    org = g.organization(organizationName)
    return org

def getAdminTeam(g,organization,adminteamname):
    teams = organization.iter_teams();
    admin = None
    for team in teams:
        if team.name == adminteamname:
            admin = team
    return admin

def inviteToTeam(team,person):
    result=team.invite(person)
    return result

def main():
    g=login("burakfurkanaksahin","d672c87e244e4e736deb300a6f324d6c6d41a1fc")
        #d672c87e244e4e736deb300a6f324d6c6d41a1fc

    organization=getOrganization(g,"PlanAndCode")
    admin = getAdminTeam(g,organization,"Admin")
    print(admin.is_member("burakfurkanaksahin"))
    print(admin.is_member("muzaffermetehanalan"))
    print(admin.is_member("aydincalikoglu"))
    print(admin.is_member("hkteloglu"))
    print(admin.is_member("gulzadaiisaeva"))
    print(admin.is_member("fkiraz"))
    print(admin.is_member("osmanakkus44"))
    print(admin.is_member("ibrhmyzc"))
    #organization.create_repo("NewProject", "Created from PlanAndCode.py", False, True, True, True, admin.id, True, "None", "None")

main()