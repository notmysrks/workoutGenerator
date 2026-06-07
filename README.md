# Workout Generator

This program allows a user to create a personalized profile with their choice of exercises and then generate a randomized workout program according to the user's preferences.

## Videos
- [Demo](https://youtu.be/uvVH2tUc0OA) (1:52)
- [Code Walkthrough](https://youtu.be/SZSuukd_aiQ) (4:38)

## How to Run
No third party modules required. Plug and play. Requires Python 3.7 or newer for `dataclass` module support, check version with `python3 -V`

### Terminal (Recommended)
- From the project directory: `python3 main.py`

### Pycharm
- Add `TERM=xcode-color` to your Environment Variables
- From the Terminal panel: `python3 main.py`

###### Note for testing:

Prebuilt TestUser profile in profiles.json has 2 exercises in each category for Relaxed and Standard intensity to demonstrate randomization of generated workouts and no workouts of Hardcore intensity to demonstrate error handling when a user attempts to generate a workout without exercises in their profile corresponding to the chosen intensity.

## Features Implemented:

- Profile persistence (saving/loading) with `dataclass` classes and `json` module
- Composition OOP relationships (Profiles have a list of Exercises)
- Recursive decision trees
- Robust input validation

#### Dataclass References:

- https://stackoverflow.com/a/68929467
- https://docs.python.org/3/library/dataclasses.html
- https://medium.com/alan/5-things-you-should-know-about-dataclass-8c143b75596
