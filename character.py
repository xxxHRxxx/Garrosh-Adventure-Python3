#**************************************Unit Classes***************************#
#character base class
class character:
  name_ = "Unknown"
  race_ = "Unknown"
  class_ = "Unknown"
  level_ = 1
  health_ = 0
  attack_ = 0
  defence_ = 0
  #create new character
  def __init__(self, new_race, new_class, new_name):
    self.race_ = new_race
    self.class_ = new_class
    self.name_ = new_name
    self.health_ = self.level_*100
    self.exp_ = 0;

  #check character info
  def check_status(self):
    print("[***Player character***]")
    print("character:  {}, level {} {} {}".format(self.name_, self.level_, self.race_,
          self.class_))
    print("health: " + chr(9608)*(self.health_//(self.level_*5)), self.health_)
    print("exp:    ", self.exp_)

  def get_attack_info(self):
    return self.attack_

#warrior character
class warrior(character):
  class_name_ = "warrior"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name)
    self.attack_ = self.level_*10

#mage character
class mage(character):
  class_name_ = "mage"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name)
    self.attack_ = self.level_*20

#priest character
class priest(character):
  class_name_ = "priest"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name)
    self.attack_ = self.level_*1
#**************************************End Unit Classes***********************#