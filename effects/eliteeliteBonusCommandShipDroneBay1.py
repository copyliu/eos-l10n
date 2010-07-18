#Item: Eos
from customEffects import increase
def eliteeliteBonusCommandShipDroneBay1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    increase(fitting.ship, "droneCapacity", "eliteBonusCommandShips1",
                  self.item, extraMult = level)