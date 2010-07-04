from model.types import Item

class Skill(object):
    def __init__(self):
        self.__skill = None
        self.__level = None
        
    @property
    def skill(self):
        return self.__skill
    
    @skill.setter
    def skill(self, skill):
        if skill != None and type(skill) != Item:raise ValueError("skill should be an item or none")
        self.__skill = skill
        self.skillID = skill.ID if skill != None else None
