import pickle

class Player:

    def Sereliaze():
        example_dict ={1:"6",2:"2",3:"f"}

        pickle_out = open("save_data.pickle","wb")
        pickle.dump(example_dict, pickle_out)
        pickle_out.close()

    def Desereliaze(nomor):

        pickle_in= open("save_data.pickle","rb")
        example_dict = pickle.load(pickle_in)

        pickle_in.close()
        print("Setelah deserelization")
        print(example_dict[nomor])


    if __name__ == '__main__':
        Desereliaze(2)