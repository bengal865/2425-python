class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

taylor = User('taylor', 'swift', 't_swift', 't_swift@gmail.com', 'colorado')
taylor.describe_user()
taylor.greet_user()

print("\nTrying to log in three times...")
taylor.increment_login_attempts()
taylor.increment_login_attempts()
taylor.increment_login_attempts()
print("  Number of login attempts: " + str(taylor.login_attempts))

print(f"Resetting login attempts for {taylor.last_name}, {taylor.first_name}...")
taylor.reset_login_attempts()
print("  Number of login attempts: " + str(taylor.login_attempts))
