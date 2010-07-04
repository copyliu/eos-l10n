#Used by: Item: Defender Missile
def defenderMissileLaunching(self, fitting, containerModule):
    #Ignore defender missile damage
    self.item.attributes["explosiveDamage"].overrideValue = 0