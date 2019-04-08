from character import warrior, mage, priest
from enemy import goblin, murloc
from team import team
from combat import combat
#**************************************Place character into World*************#
warrior_gar = warrior("Orc", "Garrosh")
mage_jen = mage("human", "Jaina")
priest_and = priest("human", "Anduin")
my_team = team([warrior_gar, mage_jen, priest_and], 1)

enemy1 = goblin(1)
enemy2 = goblin(1)
enemy3 = murloc(1)
enemy_team = team([enemy1, enemy2, enemy3], 0)

first_combat = combat(my_team, enemy_team)
first_combat.check_combat_info()
#**************************************Eof************************************#