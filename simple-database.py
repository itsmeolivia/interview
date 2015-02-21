import sys


var_map = {}
val_map = {}

#data commands
def set(name, value):
    var_map[name] = value
    if value in val_map:
        val_map[value] += 1
    else:
        val_map[value] = 1

def get(name):
    return var_map[name]

def unset(name):
    val_map[var_map[name]] -= 1
    del var_map[name]

def numequalto(value):
    return val_map[value]

#transaction commands

def main():
    for line in sys.stdin:
        print line

if __name__ == "__main__":
    main()
