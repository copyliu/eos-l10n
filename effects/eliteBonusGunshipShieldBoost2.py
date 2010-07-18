#Item: Hawk
from customEffects import boostModListByReq
def eliteBonusGunshipShieldBoost2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListByReq(fitting.modules, "shieldBonus", "eliteBonusGunship2",
                      lambda mod: mod.group.name == "Shield Booster", self.item,
                      extraMult = level)