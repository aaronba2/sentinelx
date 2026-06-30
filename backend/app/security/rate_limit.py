ATTEMPTS={}

def allow(ip):

    ATTEMPTS[ip]=ATTEMPTS.get(ip,0)+1

    if ATTEMPTS[ip]>5:
        return False

    return True
