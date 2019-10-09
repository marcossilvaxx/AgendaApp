import json

def main():
    while True:
        try:
            f = open("months.txt", "r", encoding='utf-8')
            lines = f.readlines()

            for line in lines:
                print(line.strip())
            break
        except FileNotFoundError:
            print("File not found.")

if __name__ == "__main__":
    main()
