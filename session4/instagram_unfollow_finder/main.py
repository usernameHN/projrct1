import instaloader
import getpass
l = instaloader.Instaloader()

f = open("session4/instagram_unfollow_finder/followers.txt")
old_followers = []
follower_new = []
for line in f:
    old_followers.append(line)
f.close()

username = input("enter username :")

password = getpass.getpass("enter password :")

l.login(username, password)
print("good job")
profile = instaloader.Profile.from_username(l.context, "hosein_hn_boe")

new_followers = []
for follower in profile.get_followees():
    new_followers.append(follower)

for old_follower in old_followers:
   if old_follower not in new_followers:
   #if new_followers not in old_follower :     

        print(old_follower)
       # print(new_followers)

f = open("session4/instagram_unfollow_finder/followers.txt")
for follower in new_followers:
    f.write(follower + "\n")

f.close
