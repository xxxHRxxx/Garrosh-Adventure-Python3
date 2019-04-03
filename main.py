from character import character, warrior, mage, priest, NPC

#**************************************Place character into World*************#
warrior_gar = warrior("Orc", "Garrosh")
warrior_gar.check_status()
mage_jen = mage("human", "Jaina")
mage_jen.check_status()
priest_and = priest("human", "Anduin")
priest_and.check_status()
npc_dummy = NPC("orc", "dummy", 1)
npc_dummy.check_status()
#**************************************Eof************************************#