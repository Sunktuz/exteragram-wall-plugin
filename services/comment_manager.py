# comment_manager.py

class CommentManager:
    def __init__(self):
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def remove_comment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)

    def get_comments(self):
        return self.comments

    def clear_comments(self):
        self.comments.clear()