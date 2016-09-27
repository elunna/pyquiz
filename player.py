import pickle
import os

DATADIR = 'data/'


class Player():
    def __init__(self, name):
        self.name = name
        self.solved = 0
        self.guesses = 0

    def __str__(self):
        return self.name

    def info(user):
        """
        Displays the player's information
        """
        print('Showing data for {}'.format(user.name))
        print('Score: {}'.format(user.solved))
        print('Guesses: {}'.format(user.guesses))


def ensure_datadir():
    d = os.path.dirname(DATADIR)
    if not os.path.exists(d):
        os.makedirs(d)


def load_player(name):
    """
    Gets the username, checks for any previous player info and loads the player. If no player
    file it creates a new one. Returns a Player object.
    """
    userfile = DATADIR + name + '.dat'
    try:
        with open(userfile, 'rb') as f:
            print('Loading the player file...')
            p = pickle.load(f)
            return p

    except IOError:
        print('No player found!')
        return None


def save_user(user):
    """
    Saves the players current stats to file.
    """
    userfile = DATADIR + user.name + '.dat'
    print('Saving player file... ')
    ensure_datadir()

    try:
        with open(userfile, 'wb') as f:
            pickle.dump(user, f)
    except IOError:
        print('An error occurred while writing the player info!')
