import requests
from hashlib import sha1
from sys import argv, exit
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code}, check the api and try again')
    return res

def pass_leak_count(hashes, our_hash):
    hash = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hash:
        if h == our_hash:
            return count
    # return 0

def hash_password(password):
    sha1_password = sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    # print(pass_leak_count(response, tail))
    return pass_leak_count(response, tail)

def main(args):
    for password in args:
        count = hash_password(password)
        if count:
            print(f"{password} was found {count} times. ")
        else:

            print(f"{password} secured, continue")
    return "done!"
if __name__ == "__main__":
    exit(main(argv[1:]))

