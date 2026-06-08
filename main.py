"""
WORKOUT GENERATOR
This program allows a user to create a personalized profile with their choice of exercises and then generate a randomized workout program according to the user's preferences.

Skylar Randall Kass
June 07, 2026
"""


from copy import deepcopy
from random import shuffle
from os import system, name
from classes import Exercise, Profile

def promptToLoadOrCreateProfile(allProfiles = None):
  """Prompt the user to load an existing profile or create a new one"""

  clearScreen()
  print("Welcome to Workout Generator!")

  if not allProfiles:
    print("\nNo profiles have been created yet!")
    saveOrLoadChoice = 2
  else:
    print("\nPress 1 to load profile or 2 to make a new profile.\n")
    print("(1) Load Profile")
    print("(2) New Profile")

    try:
      saveOrLoadChoice = int(input("\nEnter your choice: "))
    except ValueError:
      invalidInput()
      return promptToLoadOrCreateProfile(allProfiles)
    if saveOrLoadChoice not in [1,2]:
      invalidInput()
      return promptToLoadOrCreateProfile(allProfiles)

  if saveOrLoadChoice == 1:
    clearScreen()
    print("Select a profile to load:\n")
    count = 1
    for profile in allProfiles:
      print(f"({count}) {profile.name}")
      count += 1

    try:
      profileChoice = int(input("\nEnter your choice: "))
    except ValueError:
      invalidInput()
      return promptToLoadOrCreateProfile(allProfiles)
    if profileChoice < 1 or profileChoice > len(allProfiles):
      invalidInput()
      return promptToLoadOrCreateProfile(allProfiles)
    thisProfile = allProfiles[profileChoice-1]
    #input(thisProfile)  # Show Profile with unloaded exercise dictionaries
    Profile.loadProfile(thisProfile)
    #input(thisProfile)  # Show Profile with loaded Exercise objects

  else: # saveOrLoadChoice == 2
    clearScreen()
    try:
      profileName = str(input("Enter your name to create a new profile:"))
    except ValueError:
      invalidInput()
      return promptToLoadOrCreateProfile(allProfiles)
    if profileName == '':
      blankInput()
      return promptToLoadOrCreateProfile(allProfiles)
    for thisProfile in allProfiles:
      if thisProfile.name == profileName:
        input(f"Profile {profileName} already exists! Press Enter to try another option...")
        return promptToLoadOrCreateProfile(allProfiles)
    thisProfile =  Profile(profileName, [])

  return thisProfile


def mainMenu(profile):
  """Display the main menu"""

  clearScreen()
  Profile.displayProperties(profile)
  print("Select an option:\n")
  print("(1) Manage Profile")
  print("(2) Generate Workout")
  print("(3) Exit")

  mainMenuChoice = None
  try:
    mainMenuChoice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    mainMenu(profile)

  if mainMenuChoice not in [1, 2, 3]:
    invalidInput()
    mainMenu(profile)
  elif mainMenuChoice == 1:
    manage(profile)
  elif mainMenuChoice == 2:
    workout(profile)
  else: # mainMenuChoice == 3
    exitProgram(profile)


def workout(profile):
  """Initiate flow for user to generate and complete workout"""

  clearScreen()
  print("Enter (0) to return to the main menu.\n")
  print("Select an intensity:\n")
  print("(1) Relaxed")
  print("(2) Standard")
  print("(3) Hardcore")

  intensity = None
  try:
    intensity = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    workout(profile)
  if intensity not in [0, 1, 2, 3]:
    invalidInput()
    workout(profile)
  elif intensity == 0:
    mainMenu(profile)
  else: # intensity == 1, 2, or 3
    generateWorkout(profile, intensity)
    mainMenu(profile)


