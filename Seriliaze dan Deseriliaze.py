import pickle

class Player:

    def Sereliaze():
        example_dict ={1:"Imam",2:"Biladi",3:"2222"}

        pickle_out = open("save_seriliaze.pickle","wb")
        pickle.dump(example_dict, pickle_out)
        pickle_out.close()

    def Desereliaze(nomor):

        pickle_in= open("save_seriliaze.pickle","rb")
        example_dict = pickle.load(pickle_in)

        pickle_in.close()

        print(example_dict[nomor])
        print("Setelah deserelization")
   ###     print(example_dict)
    def Read():
        pickle_in = open("save_seriliaze.pickle", "rb")
        example_dict = pickle.load(pickle_in)
        file2 = open("save.txt", "a")
        file2.write(str(example_dict) + "\n")
        file2.close()
    if __name__ == '__main__':
        Sereliaze()
        Desereliaze(1)
        Desereliaze(2)
        Desereliaze(3)
        Read()
