# Frog-and-Leap-game-in-python
The Frog and Toad game you've implemented is a simple puzzle game. Here's the logic behind the game:

1. **Initialization:**
   - The game is initialized with a specified number of frogs (`num_frogs`) and toads (`num_toads`).
   - Each frog and toad is represented by an index in the list (`self.frogs` and `self.toads`). The order of the frogs and toads is represented by the order of the indices in these lists.
   - An `empty_space` is initialized at the end of the list to represent an empty space.

2. **Game State:**
   - The game state is represented by the positions of frogs, toads, and the empty space.
   - The goal is to arrange all the frogs to the left of all the toads (i.e., in non-decreasing order).

3. **Valid Move:**
   - A move is valid if the selected frog's index is within the range of the frog list and the space it's moving to is not already occupied.

4. **Making a Move:**
   - When a valid move is made, the selected frog is moved to the empty space, and the empty space takes the index of the moved frog.

5. **Winning Condition:**
   - The game is won when all the frogs are on the left side (with indices less than the empty space).

6. **Game Loop:**
   - The player is prompted to input the index of the frog to move.
   - If the move is valid, the move is executed, and the game state is updated.
   - The loop continues until the winning condition is met.

7. **Printing the State:**
   - The `__str__` method is used to print the current state of the game, showing the positions of frogs, toads, and the empty space.

8. **Playing the Game:**
   - The `play_game` function initializes the game and enters a loop where the player is prompted to make moves until they win.

This is a simple and text-based representation of a Frog and Toad puzzle, where the player's goal is to rearrange the frogs and toads to achieve a specific order. The game is won when all the frogs are on the left side.
