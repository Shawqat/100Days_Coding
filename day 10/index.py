# Goals : 
# Understand when to use each data structure
# Learn to analyze problem requirements to pick the best tool
# Practice combining data structures for complex problems
# Develop intuition for performance considerations

# Does order matter? → List or Tuple
# Will data change? → Mutable (List, Set, Dict) vs Immutable (Tuple)
# Need fast lookups? → Dictionary or Set
# Dealing with key-value pairs? → Dictionary
# Need uniqueness? → Set
# Performance critical? → Consider time complexity

# A simple social network model
social_network = {
    "users": {
        "alice": {
            "friends": {"charlie"},  # Set for fast lookups
            "posts": [                       # List for ordered timeline
                {"content": "Hello world!", "likes": {"bob"}},
                {"content": "Python is fun!", "likes": {"bob", "charlie"}}
            ],
            "profile": ("Alice", "Developer", "NYC")  # Tuple for fixed info
        },
        "bob": {
            "friends": {"charlie"},
            "posts": [],
            "profile": ("Bob", "Designer", "LA")
        }
    },
    "all_usernames": {"alice", "bob", "charlie"}  # Quick username availability check
}

# Access patterns
def add_friend(user1, user2):
    social_network["users"][user1]["friends"].add(user2)
    social_network["users"][user2]["friends"].add(user1)

def get_mutual_friends(user1, user2):
    return social_network["users"][user1]["friends"] & social_network["users"][user2]["friends"]

# Test it
add_friend("alice", "bob")
print(f"Alice's friends: {social_network['users']['alice']['friends']}")
print(f"Mutual friends (Alice & Bob): {get_mutual_friends('alice', 'bob')}")