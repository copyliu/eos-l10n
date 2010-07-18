#Item: Nightmare [Ship]
from customEffects import boostModListBySkillReq
def shipBonusLargeEnergyTurretDamageCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListBySkillReq(
        fitting.modules,
        "damageMultiplier",
        "shipBonus2CB",
        lambda skill: skill.name == "Large Energy Turret",
        self.item,
        extraMult = level
    )
