from customEffects import boostModListBySkillReq
def shipBonusHybridTrackingATC2(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusATC2",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item)