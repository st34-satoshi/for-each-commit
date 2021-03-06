import subprocess
import sys


def main():
    # get path
    path_dir = "./"
    if len(sys.argv) < 2:
        print("Error: no path to directory")
        exit()
    else:
        path_dir = sys.argv[1]

    # TODO: if you want to change a branch.
    # # checkout new branch. not to break commit
    # subprocess.call(["git", "checkout", "for-each-commit"])
    # subprocess.call(["git", "checkout", "-b", "for-each-commit"])

    # create log list. the list has only commit hash
    res_b = subprocess.check_output(["git", "-C", path_dir, "log", "--pretty=oneline"])
    res = str(res_b.decode())
    log_list = [s.split(" ")[0] for s in res.split("\n") if len(s) > 1]  # log is only commit hash. avoid commit comment
    log_list.reverse()  # from initial commit

    # do command for each commit
    for i, commit in enumerate(log_list):
        print("commit = {0}".format(commit))
        subprocess.call(["git", "-C", path_dir, "reset", "--hard", commit])
        command(path_dir)


def command(path_dir):
    # TODO implement: this is a example. implement a function what you want
    # output number of all files line
    # get files
    files = subprocess.check_output(["git", "-C", path_dir, "ls-files"]).decode()
    file_list = [s for s in files.split("\n") if len(s) > 1]
    total_line = 0
    for file in file_list:
        # add line number of this file.
        result_wc = subprocess.check_output(["wc", path_dir + file]).decode().split(' ')
        for s in result_wc:
            if len(s) > 0:
                total_line += int(s)
                break
    print(total_line)


if __name__ == '__main__':
    main()
