var_map = {}
val_map = {}
undo = []
rolling_back = False


def in_transaction_block():
    return len(undo) != 0 and not rolling_back


def set_var(name, value):
    if name in var_map:
        if in_transaction_block():
            undo.append((set_var, name, var_map[name]))
        val_map[var_map[name]] -= 1
    elif in_transaction_block():
        undo.append((unset, name))

    if value in val_map:
        val_map[value] += 1
    else:
        val_map[value] = 1
    var_map[name] = value


def get_val(name):
    if name in var_map:
        print var_map[name]
    else:
        print "NULL"


def unset(name):
    if in_transaction_block():
        undo.append((set_var, name, var_map[name]))
    val_map[var_map[name]] -= 1
    del var_map[name]


def num_equal_to(value):
    if value in val_map:
        print val_map[value]
    else:
        print "0"


def commit():
    if not in_transaction_block():
        print "NO TRANSACTION"
        return
    global undo
    undo = []


def rollback():
    if not in_transaction_block():
        print "NO TRANSACTION"
        return
    global rolling_back
    rolling_back = True
    rolling = None
    while rolling != "begin":
        rolling = undo.pop()
        if rolling != "begin":
            rolling[0](*rolling[1:])
    rolling_back = False


def begin():
    undo.append("begin")


def main():

    dispatch_table = {
        "GET": get_val,
        "SET": set_var,
        "UNSET": unset,
        "NUMEQUALTO": num_equal_to,
        "END": exit,
        "BEGIN": begin,
        "COMMIT": commit,
        "ROLLBACK": rollback,
    }

    while True:
        try:
            line = raw_input()
        except EOFError:
            exit()
        command = line.split()
        dispatch_table[command[0]](*command[1:])


if __name__ == "__main__":
    main()
