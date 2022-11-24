import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("output.txt", "w")
    counter = 0
    while True:
        time.sleep(1)
        counter = counter + 1
        f.write(str(counter)+"\n")
        print("printed to file")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
