"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.
"""

from model import db, Human, Animal


def get_human_2():
    """Return the human with the id 2."""

    return Human.query.filter(Human.human_id == 2).one()

def get_first_fish():
    """Return the FIRST animal with the species 'fish'."""

    return Animal.query.filter(Animal.animal_species == 'fish').first()


def get_young_animals():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """

    return Animal.query.filter(Animal.birth_year > 2015).all()

def get_j_names():
    """Return the humans with first names that start with 'J'."""

    return Human.query.filter(Human.fname.like('J%')).all()


def get_null_bdays():
    """Return all animals whose birth years are NULL."""

    return Animal.query.filter(Animal.birth_year == None).all()


def get_fish_or_rabbits():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    return Animal.query.filter( (Animal.animal_species == 'fish') | 
                                (Animal.animal_species == 'rabbit') ).all()


def print_directory():
    """Output a list of humans and their animals.

    For example:

    >>> print_directory()
    Justin Time
    - Peter (rabbit)
    - Peppa (pig)
    Carmen Sandiego
    - Blub (fish)

    You may only use ONE query to retrieve initial data. (Hint: leverage a
    SQLAlchemy relationship to retrieve additional information)
    """

    # directory = db.session.query(Animal.human_id).group_by(Animal.human_id).all()
    # directory = db.session.query(Animal).join(Human).group_by(Human.human_id).all()
    # directory = db.session.query(Human).outerjoin(Animal).group_by(Human.human_id).all()
    # directory = db.session.query(Animal).all() 
    
    directory = db.session.query(Human).all() #(╯°□°)╯︵ ┻━┻ I overthought this LOL

    for person in directory:
        pets = person.animal
        print(f'{person.fname} {person.lname}')
        
        for pet in pets:
            print(f'- {pet.name} ({pet.animal_species})')


def find_humans_by_animal_species(species):
    """Return a list of all humans who have animals of the given species.

    Each human should only appear once in the returned list. For example:

    >>> find_humans_by_animal_species('snake')

    Again, you may only use ONE query to retrieve initial data. (Hint: use a
    relationship! Also, you can pursue uniqueness in a Pythonic way --- you
    don't have to do it with pure SQLAlchemy)
    """
    #this returns a list as objects, if the list was supposed to only return names
    #would have simply changed parameters within .query() and group_by() to be 
    #Human.fname, Human.lname
    directory = db.session.query(Human).join(Animal).filter_by(animal_species=species
                ).group_by(Human).all()
    
    return directory


if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
