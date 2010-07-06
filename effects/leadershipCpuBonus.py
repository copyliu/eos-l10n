#Used by: Ship: Erebus
#               Leviathan
#               Avatar
#               Ferox
#               Brutix
#               Cyclone
#               Prophecy
#               Eos
#               Sleipnir
#               Vulture
#               Absolution
#               Astarte
#               Claymore
#               Nighthawk
#               Damnation
#               Hel
#               Archon
#               Ragnarok
#               Thanatos
#               Nyx
#               Chimera
#               Wyvern
#               Aeon
#               Nidhoggur
#               Harbinger
#               Drake
#               Myrmidon
#               Hurricane
#               Rorqual
#               Orca
#        Item : Legion Defensive - Warfare Processor
#               Tengu Defensive - Warfare Processor
#               Loki Defensive - Warfare Processor
#               Proteus Defensive - Warfare Processor
from customEffects import boostModListBySkillReq
def leadershipCpuBonus(self, fitting, state = None):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Leadership", self.item)