import random
import string


def get_account_number():
    return "44" + str(random.randrange(00000000,99999999))

def generate_reference():
    return "anime" + str(random.shuffle([string.ascii_letters + string.digits][ :30]))