def _hitting_set_greedy(ordered_players):
    solution =[]
    visited=[]
    while True:
        player=list(ordered_players.items())[0][0]
        if len(ordered_players[player])!=0:
            solution.append(player)
        else:
            break
        visited[:]=ordered_players[player]
        ordered_players.pop(player)
        for journalist in visited:
            for other_player in ordered_players:
                if journalist in ordered_players[other_player]:
                    ordered_players[other_player].remove(journalist)
        ordered_players = sort_by_journalist(ordered_players)
    return solution

def hitting_set_greedy(B):
    ordered_players = sort_players(B)
    return _hitting_set_greedy(ordered_players)

def sort_players(B):
    journalistsByPlayer= {}
    journalistNumber = 0

    for Bi in B:
        journalistNumber +=1
        for playerName in Bi:
            if playerName not in journalistsByPlayer:
                journalistsByPlayer[playerName] = []
                
            journalistsByPlayer[playerName].append(journalistNumber)
     
    return sort_by_journalist(journalistsByPlayer)

def sort_by_journalist(players):
    return dict(sorted(players.items(), key=lambda item: len(item[1]), reverse=True))