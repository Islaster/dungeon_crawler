building_cache = None

def get_buildings():
    global building_cache
    from town.portal_hub import portal_hub
    from town.guild import guild_building
    from town.home import home
    from town.hunter_association import hunter_association_building
    from town.main import town

    building_cache = {
        "portals": portal_hub,
        "guild": guild_building,
        "home": home,
        "hunter_association": hunter_association_building,
        "town": town
    }

    return building_cache