import shutil
import os

def copy_file(source, file_type, destination):

    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    for f in files:
        if f.endswith(file_type):
            shutil.copy(f,destination)
            print("Copied:{0}".format(f))

if __name__ == "__main__":
    copy_file('./source','txt','./destination')