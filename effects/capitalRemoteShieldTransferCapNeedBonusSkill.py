#Item: Capital Shield Emission Systems [Skill]
#Item: Hardwiring - Zainou 'Sprite' KXX1000 [Implant]
#Item: Hardwiring - Zainou 'Sprite' KXX2000 [Implant]
#Item: Hardwiring - Zainou 'Sprite' KXX500 [Implant]
from customEffects import boostModListByReq
def capitalRemoteShieldTransferCapNeedBonusSkill(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)