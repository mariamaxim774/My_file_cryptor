import os
import os.path
import sys
import hashlib


class FileHandler:
    def __init__(self,filename):
        self.filename=filename
    def is_file(self):
        path_to_file = self.search_file()
        if path_to_file and os.path.isfile(path_to_file):
            return True
        else:
            return False
    def search_file(self):
        for root,directories,files in os.walk("C:\\"):
            if self.filename in files:
                return os.path.join(root,self.filename)
        else:
            return None
class FileCryptor:
    def __init__(self,filename,password):
        self.filename=filename
        self.password=password
    def crypt(filename):
        print('In crypt')
    def  decrypt(filename):
        print('In decrypt')
    def compute_hash(self):
        hasher=hashlib.sha3_256()
        with open(self.filename,'rb') as f:
            print(hasher.block_size())
def main():
    if len(sys.argv)!=4:
        return 'Trebuie sa apelezi scriptul astfel: python main.py <crypt>/<decrypt> filename password'
        sys.exit(1)

    command = sys.argv[1]
    file=sys.argv[2]
    password=sys.argv[3]


    fileHandler=FileHandler(file)
    if not fileHandler.is_file():
        return 'Fisierul nu exista, dati un fisier valid'
        sys.exit(1)
    else:
        cryptor = FileCryptor(file,password)
        if command=='crypt':
            cryptor.compute_hash()
            #exit_file=cryptor.crypt()
        elif command=='decrypt':
            #exit_file=cryptor.decrypt()
        else:
            return 'Singurele comenzi ce pot fi apelate sunt <crypt> si <decrypt>'

if __name__ == '__main__':
    main()

