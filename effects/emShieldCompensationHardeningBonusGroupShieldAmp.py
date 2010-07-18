#Item: EM Shield Compensation [Skill]
from customEffects import boostModListByReq, increase
def emShieldCompensationHardeningBonusGroupShieldAmp(self, fitting, level):
    boostModListByReq(fitting.modules, "emDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Shield Amplifier",
                      self.item, extraMult = level)