import time


def main():
    while True:
        print("loop sleep")
        time.sleep(60 * 60)  # sleep one hour


if __name__ == "__main__":
    print("started")
    main()