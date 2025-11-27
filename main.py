# School clubs using dictionaries.
from pyscript import document, display

# Putting more than one "getting_info" so that the buttons can work properly without an error.
# Military Club
def getting_info1(e):
    document.getElementById('output').innerHTML = " "
    military_club = {
        'club name': 'Military Club',
        'description': 'We learn military drills, fighting skills, and survival skills. And take note, this is serious and not fun, but we keep it from simplified all the way to advanced training.',
        'meeting_time': '2:00 pm to 3:00 pm',
        'location': 'Room 901',
        'club_moderator': 'Sgt Peppers',
        'number_of_members': '100'
    }

    # Displaying the information
    display(military_club['club name'], target='output')
    display(f'Description:', military_club['description'], target='output')
    display(f'Meeting Time:', military_club['meeting_time'], target='output')
    display(f'Location:', military_club['location'], target='output')
    display(f'Club Moderator:', military_club['club_moderator'], target='output')
    display(f'Number of Members:', military_club['number_of_members'], target='output')

# Entertainment Club
def getting_info2(e):
    document.getElementById('output').innerHTML = " "
    entertainment_club = {
        'club name': 'Entertainment Club',
        'description': 'We learn how to act, dance, sing, do content, and many more.',
        'meeting_time': '2:00 pm to 3:00 pm',
        'location': 'Room 607',
        'club_moderator': 'Mr. Smiley',
        'number_of_members': '200'
    }

    # Displaying the information
    display(entertainment_club['club name'], target='output')
    display(f'Description:', entertainment_club['description'], target='output')
    display(f'Meeting Time:', entertainment_club['meeting_time'], target='output')
    display(f'Location:', entertainment_club['location'], target='output')
    display(f'Club Moderator:', entertainment_club['club_moderator'], target='output')
    display(f'Number of Members:', entertainment_club['number_of_members'], target='output')

# Math and Science Club
def getting_info3(e):
    document.getElementById('output').innerHTML = " "
    math_and_science = {
        'club name': 'Math and Science Club',
        'description': 'We learn Chemistry, Physics, Engineering, Biology, Earth/Space, and many things to explore in a fun and interactive way.',
        'meeting_time': '2:00 pm to 3:00 pm',
        'location': 'Room 711',
        'club_moderator': 'Mr. Garrison',
        'number_of_members': '150'
    }

    # Displaying the information
    display(math_and_science['club name'], target='output')
    display(f'Description:', math_and_science['description'], target='output')
    display(f'Meeting Time:', math_and_science['meeting_time'], target='output')
    display(f'Location:', math_and_science['location'], target='output')
    display(f'Club Moderator:', math_and_science['club_moderator'], target='output')
    display(f'Number of Members:', math_and_science['number_of_members'], target='output')

#References: Codes from w3schools.com