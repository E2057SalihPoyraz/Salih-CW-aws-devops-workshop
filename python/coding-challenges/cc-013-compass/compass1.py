def final_direction(dir, turns):
    dir_sym = ["E","N","W","S"]
    dir_coord = [0,90,180,270]
    loc = (dir_coord[dir_sym.index(dir)]+(turns.count("L")-turns.count("R"))*90)%360
    return dir_sym[dir_coord.index(loc)]

final_direction("N", ["L", "L", "L"])