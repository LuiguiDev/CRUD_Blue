


__name = '__main'

planets = [
    {
    'Planet': 'Mercury',
    'Clasification':'Rocky planet',
    'Distance to sun': '57 910 000 Km',
    'Day duration': '58 Earth days',
    'Moons': 'None',
     },
    {
    'Planet': 'Venus',
    'Clasification': 'Rocky planet',
    'Distance to sun': '108 200 000 Km',
    'Day duration': '116 Earth days',
    'Moons':'None'
    },
    {
    'Planet': 'Earth',
    'Clasification': 'Rocky planet',
    'Distance to sun': '150 300 000 Km',
    'Day duration': '24 hours',
    'Moons': 'Moon'
    },
    {
    'Planet': 'Mars',
    'Clasification': 'Rocky planet',
    'Distance to sun': '206 700 000 Km',
    'Day duration': '1 earth day with 37 min',
    'Moons': 'Deimos, Fobos',
    },
    {
    'Planet': 'Jupiter',
    'Clasification': 'Gaseous planet',
    'Distance to sun': '778 500 000 Km',
    'Day duration': '9 earth hours',
    'Moons': 'Europa, Ganimedes, ío, Calisto',
    },
    {
    'Planet': 'Saturn',
    'Clasification': 'Gaseous planet',
    'Distance to sun': '1 434 000 000 Km',
    'Day duration': '10 earth hours',
    'Moons': 'Titán, Encélado, Mimas',
    },
    {
    'Planet': 'Uranus',
    'Clasification': 'Gaseous planet',
    'Distance to sun': '2 871 000 000 Km',
    'Day duration': '17 earth hours',
    'Moons': 'Umbruel, Titania',
    },
    {
    'Planet': 'Neptune',
    'Clasification': 'Gaseous planet',
    'Distance to sun': '4 495 000 000 000 Km',
    'Day duration': '16 earth hours',
    'Moons': 'Tritón',
    }
]

def  create_planet(planet):
    global planets

    if planet not in planets:
        planets.append(planet)
    else:
        _planet_in_list()

def deleate_planet(planet_name):

    for planet in planets:
        if planet['Planet'] == planet_name:
            planets.remove(planet)
            return True
    else:
        _unkwnow_planet()

def update_planet(planet_name, updated_planet):

    for planet in planets:
        if planet['Planet'] == planet_name:
            index= planets.index(planet)
            planets[index]= updated_planet

    else:
        return True

def search_planet(planet_name):

    for planet in planets:
        if planet['Planet'] != planet_name:
            continue
        else:
            return True

def planets_list():
    ui_ux()
    for idx, planet in enumerate(planets):
        print('{num} | {name} | {clasification} | {distance} | {day} | {moon}'.format(
            num= idx,
            name= planet['Planet'],
            clasification= planet['Clasification'],
            distance= planet['Distance to sun'],
            day= planet['Day duration'],
            moon= planet['Moons']
        ))

def _get_planet_field(fild_name):
    fild= None
    while not fild:
        fild= input ('Write planet {}: '.format(fild_name))
    return fild

def _get_updated_field(fild_name):
    updated_fild= None
    while not updated_fild:
        updated_fild= input ('Write updated planet {}: '.format(fild_name))
    return updated_fild

def _unkwnow_planet():
    print('Planet \'{}\' is not in planet\'s list'.format(planet_name))

def _planet_in_list():
    print('Planet already is in planet\'s list')

def ui_ux(): print('-' * 30)


def _interfaz():
    print(' Welcome to BLUEDOT')
    ui_ux()
    print('What would you like to do?')

    print('[A] Add planet')
    print('[B] Deleate planet')
    print('[C] Update planet name')
    print('[D] Search planet')
    print('[E] Show planet\'s list')

if __name == '__main':
    _interfaz()

    command=input()
    command=command.upper()

                                # COMMANDS

    if command=='A':
        planet= {
        'Planet': _get_planet_field('name'),
        'Clasification': _get_planet_field('clasification'),
        'Distance to sun': _get_planet_field('distance'),
        'Day duration': _get_planet_field('day duration'),
        'Moons': _get_planet_field('moons')
        }
        create_planet(planet)
        planets_list()


    elif command=='B':
        planet_name= _get_planet_field('name')
        deleate_planet(planet_name)
        planets_list()

    elif command=='C':
        planet_name= _get_planet_field('name')
        found= search_planet(planet_name)

        if found:
            updated_planet= {
            'Planet': _get_updated_field('name'),
            'Clasification': _get_updated_field('clasification'),
            'Distance to sun': _get_updated_field('distance'),
            'Day duration': _get_updated_field('day'),
            'Moons': _get_updated_field('moons')
            }
            update_planet(planet_name, updated_planet)
            planets_list()
        else:
            _unkwnow_planet()
            planets_list()

    elif command== 'D':
        planet_name= _get_planet_field('name')
        found= search_planet(planet_name)

        if found:
            _planet_in_list()
        else:
            _unkwnow_planet()

    elif command== 'E':
        planets_list()

    else:
         print('Invalid command')