def generateWorkout(profile, intensity):
  """Generate a workout from the list of exercises associated with the current user"""

  thisWorkout = deepcopy(profile.exercises)
  shuffle(thisWorkout)

  print("\nGenerating Workout...\n")
  warmup = selectExerciseFromProfile(profile, thisWorkout, intensity, "Warmup")
  strengthening = selectExerciseFromProfile(profile, thisWorkout, intensity, "Strengthening")
  cardio = selectExerciseFromProfile(profile, thisWorkout, intensity, "Cardio")
  cooldown = selectExerciseFromProfile(profile, thisWorkout, intensity, "Cooldown")

  print(f"Warmup: {warmup.name}")
  print(f"Strengthening: {strengthening.name}")
  print(f"Cardio: {cardio.name}")
  print(f"Cooldown: {cooldown.name}")

  print("\n(1) Start workout")
  print("(2) Generate a different workout")
  print("(0) Return to the main menu")

  choice = None
  try:
    choice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    generateWorkout(profile, intensity)
  if choice not in [0, 1, 2]:
    invalidInput()
    generateWorkout(profile, intensity)
  elif choice == 2:
    generateWorkout(profile, intensity)
  elif choice == 0:
    mainMenu(profile)
  else:
    nextExercise(warmup, "Warmup")
    nextExercise(strengthening, "Strengthening")
    nextExercise(cardio, "Cardio")
    nextExercise(cooldown, "Cooldown")
    mainMenu(profile)


def selectExerciseFromProfile(profile, thisWorkout, intensity, category):
  """Select an exercise from the list of exercises associated with the current profile"""

  clearScreen()
  chosenExercise = next((exercise for exercise in thisWorkout if exercise.intensity == intensity and exercise.category == category), None)
  if not chosenExercise:
    intensityStrings = ["Relaxed", "Standard", "Hardcore"]
    print(f"This profile does not have a {category} exercise with a {intensityStrings[intensity-1]} intensity rating.")
    print("Try adding more exercises to this profile or select a different intensity.")
    input("\nPress Enter to return to the main menu...")
    mainMenu(profile)
  else:
    return chosenExercise


def nextExercise(exercise, category):
  """Prints details for the next exercise in the workout."""

  clearScreen()
  print(f"Your {category} exercise is {exercise.name}.\n")
  if exercise.duration:
    if exercise.duration > 60:
      print(f"Duration: {int(exercise.duration / 60)} minutes and {exercise.duration % 60} seconds")
    else:
      print(f"Duration: {exercise.duration} seconds")
  else:
    print(f"Do {exercise.sets} sets of {exercise.reps} repetitions.")
  input("\nPress Enter to continue...")


def manage(profile):
  """Initiate flow for user to create and edit exercises"""

  clearScreen()
  Profile.displayProperties(profile)
  print("Select an option:\n")
  print("(1) Add an exercise")
  print("(2) Edit an exercise")
  print("(3) Delete an exercise")
  print("(4) Delete profile")
  print("\n(0) Main Menu")

  choice = None
  try:
    choice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    manage(profile)
  if choice not in [1, 2, 3, 4, 0]:
    invalidInput()
    manage(profile)

  if choice == 1:
    addExercise(profile)
  elif choice == 2:
    editExercise(profile)
  elif choice == 3:
    deleteExercise(profile)
  elif choice == 4:
    deleteProfile(profile)
  else: # choice == 5
    mainMenu(profile)


def addExercise(profile):
  """Initiate flow for user to add an exercise"""

  clearScreen()
  thisName = promptToAddProperty(profile, "Name")
  thisCategory = promptToAddProperty(profile, "Category")
  thisIntensity = promptToAddProperty(profile, "Intensity")
  durationChoice = chooseSetsOrReps(profile)

  if durationChoice == 1:
    thisSets = promptToAddProperty(profile, "Sets")
    thisReps = promptToAddProperty(profile, "Reps")
    thisDuration = None
  else:
    thisDuration = promptToAddProperty(profile, "Duration")
    thisSets = None
    thisReps = None

  newExercise = Exercise(thisName, thisCategory, thisIntensity, thisDuration, thisSets, thisReps)
  confirmExercise(profile, newExercise)


def confirmExercise(profile, newExercise):
  """Asks the user whether to add exercise to profile or exit editor without saving"""

  clearScreen()
  Exercise.displayProperties(newExercise)
  print("\nPress (1) to save this exercise or (2) to return to main menu without saving.")

  choice = None
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    invalidInput()
    addExercise(profile)
  if choice not in [1, 2]:
    invalidInput()
    addExercise(profile)
  elif choice == 1:
    profile.exercises.append(newExercise)
    manage(profile)
  else:
    mainMenu(profile)


