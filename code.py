def valid_username(username):
    # Requirement 1: Username must be ten characters or less
    if len(username) > 10:  
        return False  
    
    # Requirement 2: Username must only contain alphanumeric characters
    if not username.isalnum():
        return False

    # Requirement 3: Username must not contain "<" or ">"
    if "<" in username or ">" in username:
        return False
    
    # If all the requirements are met, system returns True
    return True

# Sample Input
test_usernames = [
    "Bob123", # valid
    "John!", # invalid: contains ("!")
    "Alice1234567", # invalid: (exceeds ten characters)
    "Megan>Charles", # invalid: contains ("<")
    "JaneSmith1" # valid
    ]

# Print output for each username
for name in test_usernames:
    print(name, "=>", valid_username(name))