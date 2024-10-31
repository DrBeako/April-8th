import random

def roll_d8():
    return random.randint(1,8)

element_table = {
    1: "omni",
    2: ":fire:",
    3: ":ice_cube:",
    4: ":zap:",
    5: ":shamrock:",
    6: ":ocean:",
    7: ":wind_chime:",
    8: ":rock:"
}

def convert_id(id_number):
    return element_table.get(id_number, "ID not found")

class DicePhase:
  def __init__(self, rolls: int, dice_sides: int) -> None:
    self.dice_sides: int = dice_sides
    self.rolls: int = rolls
    self.results: list[int] = []
    self.locked: set[int] = []

  def roll() -> None:
    self.rolls = [random.randint(1, self.dice_sides) for i in range(self.rolls) if i not in self.locked]

  def lock(index: int) -> None:
    self.lock.add(index)