def chooseSetsOrReps(profile):
  """Choose whether this exercise will be measured in sets and reps or duration in seconds."""

  clearScreen()
  print("Enter (0) to return to main menu without saving.\n")
  print("Is this exercise measured in sets and reps or time?\n")
  print("(1) Sets and reps")
  print("(2) Time")

  try:
    durationChoice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    return chooseSetsOrReps(profile)
  if durationChoice not in [0, 1, 2]:
    invalidInput()
    return chooseSetsOrReps(profile)
  elif durationChoice == 0:
    mainMenu(profile)
  else: # durationChoice == 1 for sets and reps or 2 for time-based
    return durationChoice


def promptToAddProperty(profile, propertyName):
  """Prompt user to set a parameter when creating or editing exercise"""

  clearScreen()
  print("Enter (0) to return to main menu without saving.")

  if propertyName == "Name":
    print("\nWhat should be the name of this exercise?")
    propertyValue = str(input("\nEnter your choice: "))
    if propertyValue == '':
      blankInput()
      return promptToAddProperty(profile, "Name")
    else:
      try:
        if int(propertyValue) == 0:
          mainMenu(profile)
      except ValueError:
        return propertyValue

  elif propertyName == "Category":
    print("\nChoose a category for this exercise:")
    print("\n(1) Warmup")
    print("(2) Strengthening")
    print("(3) Cardio")
    print("(4) Cooldown")

    propertyValue = None
    try:
      categoryChoice = int(input("\nEnter your choice: "))
    except ValueError:
      invalidInput()
      return promptToAddProperty(profile, "Category")
    if categoryChoice not in [0, 1, 2, 3, 4]:
      invalidInput()
      return promptToAddProperty(profile, "Category")

    if categoryChoice == 1:
      propertyValue = "Warmup"
    elif categoryChoice == 2:
      propertyValue = "Strengthening"
    elif categoryChoice == 3:
      propertyValue = "Cardio"
    elif categoryChoice == 4:
      propertyValue = "Cooldown"
    else:
      mainMenu(profile)

  elif propertyName == "Duration":
    print("\nWhat is the duration of this exercise in seconds? (60 seconds per minute, 3600 seconds per hour)")

    try:
      propertyValue = int(input("\nEnter your choice: "))
      if propertyValue == 0:
        mainMenu(profile)
    except ValueError:
      invalidInput()
      return promptToAddProperty(profile, "Duration")
    if propertyValue < 0:
      negativeInput()
      return promptToAddProperty(profile, "Duration")

  elif propertyName == "Sets":
    print("How many sets?")

    try:
      propertyValue = int(input("\nEnter your choice: "))
      if propertyValue == 0:
        mainMenu(profile)
    except ValueError:
      invalidInput()
      return promptToAddProperty(profile, "Sets")
    if propertyValue < 0:
      negativeInput()
      return promptToAddProperty(profile, "Sets")

  elif propertyName == "Reps":
    print("How many reps?")

    try:
      propertyValue = int(input("\nEnter your choice: "))
      if propertyValue == 0:
        mainMenu(profile)
    except ValueError:
      invalidInput()
      return promptToAddProperty(profile, "Reps")
    if propertyValue < 0:
      negativeInput()
      return promptToAddProperty(profile, "Reps")

  else: #Intensity
    print("\nWhat is the intensity of this exercise?\n")
    print("(1) Relaxed")
    print("(2) Standard")
    print("(3) Hardcore")

    try:
      propertyValue = int(input("\nEnter your choice: "))
      if propertyValue == 0:
        mainMenu(profile)
    except ValueError:
      invalidInput()
      return promptToAddProperty(profile, "Intensity")
    if propertyValue not in [1, 2, 3]:
      invalidInput()
      return promptToAddProperty(profile, "Intensity")

  return propertyValue


def editExercise(profile):
  """Initiates flow for user to edit an exercise associated with their profile"""

  exercise = selectExercise(profile)
  selectProperty(profile, exercise)


def selectExercise(profile):
  """Select an exercise from the list of exercises associated with the current profile"""

  clearScreen()
  print("Press (0) to return to the main menu\n")
  print("Choose an exercise:\n")
  count = 1
  for exercise in profile.exercises:
    print(f"{count}. {exercise.name}")
    count += 1

  try:
    choice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    return selectExercise(profile)
  if choice == 0:
    mainMenu(profile)
  elif choice > len(profile.exercises):
    invalidInput()
    return selectExercise(profile)
  else:
    return profile.exercises[choice - 1]


