from .api import get_buildings
def travel_to(location:str):
    locations = get_buildings()
    action = locations.get(location)
    if action:
        action()
    