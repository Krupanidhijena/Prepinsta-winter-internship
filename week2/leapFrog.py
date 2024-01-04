class FrogAndToadGame:
  def __init__(self, num_frogs, num_toads):
    self.frogs = [i for i in range(num_frogs)]
    self.toads = [i for i in range(num_toads)]
    self.empty_space = num_frogs + num_toads

  def is_valid_move(self, move):
    if move < 0 or move >= len(self.frogs):
      return False
    if self.frogs[move] == self.empty_space:
      return False
    return True

  def make_move(self, move):
    self.frogs[move], self.empty_space = self.empty_space, self.frogs[move]

  def is_won(self):
    return all(frog >= self.empty_space for frog in self.frogs)

  def __str__(self):
    return "Frogs: {} | Toads: {} | Empty space: {}".format(
        self.frogs, self.toads, self.empty_space
    )


def play_game():
  num_frogs = int(input("Enter the number of frogs: "))
  num_toads = int(input("Enter the number of toads: "))
  game = FrogAndToadGame(num_frogs, num_toads)

  while not game.is_won():
    print(game)
    move = int(input("Enter the index of the frog to move: "))
    if not game.is_valid_move(move):
      print("Invalid move.")
      continue
    game.make_move(move)

  print("Congratulations, you won!")


if __name__ == "__main__":
  play_game()