def selectProperty(profile, exercise):
  """Select a property of the selected exercise to edit."""

  clearScreen()
  Exercise.displayProperties(exercise)
  print("\nSelect a property to edit:\n")
  print("(1) Name")
  print("(2) Exercise Type")
  print("(3) Intensity")
  if not exercise.duration:
    print("(4) Sets")
    print("(5) Reps")
    print("(0) Return to the main menu")

    choice = None
    try:
      choice = int(input("\nEnter your choice: "))
    except ValueError:
      invalidInput()
      selectProperty(profile, exercise)
    if choice not in [1, 2, 3, 4, 5, 0]:
      invalidInput()
      return selectProperty(profile, exercise)
  else:
    print("(4) Duration")
    print("(0) Return to the main menu")

    choice = None
    try:
      choice = int(input("\nEnter your choice: "))
    except ValueError:
      invalidInput()
      selectProperty(profile, exercise)
    if choice not in [0, 1, 2, 3, 4, 5]:
      invalidInput()
      return selectProperty(profile, exercise)

  if choice == 0:
    mainMenu(profile)
  elif choice == 1:
    exercise.name = promptToAddProperty(profile, "Name")
  elif choice == 2:
    exercise.category = promptToAddProperty(profile, "Category")
  elif choice == 3:
    exercise.intensity = promptToAddProperty(profile, "Intensity")
  elif choice == 4 and not exercise.duration:
    exercise.sets = promptToAddProperty(profile, "Sets")
  elif choice == 4:
    exercise.duration = promptToAddProperty(profile, "Duration")
  elif choice == 5 and not exercise.duration:
    exercise.reps = promptToAddProperty(profile, "Reps")

  selectProperty(profile, exercise) # Recursive call until user selects 0 to quit


def deleteExercise(profile):
  """Prompts user to delete an exercise and then calls mainMenu()"""

  profile.exercises.remove(selectExercise(profile))
  mainMenu(profile)


def deleteProfile(profile):
  """Prompts the user to delete the current profile and calls main() to restart program"""

  clearScreen()
  print("Press (0) to return to the main menu\n")
  Profile.displayProperties(profile)

  choice = None
  try:
    choice = int(input("\nEnter (12345) to delete the current profile and restart the program.\nWARNING: This cannot be undone!\n\nEnter (0) to return to the main menu or (12345) to delete:\n"))
  except ValueError:
    invalidInput()
    deleteProfile(profile)
  if choice == 0:
    mainMenu(profile)
  elif choice != 12345:
    invalidInput()
    deleteProfile(profile)
  else: # choice == 12345
    Profile.deleteProfile(profile)
    main()


def exitProgram(profile):
  """Prompt the user to save or quit without saving and then terminate program"""

  clearScreen()
  print("Press (1) to save and exit or (2) to quit without saving.")

  choice = None
  try:
    choice = int(input("\nEnter your choice: "))
  except ValueError:
    invalidInput()
    exitProgram(profile)
  if choice not in [1,2]:
    invalidInput()
    exitProgram(profile)
  if choice == 1:
    Profile.saveProfile(profile)
    quit()
  else: # choice == 2
    quit()


def clearScreen():
  """Clears the screen"""
  # https://www.geeksforgeeks.org/python/clear-screen-python/

  system('cls' if name == 'nt' else 'clear')


def invalidInput():
  """Shows error message for invalid input and clears screen"""

  input("Invalid input. Press Enter to continue...")
  clearScreen()


def blankInput():
  """Shows error message for blank input and clears screen"""

  input("This field cannot be left blank. Press Enter to continue...")
  clearScreen()


def negativeInput():
  """Shows error message for negative integer input and clears screen"""

  input("This field cannot be a negative value. Press Enter to continue...")
  clearScreen()


def main():
  """Loads profiles into memory and calls mainMenu()"""

  allProfiles = Profile.loadAll()
  chosenProfile = promptToLoadOrCreateProfile(allProfiles)
  mainMenu(chosenProfile)

if __name__ == "__main__":
    main()
