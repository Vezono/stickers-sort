import heroku3

from config import heroku_key


class Heroku():
    def __init__(self, bot):
        self.bot = bot
        self.app = heroku3.from_key(heroku_key).apps()['lk-contest']
        self.last_log = ''
