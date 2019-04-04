from character import warrior, mage, priest, NPC
from enemy import goblin, murloc

#**************************************Place character into World*************#
warrior_gar = warrior("Orc", "Garrosh")
warrior_gar.check_status()
mage_jen = mage("human", "Jaina")
mage_jen.check_status()
priest_and = priest("human", "Anduin")
priest_and.check_status()
npc_dummy = NPC("orc", "dummy", 1)
npc_dummy.check_status()
enemy1 = goblin(10)
enemy1.check_status()
enemy2 = murloc(15)
enemy2.check_status()
#**************************************Eof************************************#