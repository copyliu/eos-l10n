from customEffects import boostModListBySkillReq
def shipProjectileDmgMC(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMC",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)