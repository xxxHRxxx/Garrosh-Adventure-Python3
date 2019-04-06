from character import warrior, mage, priest
from enemy import goblin, murloc
from team import team
#**************************************Place character into World*************#
warrior_gar = warrior("Orc", "Garrosh")
mage_jen = mage("human", "Jaina")
priest_and = priest("human", "Anduin")
my_team = team([warrior_gar, mage_jen, priest_and], 1)
my_team.check_team_status()


enemy1 = goblin(10)
enemy2 = goblin(10)
enemy3 = murloc(15)
enemy_team = team([enemy1, enemy2, enemy3], 0)
enemy_team.check_team_status()

#**************************************Eof************************************#