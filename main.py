import subprocess


def main():
    res_b = subprocess.check_output(["git", "log", "--pretty=oneline"])
    res = str(res_b.decode())
    print(res)


if __name__ == '__main__':
    main()
