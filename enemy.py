#**************************************enemy class****************************#
import math
from game_util import health_bar_block_num

#enemy base class
class enemy():
  enemy_type_ = "unknown"
  level_ = 1
  full_health_ = 0
  curr_health_ = 0
  attack_ = 0
  def __init__(self, enemy_type, level):
    self.enemy_type_ = enemy_type
    self.level_ = level
    self.full_health_ = self.level_*100
    self.curr_health_ = self.full_health_

  def check_status(self):
    print("[***enemy***]")
    print("enemy:  level {} {}".format(self.level_, self.enemy_type_))
    print("health: " + chr(9608)*(health_bar_block_num(self.curr_health_, self.full_health_))
          + "_"*(20 - health_bar_block_num(self.curr_health_, self.full_health_)) + 
          "{}/{}".format(self.curr_health_, self.full_health_))

	#get current health
  def get_current_health(self):
  	return self.curr_health_

  def get_attack_info(self):
  	return self.attack_

  def get_name(self):
  	return self.enemy_type_

  def set_new_health(self, new_health):
  	self.curr_health_ = new_health

  def take_damage(self, damage):
  	self.curr_health_ = (self.curr_health_ - damage) if (self.curr_health_ - damage) >= 0 else 0

#enemy goblin
class goblin(enemy):
  goblin_enemy_type_ = "goblin"
  def __init__(self, level):
  	self.attack_ = 5
  	super().__init__(self.goblin_enemy_type_, level)

#enemy murloc
class murloc(enemy):
  murloc_enemy_type_ = "murloc"
  def __init__(self, level):
  	self.attack_ = 10
  	super().__init__(self.murloc_enemy_type_, level)
#**********************************end enemy class****************************#