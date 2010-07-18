from customEffects import boostModListBySkillReq
def shipMTFalloffBonusATF(self, fitting):
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusATF2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item)