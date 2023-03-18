import hashlib

ha = hashlib.md5('hello'.encode('utf-8')).hexdigest()
print('===>', ha)


