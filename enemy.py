#**************************************enemy class****************************#
#enemy base class
class enemy():
  enemy_type_ = "unknown"
  evel_ = 1
  def __init__(self, enemy_type, level):
    self.enemy_type_ = enemy_type
    self.level_ = level

  def check_status(self):
    print("[***enemy***]")
    print("enemy:  level {} {}".format(self.level_, self.enemy_type_))

#enemy goblin
class goblin(enemy):
  goblin_enemy_type_ = "goblin"
  def __init__(self, level):
    super().__init__(self.goblin_enemy_type_, level)

#enemy murloc
class murloc(enemy):
  murloc_enemy_type_ = "murloc"
  def __init__(self, level):
    super().__init__(self.murloc_enemy_type_, level)
#**********************************end enemy class****************************#