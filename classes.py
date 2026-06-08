from dataclasses import dataclass, asdict
from json import dump, load, decoder

@dataclass
class Exercise:
  """Dataclass for each exercise created by the user"""

  _name: str # Name of exercise
  _category: str # Warmup, Strengthening, Cardio, Cooldown
  _intensity: int # Relaxed, Standard, Hardcore
  _duration: int = None # Duration in seconds or None for sets and reps
  _sets: int = None # Number of sets to complete or None for duration
  _reps: int = None # Number of reps per set or None for duration

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, value: str):
    self._name = value

  @property
  def category(self) -> str:
    return self._category
  @category.setter
  def category(self, value: str):
    self._category = value

  @property
  def intensity(self) -> int:
    return self._intensity
  @intensity.setter
  def intensity(self, value: int):
    self._intensity = value

  @property
  def duration(self) -> int:
    return self._duration
  @duration.setter
  def duration(self, value: int):
    self._duration = value

  @property
  def sets(self) -> int:
    return self._sets
  @sets.setter
  def sets(self, value: int):
    self._sets = value

  @property
  def reps(self) -> int:
    return self._reps
  @reps.setter
  def reps(self, value: int):
    self._reps = value


  def displayProperties(self):
    """Display the properties of the exercise"""

    print(f"Name: {self.name}")
    print(f"Type: {self.category}")
    if self.intensity == 1:
      print("Intensity: Relaxed")
    elif self.intensity == 2:
      print("Intensity: Standard")
    else:
      print("Intensity: Hardcore")
    if self.duration:
      if self.duration > 60:
        print(f"Duration: {int(self.duration / 60)} minutes and {self.duration % 60} seconds")
      else:
        print(f"Duration: {self.duration} seconds")
    elif self.sets:
      print(f"Sets: {self.sets}")
      print(f"Reps: {self.reps}")



@dataclass
class Profile:
  """Dataclass for each profile created by the user"""

  _name: str # Name of profile
  _exercises: list[Exercise] # List of exercises associated with the profile

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, value: str):
    self._name = value

  @property
  def exercises(self) -> list:
    return self._exercises
  @exercises.setter
  def exercises(self, value: list):
    self._exercises = value

  @staticmethod
  def loadAll() -> list:
    """Load profiles into memory from profiles."""
    try:
      with open("profiles.json", 'r') as profilesJson:
        try:
          loadedProfiles = load(profilesJson)
        except decoder.JSONDecodeError:
          return []
        return [Profile(**x) for x in loadedProfiles]
    except FileNotFoundError:
      return []


  def loadProfile(self):
    """Convert list of dictionaries in self.exercises into list of Exercise objects"""

    self.exercises = [Exercise(**x) for x in self.exercises]
    return self


  def displayProperties(self):
    """Display the properties of the profile"""

    print(f"Name: {self.name}")
    print(f"Number of exercises: {len(self.exercises)}\n")



  # TODO: Combine deleteProfile and saveProfile into saveOrDelete(self, deleteOrSave)
  
  def deleteProfile(self):
    """Delete the current profile from the profiles.json file"""
    # Adapted from https://stackoverflow.com/a/68929467

    profiles = [asdict(x) for x in Profile.loadAll()] # Load profiles from profiles.json into profileList
    profiles[:] = [d for d in profiles if d.get('_name') != self.name] # Remove current profile from profileList
    with open("profiles.json", 'w') as f:
      dump(profiles, f) # Dump profileList as a JSON object into profiles.json


  def saveProfile(self):
    """Save modified profile into profiles.json"""
    # Adapted from https://stackoverflow.com/a/68929467

    profiles = [asdict(x) for x in Profile.loadAll()] # Load profiles from profiles.json into profileList
    profiles[:] = [d for d in profiles if d.get('_name') != self.name] # Remove current profile from profileList
    profiles.append(asdict(self)) # Converts current profile with changes to dictionary and appends to profileList
    with open("profiles.json", 'w') as f:
      dump(profiles, f)   # Dump profileList as a JSON object into profiles.json
