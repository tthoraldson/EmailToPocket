import sys
from gmail import Gmail

print('Please enter username')
username = raw_input()

print()
# password
print('Please enter the password for ' + username)
password = raw_input()

g = Gmail()
g.login(username, password)

g.inbox().mail(sender="noreply@medium.com")

# cleanup, logout, and exit
g.logout()
sys.exit()
