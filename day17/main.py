class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0

    def increase_followers(self):
        self.followers = +1


user_1 = User(45, 'Anne')
user_1.increase_followers()

# user_1.id = '011'
# print(user_1.id)

user_2 = User(34, "john")


print(user_1.user_id)
print(user_1.user_name)
print(user_1.followers)

print(user_1.followers)
