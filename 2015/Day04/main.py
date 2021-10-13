import hashlib


def day_4(data: str,part: int):
    x = 5 if part == 1 else 6
    nonce = 0
    while not hashlib.md5((data+str(nonce)).encode()).hexdigest().startswith(x*'0'):
        nonce += 1
    print(nonce)


if __name__ == '__main__':
    data="yzbqklnj"
    day_4(data, 1)
