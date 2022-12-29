from Handlers import Handler

class KeyPress(Handler):

    def analyze(self, event, e):
        print(e.key)