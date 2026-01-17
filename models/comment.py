class Comment:
    """
    A class to represent a Comment on the wall.
    """

    def __init__(self, author, content):
        self.author = author  # the author of the comment
        self.content = content  # the content of the comment
        self.timestamp = self.current_time()  # timestamp of the comment

    def current_time(self):
        import datetime
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'{self.timestamp} - {self.author}: {self.content}'
