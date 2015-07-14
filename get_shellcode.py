import os
import sys
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def objdump(file_name, function="main"):
    tmp = id_generator()
    os.system("objdump -d %s > %s" % (file_name, tmp,))
    objcode = ""
    start_at = "<%s>:" % (function, )
    found = False
    dump_file = open(tmp, "rb")
    for line in dump_file:
        line = line.replace("\r", "").replace("\n", "")
        if found and len(line) > 0 and line[-1] != ":":
            objcode += line + '\n'
        if len(line) > 0 and line[-1] == ":":
            if found:
                break
            if line[-len(start_at):] == start_at:
                found = True
                continue
    if os.path.exists(tmp):
        os.remove(tmp)
    return objcode

def from_objcode(objcode):
    shellcode = []
    for line in objcode.split("\n"):
        if len(line) > 1:
            hexcode = []
            line = line.split("\t")[1].split(" ")
            for char in line:
                if len(char) > 1:
                    hexcode.append(char)
            shellcode += hexcode
    return shellcode

def main():
    file_name = sys.argv[1]
    objcode = objdump(file_name)
    shellcode = from_objcode(objcode)
    sys.stdout.write("char shellcode[] = \"")
    for char in shellcode:
        sys.stdout.write("\\x")
        sys.stdout.write(char)
    sys.stdout.write("\";\n")
    print ccode
    return 0

ccode = """
int main(int argc, char **argv)
{
    int (*func)();
    func = (int (*)()) shellcode;
    (int)(*func)();
}
"""

if __name__ == '__main__':
    main()
