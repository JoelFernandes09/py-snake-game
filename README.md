# Classic Snake Game

A recreation of the classic Snake game using Python's `turtle` module. This project includes interactive gameplay, score
tracking, and collision detection, demonstrating fundamental game development concepts.

## Features

- Player-controlled snake movement using arrow or WASD keys.
- Randomly spawned food for the snake to consume.
- Score tracking and game-over display.
- Realistic wall and tail collision detection.
- Dynamic snake growth upon consuming food.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JoelFernandes09/py-snake-game.git
   cd py-snake-game
   ```
2. Run the Python script:
   ```bash
   python main.py
   ```

## Controls

- **Arrow Keys or WASD**: Control the direction of the snake.

## Gameplay

1. The snake starts as a small line.
2. Move the snake to consume the red food on the screen.
3. Each food item consumed increases the snake's length and score.
4. The game ends if the snake collides with the wall or its own tail.

## Technologies Used

- Python 3
- Turtle Graphics

## Project Structure

```
|-- food.py         # Handles food creation and repositioning
|-- main.py         # Main script to run the game
|-- scoreboard.py   # Manages score tracking and game-over display
|-- snake.py        # Contains Snake class and movement logic
```

## Example Output

```
Score: 5
GAME OVER!
```

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out to:

- **Joel Fernandes (Rockhopper)** - [joelfernandes.co.in](https://joelfernandes.co.in)
- GitHub: [JoelFernandes09](https://github.com/JoelFernandes09)
- Instagram: [@jooooeeeellll](https://instagram.com/jooooeeeellll)