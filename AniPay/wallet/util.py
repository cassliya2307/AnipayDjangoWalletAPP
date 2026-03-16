import random
import string


def get_account_number():
    return "44" + str(random.randrange(00000000,99999999))

def generate_reference():
    return "anipay" + "".join(random.choices(string.ascii_uppercase + string.digits, k=4))