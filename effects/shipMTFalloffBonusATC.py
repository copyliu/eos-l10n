from customEffects import boostModListBySkillReq
def shipMTFalloffBonusATC(self, fitting):
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusATC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item)