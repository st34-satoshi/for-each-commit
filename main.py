import subprocess


def main():
    # TODO: if you want to change a branch.
    # # checkout new branch. not to break commit
    # subprocess.call(["git", "checkout", "for-each-commit"])
    # subprocess.call(["git", "checkout", "-b", "for-each-commit"])

    # create log list. the list has only commit hash
    res_b = subprocess.check_output(["git", "log", "--pretty=oneline"])
    res = str(res_b.decode())
    log_list = [s.split(" ")[0] for s in res.split("\n") if len(s) > 1]  # log is only commit hash. avoid last new line

    # do command for each commit
    for commit in log_list:
        print("commit = {0}".format(commit))
        subprocess.call(["git", "reset", "--hard", commit])
        command()


def command():
    # TODO implement: this is a example. implement a function what you want
    # output number of all files line
    # get files
    files = subprocess.check_output(["git", "ls-files"]).decode()
    file_list = [s for s in files.split("\n") if len(s) > 1]
    total_line = 0
    for file in file_list:
        # add line number of this file.
        result_wc = subprocess.check_output(["wc", file]).decode().split(' ')
        for s in result_wc:
            if len(s) > 0:
                total_line += int(s)
                break
    print(total_line)


if __name__ == '__main__':
    main()
