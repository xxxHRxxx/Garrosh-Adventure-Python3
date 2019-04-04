#**************************************Unit Classes***************************#
#character base class
class character:
  name_ = "Unknown"
  race_ = "Unknown"
  class_ = "Unknown"
  level_ = 1
  #create new character
  def __init__(self, new_race, new_class, new_name, is_npc):
    self.race_ = new_race
    self.class_ = new_class
    self.name_ = new_name
    if (not is_npc):
      self.exp_ = 0;

  #check character info
  def check_status(self):
    npc_or_not = -1
    try:
      self.exp_
      print("[***Player character***]")
    except:
      print("[***NPC character***]")
    print("character name:  ", self.name_)
    print("          race:  ", self.race_)
    print("          class: ", self.class_)
    print("          level: ", self.level_)
    try:
      print("          exp:   ", self.exp_)
    except:
      print("NPC, cannot access exp")

#warrior character
class warrior(character):
  class_name_ = "warrior"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name, 0)

#mage character
class mage(character):
  class_name_ = "mage"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name, 0)

#priest character
class priest(character):
  class_name_ = "priest"
  def __init__(self, new_race, new_name):
    super().__init__(new_race, self.class_name_, new_name, 0)

#NPC character
class NPC(character):
  class_name_ = "NPC"
  def __init__(self, new_race, new_name, new_level):
    self.level_ = new_level
    super().__init__(new_race, self.class_name_, new_name, 1)
#**************************************End Unit Classes***********************#