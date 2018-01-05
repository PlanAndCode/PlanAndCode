########## IMPORT AREA #########



from .trelloAPI import trelloAPI


############# MAIN AREA ########



#github = githubapi.github()
#github.main()




def mainTrello():

    trello = trelloAPI.trello(apiKey="6a4fe89f7b7bd584332a3cecf685d25b",TOKEN="31322c771f6bce7fc36f6cd066cc0ebfea8102c6cb2d7e59e6e0448f557709c4")
    """
    
    # Trello Projects
    boardList= trello.boardList()
    print(  boardList )
    # Choose one of projects For Example last one
    board = trello.getBoard(boardList[0].id)
    print(board.name)
    
    # list list of the board on the screen
    listBoard=board.get_lists(None)
    print(listBoard)
    
    toDo=listBoard[0]
    coding=listBoard[1]
    #build=listBoard[2]
    #test=listBoard[3]
    #deploy=listBoard[4]
    
    
    # cards of List
    print(toDo.list_cards())
    print(coding.list_cards())
    
    
    #move a card
    #cardID=toDo.list_cards()[0].id
    #trello.moveCard(cardID,coding.id)
    
    
    #print(trello.createBoard("bordAPI"))
    #trello.printTrello()
    #trello.closeBoardName("bordAPI")
    
    """

    # organization üyeleri sadece pano görebilir
    # eğer panoya aynı üyeler eklenirse pano üzerinde yetki sahibi olabilirler
    organizationID = trello.createOrganization("apiTestTeam2")

    print(organizationID)

    print()
    # permission normal : sadece pano görebilir
    # permission admin : extra üye ekle çıkar, pano kapat
    print(trello.addOrganizationMember(organizationID,"aykocayko@gmail.com","admin"))
    print(trello.addOrganizationMember(organizationID,"my_kurt@hotmail.com","admin"))
    print(trello.getOrganization(organizationID).get_members())

    print()
    # org team seviyesinde görülebilir pano yaratır
    createdBoard=trello.createBoard("TestBoard",organizationID,"org")
    print(createdBoard)
    #trello.printTrello()
    #trello.closeBoardName("bordAPI")

    # board üzerinde kimsenin yetkisi yok
    print(createdBoard.get_members())

    # board üzerinde herkese yetki verelim
    organizationMembers = trello.getOrganization(organizationID).get_members()

    print(organizationMembers.pop(-1).username)
    #organizationMembers.remove(organizationMembers[-1])

    #for mem in organizationMembers:
     #   createdBoard.add_member(mem)



    trello.closeBoard(createdBoard.id)

    trello.removeOrganization(organizationID)

mainTrello()