import sys

var_map = {}
val_map = {}

# data commands


def set_var(name, value):
    var_map[name] = value
    if value in val_map:
        val_map[value] += 1
    else:
        val_map[value] = 1


def get_val(name):
    if name in var_map:
        print var_map[name]
    else:
        print "NULL"


def unset(name):
    val_map[var_map[name]] -= 1
    del var_map[name]


def num_equal_to(value):
    if value in val_map:
        print val_map[value]
    else:
        print "0"
# transaction commands


def main():

    dispatch_table = {
        'GET': get_val,
        'SET': set_var,
        'UNSET': unset,
        'NUMEQUALTO': num_equal_to,
        'END': exit

    }

    while True:
        line = raw_input()
        command = line.split()
        if command[0] in dispatch_table:
            dispatch_table[command[0]](*command[1:])
        else:
            print >> sys.stderr, "Command not found"


if __name__ == "__main__":
    main()
