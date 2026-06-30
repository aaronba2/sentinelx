from datetime import datetime, timedelta

failed_attempts = {}
blocked_ips = {}

MAX_ATTEMPTS = 5
BLOCK_TIME = 300  # 5 minutes


def is_blocked(ip: str):

    if ip not in blocked_ips:
        return False

    if datetime.now() > blocked_ips[ip]:
        del blocked_ips[ip]
        failed_attempts[ip] = 0
        return False

    return True


def login_failed(ip: str):

    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    if failed_attempts[ip] >= MAX_ATTEMPTS:
        blocked_ips[ip] = datetime.now() + timedelta(seconds=BLOCK_TIME)


def login_success(ip: str):

    failed_attempts[ip] = 0
