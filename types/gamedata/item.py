from sqlalchemy.orm import reconstructor
class Item(object):
    @reconstructor
    def init(self):
        self.__race = None
        self.__requiredSkills = None
        
    def getAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key].value
        
    def isType(self, type):
        for effect in self.effects.itervalues():
            if effect.isType(type):
                return True
        
        return False
    
    @property
    def requiredSkills(self):
        if self.__requiredSkills == None:
            from model import db
            requiredSkills = {}
            for i in xrange(5):
                skillID, skillLevel = None, None
                skillID = self.getAttribute('requiredSkill%d' % i)
                skillLevel = self.getAttribute('requiredSkill%dLevel' % i)
                if skillID == None or skillLevel == None: continue
                print skillID
                item = db.getItem(int(skillID))
                requiredSkills[item] = skillLevel
            
            self.__requiredSkills = requiredSkills
            
        return self.__requiredSkills
    
    @property
    def race(self):
        if self.__race == None:
            #There's a few hacks in how we look for this regarding to ships
            #I'll discuss each of them as we do it
            #1: If a ship belongs to the ORE market group, it'll be tagged as ORE
            if self.marketGroup and self.marketGroup.name == "ORE":
                return "ORE"
            
            #2: Items can only have a single raceID
            #   For pirate ships, we'll have to check the races of the skills
            skillRaces = set()
            
            skillRaces.add(self.raceID)
            for skill in self.requiredSkills.iterkeys():
                if skill.raceID != None:
                    skillRaces.add(skill.raceID)
            
            #Now that we know what races the skills have, figure it out
            #Our map on how stuff works.
            map = {(1, 8) : "guristas",
                   (1, 4) : "sansha",
                   (2, 4) : "blood",
                   (2, 8) : "angelserp",
                   (1,)   : "caldari",
                   (2,)   : "minmatar",
                   (4,)   : "amarr",
                   (8,)   : "gallente"}
            
            for matcher, race in map.iteritems():
                match = True
                for raceID in skillRaces:
                    if not raceID in matcher:
                        match = False
                        break
                if match:
                    self.__race = race
                    break
            
            #3: Special handling for angel/serpentis
            if race == "angelserp":
                if self.raceID == 2:
                    self.__race = "angel"
                else:
                    self.__race = "serpentis"
                
            
        return self.__race