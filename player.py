import pickle


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


def process_user():
    """
    Gets the username, checks for any previous player info and loads the player. If no player
    file it creates a new one. Returns a Player object.
    """
    name = input('Please enter your name > ')
    userfile = name + '.dat'
    print('\n')
    try:
        with open(userfile, 'rb') as f:
            print('Loading the player file...')
            user = pickle.load(f)
            return user

    except IOError:
        print('This user doesn\'t seem to have an account...')
        print('Creating a new player file.')
        return Player(name=name)


def save_user(user, directory):
    """
    Saves the players current stats to file.
    """
    userfile = directory + user.name + '.dat'
    print('Saving player file... ')

    try:
        with open(userfile, 'wb') as f:
            pickle.dump(user, f)
    except IOError:
        print('An error occurred while writing the player info!')
