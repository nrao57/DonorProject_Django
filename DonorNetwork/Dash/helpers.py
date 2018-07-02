#These are functions that add shortcuts to the view.py
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def safe_get(reqwuser, verbose=False):
    dict_out = {}
    try:
        dict_out['user'] = User.objects.get(username=reqwuser.user)
    except ObjectDoesNotExist as e:
        if verbose:
            print(e)
        dict_out['user']=None

    return dict_out
