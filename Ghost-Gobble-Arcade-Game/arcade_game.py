def eat_ghost(power_pellet_active, touching_ghost):
    """
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return power_pellet_active and touching_ghost
# eat_ghost()'s outputs
answer = eat_ghost(True,False)
print(f'Pac-Man eats a ghost? R// : {answer} ')

def score(touching_power_pellet, touching_dot):
    """
 
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet or touching_dot
# score()'s outputs
answer = score(True,False)
print(f'Pac-Man scores? R// : {answer} ')

def lose(power_pellet_active, touching_ghost):
    """
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    return touching_ghost and not power_pellet_active
# lose()'s outputs
answer = lose(True,False)
print(f'Pac-Man loses? R// : {answer} ')

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
 
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
# win()'s outputs
answer = win(True,False,True)
print(f'Pac-Man wins? R// : {answer} ')