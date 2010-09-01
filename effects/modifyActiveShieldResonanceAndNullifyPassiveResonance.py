#Used by:
#Modules from group: Shield Hardener (91 of 91)
from eos.types import State
type = "active"
def handler(fit, module, context):
    if module.state >= State.ACTIVE:
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            fit.ship.boostItemAttr("shield" + damageType.capitalize() + "DamageResonance",
                                   module.getModifiedItemAttr(damageType + "DamageResistanceBonus"),
                                   stackingPenalties = True)
            module.multiplyItemAttr("passive" + damageType.capitalize() + "DamageResistanceBonus", 0)
