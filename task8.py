import os

def find(path: str) -> list:
    res = []
    files = os.listdir(path)
    for i in files:
        if os.path.isdir(path + "/" + i):
            res += find(path + "/" + i)
        else:
            res.append(i)
    return res

print(find("C:/Users/X1/Downloads"))