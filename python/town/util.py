from .portal_hub import portal_hub
from .guild import guild_building
from .home import home
from .hunter_association import hunter_association_building
from .main import town

def travel_to(location:str):
    locations = {
        "home": home,
        "portal hub": portal_hub,
        "town": town,
        "guild": guild_building,
        "hunter association": hunter_association_building
    }
    action = locations.get(location)
    if action:
        action()
    