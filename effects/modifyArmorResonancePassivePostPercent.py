#Items from group: Armor Hardener (156 of 156) [Module]
from model.types import State          
type = "passive"
def handler(fit, module, context):
    if module.state != State.ONLINE: return
    for damageType in ("Kinetic", "Thermal", "Explosive", "Em"):
        if damageType == "Thermal":
            dn = "Thermic"
        else:
            dn = damageType
        fit.ship.boostItemAttr("armor%sDamageResonance" % damageType,
                               module.getModifiedItemAttr("passive%sDamageResistanceBonus" % dn),
                               stackingPenalties = True)