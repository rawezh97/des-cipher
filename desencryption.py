def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

def encrypt(value,key):

    plain_bin = value #11011001
    k1 = key #10100010
    ip = "26314857"

    # find the mp by replace plain text value with the index of ip
    # mp = 10011110
    mp = []
    for i in ip:
        mp.append(plain_bin[int(i)-1])
    # print("mp : " , mp)

    L0 = mp[:4] # 1001
    R0 = mp[4:] # 1110

    L1 = R0
    #R1 = L0 XOR f(R0 , k1) , R0

    Ep = "41232341" 

    RF0 = []
    for i in Ep:
        RF0.append(R0[int(i)-1])
    # print("RF0 : ",RF0)

    f = [] # the result of R0 XOR k1 = 11011111
    for i in range(0,7):
        if( RF0[i] == k1[i] ):
            f.append("0")
        else:
            f.append("1")
    # print("f(R0 , k1) : " , f)

    S0 = [
        ['1','0','3','2'],
        ['3','2','1','0'],
        ['0','2','1','3'],
        ['3','1','3','2'],
    ]
    S1 = [
        ['0','1','2','3'],
        ['2','0','1','3'],
        ['3','0','1','0'],
        ['2','1','0','3'],
    ]
    # f = 11011111
    # split the f to the half and barawardkrdny ba SO box
    # bo away 4bit binary man dast bkawet w lagal L0 XOR bkaen
    left_part1 = f[:4] # 1101
    column_part1 = left_part1[0] + left_part1[-1] # 11  last one and the fisrt one
    row_part1 = left_part1[1] + left_part1[2]     # 10 the middle one
    col_S0 = int(column_part1 , 2)                # convert binary to number 
    row_S0 = int(row_part1 , 2)                   # convert binary to number 
    lef_data = S0[row_S0][col_S0] # row_S0=2 col_S0=3  result = 3


    reght_part2 = f[4:] # 1111
    column_part2 = reght_part2[0] + reght_part2[-1] # 11  last one and the fisrt one
    row_part2 = reght_part2[1] + reght_part2[2]     # 10 the middle one
    col_S1 = int(column_part2 , 2)                # convert binary to number 
    row_S1 = int(row_part2 , 2)                   # convert binary to number 
    regh_data = S1[row_S1][col_S1] # row_S1=3 col_S1=3  result = 3


    Emurate_f = decimalToBinary(int(lef_data)) + decimalToBinary(int(regh_data)) # 1111
    # print("Emurate_f : " , Emurate_f)


    # R1 = L0 XOR f(R0,k1),R0
    # R1 = 1001 XOR Emurate_f , R0


    # XOR between the L0 and Emurate_f
    result = []
    for i in range(0,4):
        if( L0[i] ==  Emurate_f[i-1]):
            result.append("0")
        else:
            result.append("1")

    # R1 = L0 XOR f(R0,k1),R0
    # R1 = 1001 XOR Emurate_f , R0
    # L0 XOR Emurate_f = result
    # R1 = result XOR R0


    R1 = []
    for i in range(0,4):
        if( result[i] == R0[i] ):
            R1.append("0")
        else:
            R1.append("1")
    # print("R1 : " , R1)
    # print("L1 : " , L1)



    # now we nedd ip reverse 
    # ip = 26314857

    ip_inverse = ['','','','','','','','']
    count = 1
    for i in ip:
        ip_inverse[int(i)-1] =count
        count +=1
    # print("ip_inverse : " , ip_inverse)


    # Concatenate R1+L1
    Concatenate = R1+L1
    # print('Concatenate : ',Concatenate)

    message = ['','','','','','','','']
    s = 0
    for i in ip_inverse:
        message[s] = Concatenate[int(i)-1]
        s += 1
    # print(''.join(message))
    return ''.join(message)

inp = "11011001"
list_key = ["10100010","10001111","00101111","10001110","10000011","10101001","10100001","11100111","10101110","11101011","00101001","01011001","10101010","10100010","11100111","11100110"]

c1 = encrypt(inp , list_key[0])
c2 = encrypt(c1 , list_key[1])
c3 = encrypt(c2 , list_key[2])
c4 = encrypt(c3 , list_key[3])
c5 = encrypt(c4 , list_key[4])
c6 = encrypt(c5 , list_key[5])
c7 = encrypt(c6 , list_key[6])
c8 = encrypt(c7 , list_key[7])
c9 = encrypt(c8 , list_key[8])
c10 = encrypt(c9 , list_key[9])
c11 = encrypt(c10 , list_key[10])
c12 = encrypt(c11 , list_key[11])
c13 = encrypt(c12 , list_key[12])
c14 = encrypt(c13 , list_key[13])
c15 = encrypt(c14 , list_key[14])
c16 = encrypt(c15 , list_key[15])
print("the Enter word is :11011001\nthe Cipher word is :",c16)
