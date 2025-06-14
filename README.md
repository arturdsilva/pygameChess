# Chess Game Refactoring Project

## Overview

This project involved refactoring an existing functional chess game, initially
characterized by various code smells, to improve its design and
maintainability through the application of relevant design patterns. The
original codebase is preserved for reference, while the refactored version
demonstrates enhanced architectural principles.

## Project Context

This project was developed as part of the **CSI-22: Object-Oriented
Programming** course.

**Professor:** Karla D. Fook

**Students:**

- Ângelo de Carvalho Nunes
- Arthur Rocha e Silva
- Artur Dantas Ferreira da Silva
- Gabriel Padilha Leonardo Ferreira
- Guilherme Eiji Moriya

## Design Patterns Applied

During the refactoring process, the following design patterns were
strategically implemented:

### State Pattern

The State pattern was applied to manage the different states of the game. This
was achieved by creating distinct classes for each game state (e.g.,
`PlayingState`, `GameOverState`), allowing the game's behavior to change based
on its internal state. This approach centralizes state-specific logic, making
the codebase more organized and easier to extend.

### Facade Pattern

The Facade pattern was used to provide a simplified interface to a complex
subsystem. A `Game` class was introduced to act as a facade, encapsulating the
intricate interactions between various game components. Additionally, the
`Drawer` component, responsible for rendering the game's visual elements, also
functions as a facade within the broader `Game` facade, further simplifying
the drawing operations.

## Project Structure

The project is structured to clearly separate the original and refactored
code, as well as to organize components based on their responsibilities. The
`old_main` file contains the initial codebase, while the refactored code is
organized into modules such as `states` (for State pattern implementations)
and other relevant directories for game logic and drawing.

Further details on the specific implementation of each pattern can be found by
examining the respective source files within the project directory.


