# Variabel global
# Digunakan untuk menyimpan hasil proses
PROCESS_SAVER = []

# Catatan:
# EPSILON = \u03B5
# DELTA = \u03B4
# DELTA_TOP = \u0394
# SUBSCRIPT: \u2080 \u2081 \u2082 \u2083 \u2084

# Fungsi transisi
# Didapatkan dari diagram transisi
def delta(state, value):
    if (state == "q\u2080" and value == "0"):
        return "q\u2081"
    elif (state == "q\u2080" and value == "1"):
        return "q\u2082"
    elif (state == "q\u2081" and value == "0"):
        return "q\u2081"
    elif (state == "q\u2081" and value == "1"):
        return "q\u2081"
    elif (state == "q\u2082" and value == "0"):
        return "q\u2083"
    elif (state == "q\u2082" and value == "1"):
        return "q\u2082"
    elif (state == "q\u2083" and value == "0"):
        return "q\u2084"
    elif (state == "q\u2083" and value == "1"):
        return "q\u2083"
    elif (state == "q\u2084" and value == "0"):
        return "q\u2082"
    elif (state == "q\u2084" and value == "1"):
        return "q\u2084"

# Fungs pembantu untuk mendapatkan detail proses
# Dibuat untuk menyimpan string hasil proses..
# .. setelah fungsi delta_top() mencapai akhir
def helper_get_detail_process(str, new):
    if len(str) > 2:
        if "\u03B4(q\u2080, 0)" in str:
            new = str.replace("\u03B4(q\u2080, 0)", "q\u2081")
        elif "\u03B4(q\u2080, 1)" in str:
            new = str.replace("\u03B4(q\u2080, 1)", "q\u2082")
        elif "\u03B4(q\u2081, 0)" in str:
            new = str.replace("\u03B4(q\u2081, 0)", "q\u2081")
        elif "\u03B4(q\u2081, 1)" in str:
            new = str.replace("\u03B4(q\u2081, 1)", "q\u2081")
        elif "\u03B4(q\u2082, 0)" in str:
            new = str.replace("\u03B4(q\u2082, 0)", "q\u2083")
        elif "\u03B4(q\u2082, 1)" in str:
            new = str.replace("\u03B4(q\u2082, 1)", "q\u2082")
        elif "\u03B4(q\u2083, 0)" in str:
            new = str.replace("\u03B4(q\u2083, 0)", "q\u2084")
        elif "\u03B4(q\u2083, 1)" in str:
            new = str.replace("\u03B4(q\u2083, 1)", "q\u2083")
        elif "\u03B4(q\u2084, 0)" in str:
            new = str.replace("\u03B4(q\u2084, 0)", "q\u2082")
        elif "\u03B4(q\u2084, 1)" in str:
            new = str.replace("\u03B4(q\u2084, 1)", "q\u2084")
        PROCESS_SAVER.append(new)
        helper_get_detail_process(new, "")

# Fungsi delta topi
# Merupakan fungsi utama yang memanggil fungsi delta..
# .. dan fungsi pembantu untuk mendapatkan detail proses
def delta_top(state, value, prev):
    if len(value) == 0:
        return "0"
    elif len(value) == 1 and value == "\u03B5":
        PROCESS_SAVER.append(prev)
        new = prev.replace("\u0394(q\u2080, \u03B5)", state)
        PROCESS_SAVER.append(new)
        helper_get_detail_process(new, "")
        return state
    elif len(value) == 1 and value != "\u03B5":
        PROCESS_SAVER.append(prev)
        new = "\u03B4(" + prev.replace(value+")", "\u03B5), " + value+")", 1)
        return delta(delta_top(state, "\u03B5", new), value)
    else:
        PROCESS_SAVER.append(prev)
        new = "\u03B4(" + prev.replace(value+")",
                                       value[:-1]+"), " + value[-1] + ")")
        return delta(delta_top(state, value[:-1], new), value[-1])

# Fungsi untuk mengecek apakah string diterima atau tidak
def get_is_accepted(str):
    isAccepted = delta_top("q\u2080", str, "\u0394(q\u2080, " + str + ")")
    if isAccepted == "q\u2082":
        return True
    else:
        return False

# Fungsi untuk mendapatkan detail dari proses pengecekan
def get_detail_process(str):
    PROCESS_SAVER.clear()
    delta_top("q\u2080", str, "\u0394(q\u2080, " + str + ")")
    return PROCESS_SAVER
