#Used by: Ship: Nidhoggur
#               Hel
from customEffects import boostModListByReq
def carrierMinmatarArmorShieldAmount(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Carrier")
    boostModListByReq(fitting.modules, "shieldBonus", "carrierMinmatarBonus2",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "armorDamageAmount", "carrierMinmatarBonus2",
                      lambda mod: mod.group.name == "Armor Repair Projector",
                      self.item, extraMult = level)
