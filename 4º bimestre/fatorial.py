def fat(num):
    if num <= 1:
        return 1
    return num * fat(num - 1)
print (fat(5))