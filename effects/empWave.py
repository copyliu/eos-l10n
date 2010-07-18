#Items from group: Smart Bomb (118 of 118) [Module]
from model.attribute import basicAttribute
type = "active"
def empWave(self, fitting, state):
    self.item.attributes["_maxRange"] = self.item.attributes["empFieldRange"]
