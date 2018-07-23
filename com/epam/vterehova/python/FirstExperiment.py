import sys
import re
import os
import shutil
import commands

def fileOp():
    dir = "."
    listdir = os.listdir(dir)
    for filename in listdir:
        path = os.path.join(dir, filename)
        print os.path.abspath(path)
    print("file exists", os.path.exists("d:/1.txt"))
    print(listdir)

def runCmd():
    print(commands.getstatusoutput("ls  "))

def printStr(str):
    print(str)

def main():
    #fileOp()
    runCmd()

def readFile(filename):
    f = open(filename, "r")
    words = {}
    for line in f:
         #print line
        splits = line.split()
        for split in splits:
            words[split] = 1 if not(words.get(split)) else words.get(split)+1

    print(words)
    print(sorted(words.items(), key=lambda student: student[1], reverse=True))
    #print(words)
    text = f.read()
#    print "text", text

    f.close()


def regular_test(str, find):
    match = re.search(find, str)
    if match:
        return match.group()
    else:
        print "Not found"


def prev_main2():
#    readFile("D:/README.txt")
    print(regular_test("Hello", "el"))

    #find just first appeareance and stop after that
#r - raw
    print(regular_test("fdfdf5", r"..\w+\d"))
    print(re.findall(r"(\w+)", "test test"))
    match = re.search(r"(\w+[\w.]*)@(\w+\.\w+)", "4vasilinka@gmail.com")
#@
    print match.group(1), match.group(2)
#    print(regular_test("fdfdf5", r"..\w+\d"))


def prev_main():
    world_ = "Hello, world!"
    printStr(world_[-4:])
    printStr(world_.lower())
    printStr("Hi %s" % ('Alice'))
    print "sys api: ", dir(sys)
    if len(sys.argv) > 1:
        print "args:", sys.argv[1]
    else:
        print "args less than 1"


    arr=["11","22","33"]+["5","6"]
    print "arr: ", arr

    popped = arr.pop(0)
    del arr[0]
    print "arr functions: ", dir(arr)
    print "popped:", popped
    print "arr:", arr

    sorted(arr, key=len)

    for el in arr:
        print "el: ", el

    for i in range(30):
        print "range", i

    tuple=(1,2,3)
    # tuple and string immutable, list mutable
    print "tuple part: ", tuple[2]

    tupleArr=[(2,"a"),(1,"b"),(3,"d"),(3,"c")]

    #parallel assignment
    (x,y)=(1,2)
    print x, y
    print sorted(tupleArr)

    map = {}
    map["key1"]="value2"
    map["key2"]="value2"
    map["key1"]="value1"

    print "by key receive " + map["key1"], map.get("key1")
    print map.keys(), sorted(map.values())

    print map.items()

    print map

    alertEquals("1", "2")
    alertEquals(1, 1)

def alertEquals(expected, actual):
    if not(expected == actual):
        print "expected ", expected, " but actual ", actual
    else:
        print "Ok"

if __name__ == '__main__':
    main()