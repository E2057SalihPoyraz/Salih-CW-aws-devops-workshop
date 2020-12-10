def final_direction(dir, turns):
    dirs = "NESW"
    return dirs[(dirs.index(dir)+turns.count("R")-turns.count("L"))%4]

final_direction("N", ["L", "L", "L"])