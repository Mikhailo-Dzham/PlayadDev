from gen_tools import *

class Entity:
    def __init__(self):
        pass

class Playable(Entity):
    def __init__(self):
        self.core_stats = dict(zip(("pwr","stm","hp","int","mp"), [haist() for _ in range(5)]))
        #some comment