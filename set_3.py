'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # Check if from_member follows to_member
    a_follows_b = False
    if from_member in social_graph:
        if "following" in social_graph[from_member]:
            if to_member in social_graph[from_member]["following"]:
                a_follows_b = True
    
    # Check if to_member follows from_member
    b_follows_a = False
    if to_member in social_graph:
        if "following" in social_graph[to_member]:
            if from_member in social_graph[to_member]["following"]:
                b_follows_a = True
    
    # Determine relationship
    if a_follows_b == True and b_follows_a == True:
        return "friends"
    elif a_follows_b == True:
        return "follower"
    elif b_follows_a == True:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    n = len(board)
    
    # Check rows
    for i in range(n):
        first = board[i][0]
        if first != '' and first != None:
            win = True
            for j in range(1, n):
                if board[i][j] != first:
                    win = False
                    break
            if win == True:
                return first
    
    # Check columns
    for j in range(n):
        first = board[0][j]
        if first != '' and first != None:
            win = True
            for i in range(1, n):
                if board[i][j] != first:
                    win = False
                    break
            if win == True:
                return first
    
    # Check diagonal
    first = board[0][0]
    if first != '' and first != None:
        win = True
        for i in range(1, n):
            if board[i][i] != first:
                win = False
                break
        if win == True:
            return first
        
    # Check anti-diagonal
    first = board[0][n-1]
    if first != '' and first != None:
        win = True
        for i in range(1, n):
            if board[i][n-1-i] != first:
                win = False
                break
        if win == True:
            return first
    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if first_stop == second_stop:
        return 0
    
    time = 0
    current = first_stop
    
    while current != second_stop:
        # Find next stop from current stop
        for route in route_map:
            start = route[0]
            end = route[1]
            
            if start == current:
                time = time + route_map[route]["travel_time_mins"]
                current = end
                break
    
    return time