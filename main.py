import hashlib


def calculate_hash(func_string, algorithm):
    # Calculate the hash of the string
    if algorithm == "md5":
        h = hashlib.md5()
    elif algorithm == "sha1":
        h = hashlib.sha1()
    elif algorithm == "sha256":
        h = hashlib.sha256()
    else:
        raise ValueError("Invalid hash algorithm")
    h.update(func_string.encode())
    return h.hexdigest()


# Test the hash calculator
string = "Hello, World!"
out_hash = calculate_hash(string, "sha256")
print(f"The SHA-256 hash of '{string}' is {out_hash}")
