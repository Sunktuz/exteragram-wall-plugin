class UserProfile:
    def __init__(self, username, email, bio=None, profile_picture=None):
        self.username = username
        self.email = email
        self.bio = bio
        self.profile_picture = profile_picture

    def __str__(self):
        return f"UserProfile(username={self.username}, email={self.email}, bio={self.bio}, profile_picture={self.profile_picture})"

    def update_profile(self, bio=None, profile_picture=None):
        if bio is not None:
            self.bio = bio
        if profile_picture is not None:
            self.profile_picture = profile_picture

    def get_profile_info(self):
        return {
            'username': self.username,
            'email': self.email,
            'bio': self.bio,
            'profile_picture': self.profile_picture
        }