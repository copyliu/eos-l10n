#Used by: Item: Smartbomb
from model.attribute import basicAttribute
type = "active"
def empWave(self, fitting, state):
    self.item.attributes["_maxRange"] = self.item.attributes["empFieldRange"]
