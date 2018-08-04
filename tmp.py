class User:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body


a1 = User(1, 'Article 1 title', 'Article 1 body')
a2 = User(2, 'Article 2 title', 'Article 2 body')
aList = [a1, a2]
