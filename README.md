# Workout Generator

This program allows a user to create a personalized profile with their choice of exercises and then generate a randomized workout program according to the user's preferences.

## UX Flowchart
![UX Flowchart](https://github.com/notmysrks/workoutGenerator/blob/main/updatedUX.png?raw=true)
## Videos
- [Demo](https://www.youtube.com/watch?v=7qXSc_RuWJg) (2:01)
- [Code Walkthrough](https://youtu.be/SZSuukd_aiQ) (4:38)

## How to Run
No extra modules required, plug and play. 

>[!NOTE]
>Requires Python 3.7 or newer for `dataclasses` module support, check version with `python3 -V`

### Terminal (Recommended)
- From the project directory: `python3 main.py`

### Pycharm
- Add `TERM=xcode-color` to your Environment Variables
- From the Terminal panel: `python3 main.py`

## Features Implemented:

- Profile persistence (saving/loading) with `@dataclass` classes and `json` module
- Composition OOP relationships (Profiles have a list of Exercises)
- Recursive decision trees
- Robust input validation

#### Dataclass References:

- https://stackoverflow.com/a/68929467
- https://docs.python.org/3/library/dataclasses.html
- https://medium.com/alan/5-things-you-should-know-about-dataclass-8c143b75596
