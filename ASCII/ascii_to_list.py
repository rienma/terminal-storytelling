#IMPORT
import pickle, os

#FUNCTIONS
def open_ascii_txt_file(name):
    with open(name) as file:
        return file.readlines()

def pickle_ascii_list(list,output_name):
    with open(output_name, 'wb') as f:
        pickle.dump(list, f, protocol=2)
        print('Done for {}'.format(output_name))

#PATH
root_path = os.path.dirname(os.getcwd())
path = root_path+"/ASCII/"
path_out = root_path+"/MESSAGE/"

#ASCII -> LIST
files = [file for file in os.listdir(path) if '.txt' in file]
[pickle_ascii_list(open_ascii_txt_file(path+file),path_out+file[:-4]) for file in files]
