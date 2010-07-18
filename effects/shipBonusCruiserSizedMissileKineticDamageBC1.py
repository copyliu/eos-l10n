#Item: Drake [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusCruiserSizedMissileKineticDamageBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusBC1",
                            lambda skill: skill.name == "Heavy Missiles" or \
                            skill.name == "Heavy Assault Missiles",
                            self.item, extraMult = level)