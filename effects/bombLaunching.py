#Used by: All bombs
from model import attribute
runTime = "late"
def bombLaunching(self, fitting, containerModule):
    #Set maxrange value for bombs here, as it's not available anywhere and this effect
    #is shared between all bombs
    flightTime = self.item.getModifiedAttribute("explosionDelay") / 1000.0
    speed = self.item.getModifiedAttribute("maxVelocity")
    containerModule.attributes["_maxMissileRange"] = attribute.basicAttribute(containerModule, "_maxMissileRange", None, flightTime * speed)
