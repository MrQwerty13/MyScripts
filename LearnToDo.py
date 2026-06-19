import os as os


def main():
    path_to_script = os.path.dirname(os.path.realpath(__file__))
    print(path_to_script)

    path = (str(path_to_script)).split("/")
    print(path)

    os.chdir(f"/{path[1]}/{path[2]}/{path[3]}/{path[4]}/{path[5]}")
    print(os.getcwd())

    os.mkdir("Output")
    os.chdir("Output")

    os.system('touch out1.txt')

    os.system('echo "Hello World" >> out1.txt')

    print("Done")

if __name__ == "__main__":
    main()