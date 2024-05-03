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
    min_alignment, alignment1, alignment2 = efficient(str1, str2)
    alignment.append(min_alignment)
    alignment.append(alignment1)
    alignment.append(alignment2)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    return time_taken


def efficient(x, y):
    if len(x) == 0 and len(y) == 0:
        return 0, "", ""
    if len(x) == 0:
        return len(y) * DELTA, '_' * len(y), y
    if len(y) == 0:
        return len(x) * DELTA, x, '_' * len(x)
    if len(x) == 1 or len(y) == 1:
        return base_case(x, y)

    x_mid = len(x) // 2
    u_score = dp(x[:x_mid], y)
    d_score = dp(x[x_mid:][::-1], y[::-1])
    total_score = [l + r for l, r in zip(u_score, d_score[::-1])]

    y_mid = total_score.index(min(total_score))

    l_u_score, l_u_str1, l_u_str2 = efficient(x[:x_mid], y[:y_mid])
    r_d_score, r_d_str1, r_d_str2 = efficient(x[x_mid:], y[y_mid:])

    return l_u_score + r_d_score, l_u_str1 + r_d_str1, l_u_str2 + r_d_str2


def dp(x, y):
    l1, l2 = len(x), len(y)
    memo = [_ * DELTA for _ in range(l2 + 1)]
    for row in range(1, l1 + 1):
        prev = memo[0]
        memo[0] = row * DELTA
        for col in range(1, l2 + 1):
            current = memo[col]
            memo[col] = min(memo[col] + DELTA,
                        memo[col - 1] + DELTA,
                        prev + ALPHA[x[row - 1] + "_" + y[col - 1]])
            prev = current
    return memo


def base_case(x, y):
    if len(x) == 1:
        score = DELTA * (len(y) - 1)
        if x in y:
            idx = y.index(x)
            return score, ("_" * idx) + x + "_" * (len(y) - idx - 1), y
        else:
            idx = 0
            if x == "A":
                if "G" in y:
                    score += ALPHA[x + "_G"]
                    idx = y.index("G")
                elif "T" in y:
                    score += ALPHA[x + "_T"]
                    idx = y.index("T")
                else:
                    score += ALPHA[x + "_C"]
                    idx = y.index("C")
            elif x == "C":
                if "T" in y:
                    score += ALPHA[x + "_T"]
                    idx = y.index("T")
                elif "A" in y:
                    score += ALPHA[x + "_A"]
                    idx = y.index("A")
                else:
                    score += ALPHA[x + "_G"]
                    idx = y.index("G")
            elif x == "G":
                if "A" in y:
                    score += ALPHA[x + "_A"]
                    idx = y.index("A")
                elif "T" in y:
                    score += ALPHA[x + "_T"]
                    idx = y.index("T")
                else:
                    score += ALPHA[x + "_C"]
                    idx = y.index("C")
            else:
                if "C" in y:
                    score += ALPHA[x + "_C"]
                    idx = y.index("C")
                elif "A" in y:
                    score += ALPHA[x + "_A"]
                    idx = y.index("A")
                else:
                    score += ALPHA[x + "_G"]
                    idx = y.index("G")
            return score, ("_" * idx) + x + "_" * (len(y) - idx - 1), y
    else:
        score = DELTA * (len(x) - 1)
        if y in x:
            idx = x.index(y)
            return score, x, ("_" * idx) + y + "_" * (len(x) - idx - 1)
        else:
            idx = 0
            if y == "A":
                if "G" in x:
                    score += ALPHA[y + "_G"]
                    idx = x.index("G")
                elif "T" in x:
                    score += ALPHA[y + "_T"]
                    idx = x.index("T")
                else:
                    score += ALPHA[y + "_C"]
                    idx = x.index("C")
            elif y == "C":
                if "T" in x:
                    score += ALPHA[y + "_T"]
                    idx = x.index("T")
                elif "A" in x:
                    score += ALPHA[y + "_A"]
                    idx = x.index("A")
                else:
                    score += ALPHA[y + "_G"]
                    idx = x.index("G")
            elif y == "G":
                if "A" in x:
                    score += ALPHA[y + "_A"]
                    idx = x.index("A")
                elif "T" in x:
                    score += ALPHA[y + "_T"]
                    idx = x.index("T")
                else:
                    score += ALPHA[y + "_C"]
                    idx = x.index("C")
            else:
                if "C" in x:
                    score += ALPHA[y + "_C"]
                    idx = x.index("C")
                elif "A" in x:
                    score += ALPHA[y + "_A"]
                    idx = x.index("A")
                else:
                    score += ALPHA[y + "_G"]
                    idx = x.index("G")
            return score, x, ("_" * idx) + y + "_" * (len(x) - idx - 1)


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
    alignment = []
    time_assuming = time_wrapper()
    memory = process_memory()

    with open(output_file_path, "w+") as f:
        f.writelines(str(alignment[0]) + "\n")
        f.writelines(alignment[1] + "\n")
        f.writelines(alignment[2] + "\n")
        f.writelines(str(time_assuming) + "\n")
        f.writelines(str(memory))
