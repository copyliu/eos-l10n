from customEffects import boostModListBySkillReq
def shipMTMaxRangeBonusATF(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusATF2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item)