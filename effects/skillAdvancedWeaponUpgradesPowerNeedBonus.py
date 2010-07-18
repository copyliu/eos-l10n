#Item: Advanced Weapon Upgrades
from customEffects import boostModListBySkillReq
def skillAdvancedWeaponUpgradesPowerNeedBonus(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "power", "powerNeedBonus",
                           lambda skill: skill.name == "Gunnery" or skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)