import hashlib
import binascii
import sys
#===================
global x,y,z,xCnt,zCnt, hashHex, yCnt
x, y, z, xCnt, zCnt, yCnt = 0, 0, 0, 0, 0, 0
#===================
salt = '8ad1712ab5d632d8c4dac07b792ebb17'
pathA = "/root/Game/GamesPwd/GameNO4VRU4S/AgileWordsA.txt"
pathB = "/root/Game/GamesPwd/GameNO4VRU4S/AgileWordsB.txt"
pathC = "/root/Game/GamesPwd/GameNO4VRU4S/AgileWordsC.txt"
pathWhereAmI = "/root/Game/GamesPwd/GameNO4VRU4S/WhereAmI.txt"
pathResults = "/root/Game/GamesPwd/GameNO4VRU4S/results.txt"
hashHex = "b'a3a8b8eb8e739c86f67332d17364b149cd88f33bb11eedae066ac366711ec266'"
#==================+

def EncodePrimary(salt, pwd):
    #salt = binascii.unhexlify(hexstr)
    # print(salt)
    dkey = hashlib.pbkdf2_hmac('sha256', pwd, salt, 100000, dklen=32)
    # print(dkey)
    #print(binascii.hexlify(dkey))
    return str(binascii.b2a_hex(dkey))

def PwdGen(listA, listB, listC, pathWhereAmI):

    n = len(listA)-1
    valueA, valueB, valueC = "","",""
    global x,y,z,xCnt,zCnt,yCnt
    #for i in range(start,finish,operate):

    #====Opens resume=====
    if zCnt == 0:
        text_file = open(pathWhereAmI, "r")
        list1 = text_file.readlines()
        list2 = []
        for item in list1:
            # print(str(item.rstrip('\n')))
            list2.append(str(item.rstrip('\n')))
        #print(list(map(int, list2)))
        x, y, z = list(map(int, list2))
        #print(valueB)
        zCnt = 1
    #===================

    #print(x,end="")
   #print(y,end="")
    #print(z)
    valueA = listA[x]
    x=x+1
    valueC = listC[z]
    valueB = listB[y]
    y=y+1
    if y == n+1:
        y = 1
    if x == n+1:
        x = 0

        xCnt = xCnt+1
    if xCnt == n+1:
        xCnt = 0
        y = 0
        x = 0
    z = z+1
    if z > n:
        z = y
        #print("out of bounds")
        #sys.exit()


    #test for dup. within set
    if str(valueA) == str(valueB):
        return b'no'
    if str(valueC) == str(valueB):
        return b'no'
    if str(valueA) == str(valueC):
        return b'no'

    yCnt = yCnt+1
    if yCnt == 1500:
        yCnt = 0

        with open(pathWhereAmI, 'w') as the_file:
            the_file.write(str(x)+'\n')
            the_file.write(str(y)+'\n')
            the_file.write(str(z))


    #print(valueA)
    #print(valueB)
    #print(valueC)
    hold = (str(valueA +" "+ valueB +" "+ valueC))
    # print(hold)
    #pwd = (bytes(hold), 'ascii')
    pwd = hold
    #print(pwd)
    return pwd

def CheckDk(dk, pwd):
    global hashHex

    if dk == hashHex:
        print("Target found")
        with open(pathResults, 'a') as the_file:
            the_file.write("===============RESULT===================="'\n')
            the_file.write("password set: "+str(x)+" "+str(y)+" "+str(z)+'\n')
            the_file.write("========================================="'\n')
            the_file.write("password: "+str(pwd))

        sys.exit()

#===========LIST IMPORTS===========================
def ListImportAll(pathA, pathB, pathC):
    global zCnt, z
    listA = ListImportA(pathA)
    listB = ListImportB(pathB)
    listC = ListImportC(pathC)

    if len(listA) != len(listB):
        print("bad data--sets not equal")
        sys.exit()
    if len(listC) != len(listB):
        print("bad data--sets not equal")
        sys.exit()

    #z = len(listA)
    #zCnt = len(listA)-1

    return listA, listB, listC

def ListImportA(pathA):
    text_file = open(pathA, "r")
    list1 = text_file.readlines()
    list2 = []
    for item in list1:

        #print(str(item.rstrip('\n')))
        list2.append(str(item.rstrip('\n')))
    return list2

def ListImportB(pathB):
    text_file = open(pathB, "r")
    list1 = text_file.readlines()
    list2 = []
    for item in list1:

        #print(str(item.rstrip('\n')))
        list2.append(str(item.rstrip('\n')))
    return list2

def ListImportC(pathC):
    text_file = open(pathC, "r")
    list1 = text_file.readlines()
    list2 = []
    for item in list1:

        #print(str(item.rstrip('\n')))
        list2.append(str(item.rstrip('\n')))
    return list2
#===================================================

#===================================================
def main():
    SaltHex = binascii.unhexlify(salt)
    #pwd = (bytes("governor washout beak", 'ascii'))
    listA, listB, listC = (ListImportAll(pathA,pathB,pathC))
    a = 0
    while 0==0:

        pwd = PwdGen(listA, listB, listC, pathWhereAmI)
        if pwd != b'no':
            dk = (EncodePrimary(SaltHex, pwd))
            CheckDk(dk, pwd)
            print(dk)




    #print(listA)
    #print(listB)
    #print(listC)




main()

