
def read_credentials(path: str) -> (str, str):
    """
    Reads file given at path with format name=value
    """
    with open(path, 'r') as f:
        user, pw = "", ""
        for line in f.readlines():
            if "user" in line:
                user = line.split('=')[1].strip()
            elif "pw" in line:
                pw = line.split('=')[1].strip()
    print(user, pw)
    return (user, pw)


