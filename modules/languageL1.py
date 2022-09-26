# Variabel global
# Digunakan untuk menyimpan hasil proses
PROCESS_SAVER = []

# Catatan:
# EPSILON = \u03B5
# DELTA = \u03B4
# DELTA_TOP = \u0394

# Fungsi transisi
# Didapatkan dari diagram transisi
def delta(state, value):
    if (state == "q0" and value == "0"):
        return "q3"
    elif (state == "q0" and value == "1"):
        return "q1"
    elif (state == "q1" and value == "0"):
        return "q2"
    elif (state == "q1" and value == "1"):
        return "q1"
    elif (state == "q2" and value == "0"):
        return "q2"
    elif (state == "q2" and value == "1"):
        return "q1"
    elif (state == "q3" and value == "0"):
        return "q3"
    elif (state == "q3" and value == "1"):
        return "q4"
    elif (state == "q4" and value == "0"):
        return "q3"
    elif (state == "q4" and value == "1"):
        return "q4"

# Fungs pembantu untuk mendapatkan detail proses
# Dibuat untuk menyimpan string hasil proses..
# .. setelah fungsi delta_top() mencapai akhir
def helper_get_detail_process(str, new):
    if len(str) > 3:
        if "\u03B4(q0, 0)" in str:
            new = str.replace("\u03B4(q0, 0)", "q3")
        elif "\u03B4(q0, 1)" in str:
            new = str.replace("\u03B4(q0, 1)", "q1")
        elif "\u03B4(q1, 0)" in str:
            new = str.replace("\u03B4(q1, 0)", "q2")
        elif "\u03B4(q1, 1)" in str:
            new = str.replace("\u03B4(q1, 1)", "q1")
        elif "\u03B4(q2, 0)" in str:
            new = str.replace("\u03B4(q2, 0)", "q2")
        elif "\u03B4(q2, 1)" in str:
            new = str.replace("\u03B4(q2, 1)", "q1")
        elif "\u03B4(q3, 0)" in str:
            new = str.replace("\u03B4(q3, 0)", "q3")
        elif "\u03B4(q3, 1)" in str:
            new = str.replace("\u03B4(q3, 1)", "q4")
        elif "\u03B4(q4, 0)" in str:
            new = str.replace("\u03B4(q4, 0)", "q3")
        elif "\u03B4(q4, 1)" in str:
            new = str.replace("\u03B4(q4, 1)", "q4")
        PROCESS_SAVER.append(new + "\n")
        helper_get_detail_process(new, "")

# Fungsi delta topi
# Merupakan fungsi utama yang memanggil fungsi delta..
# .. dan fungsi pembantu untuk mendapatkan detail proses
def delta_top(state, value, prev):
    if len(value) == 0:
        return "0"
    elif len(value) == 1 and value == "\u03B5":
        PROCESS_SAVER.append(prev + "\n")
        new = prev.replace("\u0394(q0, \u03B5)", state)
        PROCESS_SAVER.append(new + "\n")
        helper_get_detail_process(new, "")
        return state
    elif len(value) == 1 and value != "\u03B5":
        PROCESS_SAVER.append(prev + "\n")
        new = "\u03B4(" + prev.replace(value+")", "\u03B5), " + value+")", 1)
        return delta(delta_top(state, "\u03B5", new), value)
    else:
        PROCESS_SAVER.append(prev + "\n")
        new = "\u03B4(" + prev.replace(value+")",
                                       value[:-1]+"), " + value[-1] + ")")
        return delta(delta_top(state, value[:-1], new), value[-1])

# Fungsi untuk mengecek apakah string diterima atau tidak
def get_is_accepted(str):
    isAccepted = delta_top("q0", str, "\u0394(q0, " + str + ")")
    if isAccepted == "q1" or isAccepted == "q3":
        return True
    else:
        return False

# Fungsi untuk mendapatkan detail dari proses pengecekan
def get_detail_process(str):
    PROCESS_SAVER.clear()
    delta_top("q0", str, "\u0394(q0, " + str + ")")
    return PROCESS_SAVER
