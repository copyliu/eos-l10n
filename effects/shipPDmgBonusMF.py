#Variations of item: Rifter (3 of 3) [Ship]
#Variations of item: Slasher (3 of 3) [Ship]
#Item: Cheetah [Ship]
#Item: Republic Fleet Firetail [Ship]
from customEffects import boostModListBySkillReq
def shipPDmgBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMF",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
