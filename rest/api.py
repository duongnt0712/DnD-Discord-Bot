import requests

api = {
  "url": "https://www.dnd5eapi.co/api",
  "paths": {
    "classes": "/classes",
    "subclasses": "/subclasses",
    "spells": "/spells",
    "features": "/features",
    "monsters": "/monsters",
    "damage-types": "/damage-types",
    "magic-schools": "/magic-schools",
    "proficiencies": "/proficiencies",
    "ability-scores": "/ability-scores",
    "equipment": "/equipment",
    "equipment-categories": "/equipment-categories"
  }
}

# Constants API
CLASSES_URL = api['url'] + api['paths']['classes']
SUBCLASSES_URL = api['url'] + api['paths']['subclasses']
SPELLS_URL = api['url'] + api['paths']['spells']
FEATURES_URL = api['url'] + api['paths']['features']
MONSTERS_URL = api['url'] + api['paths']['monsters']
DAMAGE_TYPES_URL = api['url'] + api['paths']['damage-types']
MAGIC_SCHOOLS_URL = api['url'] + api['paths']['magic-schools']
PROFICIENCIES_URL = api['url'] + api['paths']['proficiencies']
ABILITY_SCORES_URL = api['url'] + api['paths']['ability-scores']
EQUIPMENT_URL = api['url'] + api['paths']['equipment']
EQUIPMENT_CATEGORIES_URL = api['url'] + api['paths']['equipment-categories']

# Get API
def req_get_classes():
   return requests.get(CLASSES_URL)

def req_get_subclasses():
   return requests.get(SUBCLASSES_URL)

def req_get_spells():
   return requests.get(SPELLS_URL)

def req_get_spells_by_index(index):
   print(SPELLS_URL + index)
   return requests.get(SPELLS_URL + index)

# Commons
def convert_to_json(response):
  return response.json()

# Classes
def res_count_classes():
  response = convert_to_json(req_get_classes())
  return response['count']

def res_get_all_classes():
  response = convert_to_json(req_get_classes())
  classes = ""
  for res in response['results']:
      classes += res['name'] + ', '
  return classes

# Subclasses
def res_count_subclasses():
  response = convert_to_json(req_get_subclasses())
  return response['count']

def res_get_all_subclasses():
  response = convert_to_json(req_get_subclasses())
  subclasses = ""
  for res in response['results']:
      subclasses += res['name'] + ', '
  return subclasses

#Spells
def res_get_specific_spells(index):
  response = convert_to_json(req_get_spells_by_index(index))
  return response