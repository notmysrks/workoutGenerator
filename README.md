# Workout Generator

This program allows a user to create a personalized profile with their choice of exercises and then generate a randomized workout program according to the user's preferences.

---

## Videos
- [Code Demo](add link here)
- [Code Walkthrough](add link here)
## How to Run

From the project directory in your terminal:
`main.py` or `python3 main.py`

Requires Python 3.7 or newer for `dataclass` module support, check version with `python3 -V`

No third party modules required. Plug and play.

Prebuilt TestUser profile in profiles.json has 2 exercises in each category for Relaxed and Standard intensity to demonstrate randomization of generated workouts and no workouts of Hardcore intensity to demonstrate error handling when a user attempts to generate a workout without exercises in their profile corresponding to the chosen intensity.

Note for Pycharm users:
`clearScreen()` requires enabling Terminal plugin in Pycharm configuration for full functionality (it's easier to just run it from the command line)

## Features Implemented:

- Profile persistence (saving/loading) with `dataclass` classes and `json` module
- Composition OOP relationships (Profiles have a list of Exercises)
- Recursive decision trees
- Robust input validation

## Dataclass References:

- https://stackoverflow.com/a/68929467
- https://docs.python.org/3/library/dataclasses.html
- https://medium.com/alan/5-things-you-should-know-about-dataclass-8c143b75596
