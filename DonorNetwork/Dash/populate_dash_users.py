import os
from django.contrib.auth.models import User


def populate():

    add_user('abc1234', 'CG9hFLBa', email='abc1234@gmail.com', website='abc1234.com')
    
    # Print out what we have added to the user.
    for u in User.objects.all():
        print("{}".format(str(u)))

def add_user(username, password, email, website):
    u = User.objects.get_or_create(username=username,
                                   password=password,
                                   email=email,
                                   website=website)[0]    
    return u


# Start execution here!
if __name__ == '__main__':
    print("Starting Dash population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DonorNetwork.settings')
    populate()
