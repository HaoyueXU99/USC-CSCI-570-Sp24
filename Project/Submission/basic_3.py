import sys
import time
import psutil


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed

def time_wrapper():
    start_time = time.time()
    dp()
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    return time_taken

def dp():
    for row in range(1, l1 + 1):
        memo[row][0] = row * DELTA
    for col in range(1, l2 + 1):
        memo[0][col] = col * DELTA
    for row in range(1, l1 + 1):
        for col in range(1, l2 + 1):
            memo[row][col] = min(memo[row - 1][col] + DELTA, memo[row][col - 1] + DELTA,
                                 memo[row - 1][col - 1] + ALPHA[str1[row - 1] + "_" + str2[col - 1]])

    s1 = []
    s2 = []
    row = l1
    col = l2
    while row > 0 or col > 0:
        if memo[row][col] == memo[row - 1][col] + DELTA:
            s1.append(str1[row - 1])
            s2.append("_")
            row -= 1
        elif memo[row][col] == memo[row][col - 1] + DELTA:
            s1.append("_")
            s2.append(str2[col - 1])
            col -= 1
        else:
            s1.append(str1[row - 1])
            s2.append(str2[col - 1])
            col -= 1
            row -= 1
    s1.reverse()
    s2.reverse()
    alignment.append("".join(s1))
    alignment.append("".join(s2))


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    ALPHA = {"A_A": 0, "A_C": 110, "A_G": 48, "A_T": 94,
             "C_A": 110, "C_C": 0, "C_G": 118, "C_T": 48,
             "G_A": 48, "G_C": 118, "G_G": 0, "G_T": 110,
             "T_A": 94, "T_C": 48, "T_G": 110, "T_T": 0}
    DELTA = 30

    with open(input_file_path, "r") as f:
        lines = f.readlines()
    strs = []
    cur = ""
    for line in lines:
        line = line.strip("\n")
        if line.isdigit():
            cur = cur[:int(line) + 1] + cur[:] + cur[int(line) + 1:]
        else:
            if cur != "":
                strs.append(cur)
            cur = line
    strs.append(cur)
    str1, str2 = strs

    l1 = len(str1)
    l2 = len(str2)
    memo = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    alignment = []
    time_assuming = time_wrapper()
    memory = process_memory()
    min_alignment = memo[l1][l2]
    # print(alignment, min_alignment)
    # print(memo)
    with open(output_file_path, "w+") as f:
        f.writelines(str(min_alignment) + "\n")
        f.writelines(alignment[0] + "\n")
        f.writelines(alignment[1] + "\n")
        f.writelines(str(time_assuming) + "\n")
        f.writelines(str(memory))