# Turtle Crossing Game

A simple arcade-style game where you guide a turtle across a busy road filled with moving cars. The goal is to reach the other side without getting hit!

## Description

In **Turtle Crossing**, you control a turtle starting at the bottom of the screen. Your objective is to cross the road and reach the top finish line. As you progress, the cars move faster, making each level more challenging.

## How to Play

- **Start the Game**: Run `main.py` to start.
- **Controls**:
  - Press the **Up Arrow** key to move the turtle forward.
  - Press the **Left Arrow** key to move left.
  - Press the **Right Arrow** key to move right.
- **Objective**:
  - Avoid the moving cars.
  - Reach the top edge of the screen to level up.
  - Each new level increases the speed of the cars.
- **Game Over**: If changes collide with a car, the game ends.

## Requirements

- Python 3.x
- Standard libraries (no external installation required):
  - `turtle`
  - `time`
  - `random`

## Installation & Running

1.  Ensure you have Python installed on your system.
2.  Clone or download this repository.
3.  Navigate to the project directory in your terminal.
4.  Run the game using the following command:

    ```bash
    python main.py
    ```

## Project Structure

- `main.py`: The entry point of the game. Handles the game loop, screen setup, and event listeners.
- `player.py`: Contains the `Player` class, which manages the turtle's movement and position.
- `car_manager.py`: Contains the `CarManager` class, responsible for generating and moving the cars.
- `scoreboard.py`: Contains the `Scoreboard` class, which displays the current level and "Game Over" message.
