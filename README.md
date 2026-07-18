# Pong & QuadPong

**Created by Jeremy Offutt**
**July 2026**

A recreation of the classic arcade game Pong, built in Python 3.12 using Pygame, and expanded into QuadPong, an original four-player survival variant. This project was built to practice object-oriented programming, game loops, collision detection, AI behavior, Git, and organizing a larger Python project across multiple modules.

---

## Features

### Pong

* Single Player against a computer-controlled opponent
* Local Two Player mode
* Start menu
* Game Over screen
* Score tracking
* Keyboard and mouse controls

### QuadPong

* Four-player local multiplayer
* Survival game mode
* First player to reach **5 points scored against them loses**
* Four independent paddles
* Expanded collision handling for four-sided gameplay

---

## Technologies

* Python 3.12
* Pygame 2.6
* Git
* Visual Studio Code

---

## Running the Project

### Install Pygame

```bash
pip install pygame
```

### Start the Game

```bash
python pongMain.py
```

---

## Menu Controls

| Key       | Action        |
| --------- | ------------- |
| **Space** | Single Player |
| **M**     | Two Player    |
| **4**     | QuadPong      |
| **Esc**   | Quit          |

---

## Game Controls

### Pong

| Paddle       | Controls  |
| ------------ | --------- |
| Left Player  | **W / S** |
| Right Player | **↑ / ↓** |

### QuadPong

| Paddle | Controls  |
| ------ | --------- |
| Left   | **W / S** |
| Right  | **↑ / ↓** |
| Bottom | **V / B** |
| Top    | **5 / 6** |

---

## Project Goals

The purpose of this project was to build a complete game from start to finish while learning:

* Object-oriented programming
* Inheritance
* Collision detection
* Vector math using `pygame.math.Vector2`
* AI paddle movement
* Event-driven programming
* Project organization using multiple Python modules
* Git branching and version control

Rather than stopping after recreating Pong, the project was expanded into **QuadPong** to explore more complex collision handling and multiplayer game logic.

---

## Future Improvements

Potential additions include:

* Sound effects and music
* Visual effects and animation
* Controller support
* Circle-based collision detection
* Better menus and UI polish

---
## Development Notes

This project was intentionally built as a learning exercise rather than by following a tutorial. The goal was to complete an entire game lifecycle from planning and implementation to debugging, refactoring, documentation, and version control.

