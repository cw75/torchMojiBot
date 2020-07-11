import Algorithmia
from Algorithmia.acl import ReadAcl

import sys

if __name__ == '__main__':
    if not len(sys.argv) == 1:
        print('Usage: python3 data.py')
        sys.exit(1)

    user_name = input("Enter Algorithmia user name: ")
    api_key = input("Enter Algorithmia API key: ")

    client = Algorithmia.client(api_key)
    dir_name = 'data://' + user_name + '/emojize'
    collection = client.dir(dir_name)
    collection.create(ReadAcl.public)
    client.file(dir_name + '/vocabulary.json').putFile('model/vocabulary.json')
    client.file(dir_name + '/pytorch_model.bin').putFile('model/pytorch_model.bin')

    print('Model files successfully uploaded!')