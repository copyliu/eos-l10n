#Used by: Item: Information Warfare Link - Electronic Superiority
#Workaround so the skills coded to boost commandBonus can just boost it without caring
runTime = "early"
def gangInformationWarfareSuperiority(self, fitting, state):
    self.item.attributes["commandBonus"] = self.item.attributes["commandBonusHidden"]