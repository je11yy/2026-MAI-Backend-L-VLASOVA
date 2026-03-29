import random
import string
import time
from urllib.parse import parse_qs

SPECIALS = "#[]().,!@&^%*"

def generate_password(length: int) -> str:
    if length < 8:
        length = 8
    if length > 16:
        length = 16

    password_chars = [
        random.choice(string.digits),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(SPECIALS),
    ]

    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase + SPECIALS

    for _ in range(length - 4):
        password_chars.append(random.choice(alphabet))

    random.shuffle(password_chars)
    return "".join(password_chars)


def app(environ, start_response):
    query = parse_qs(environ.get("QUERY_STRING", ""))
    raw_length = query.get("length", ["12"])[0]

    try:
        length = int(raw_length)
    except ValueError:
        length = 12

    password = generate_password(length)

    body = (password + "\n").encode("utf-8")
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]

    time.sleep(0.05)

    start_response(status, headers)
    return [body]