#Item: Advanced Weapon Upgrades
from customEffects import boostModListBySkillReq
def skillAdvancedWeaponUpgradesPowerNeedBonusBombLaunchers(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "power", "powerNeedBonus",
                           lambda skill: skill.name == "Bomb Deployment",
                           self.item, extraMult = level)