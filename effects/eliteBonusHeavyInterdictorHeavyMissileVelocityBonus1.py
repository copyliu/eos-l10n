#Item: Onyx [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusHeavyInterdictorHeavyMissileVelocityBonus1(self, fitting):
    skill, level = fitting.getCharSkill("")
    boostAmmoListBySkillReq(fitting.modules, "", "",
                       lambda skill: skill.name == "",
                       self.item, extraMult = level)
    
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Interdictors").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusHeavyInterdictors1") * level)