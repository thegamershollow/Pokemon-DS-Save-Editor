import binascii as bin
import numpy as np
from pathlib import Path
savFilePath = '/Users/Cal/Library/CloudStorage/OneDrive-Cash-PetersonConsulting/Documents/Github/Pokemon-DS-Save-Editor/100%.sav'
savFile = open(savFilePath, 'rb')

#* Text Decoder
def decodeText(var):
    decoder = str(var)[2:-1]
    decoder = decoder.replace("\\"," ")
    decoder = decoder.replace('x','')
    decoder = decoder.replace('a1' , '0')
    decoder = decoder.replace('a2' , '1')
    decoder = decoder.replace('a3' , '2')
    decoder = decoder.replace('a4' , '3')
    decoder = decoder.replace('a5' , '4')
    decoder = decoder.replace('a6' , '5')
    decoder = decoder.replace('a7' , '6')
    decoder = decoder.replace('a8' , '7')
    decoder = decoder.replace('a9' , '8')
    decoder = decoder.replace('aa' , '9')
    decoder = decoder.replace('ab' , '!')
    decoder = decoder.replace('ac' , '?')
    decoder = decoder.replace('ad' , '.')
    decoder = decoder.replace('ae' , '-')
    decoder = decoder.replace('b0' , '...')
    decoder = decoder.replace('b1' , '\"')
    decoder = decoder.replace('b2' , '\"')
    decoder = decoder.replace('b3' , "'")
    decoder = decoder.replace('b4' , "'")
    decoder = decoder.replace('b5' , '♂')
    decoder = decoder.replace('b6' , '♀')
    decoder = decoder.replace('b8' , ',')
    decoder = decoder.replace('ba' , '/')
    decoder = decoder.replace('bb' , 'A')
    decoder = decoder.replace('bc' , 'B')
    decoder = decoder.replace('bd' , 'C')
    decoder = decoder.replace('be' , 'D')
    decoder = decoder.replace('bf' , 'E')
    decoder = decoder.replace('c0' , 'F')
    decoder = decoder.replace('c1' , 'G')
    decoder = decoder.replace('c2' , 'H')
    decoder = decoder.replace('c3' , 'I')
    decoder = decoder.replace('c4' , 'J')
    decoder = decoder.replace('c5' , 'K')
    decoder = decoder.replace('c6' , 'L')
    decoder = decoder.replace('c7' , 'M')
    decoder = decoder.replace('c8' , 'N')
    decoder = decoder.replace('c9' , 'O')
    decoder = decoder.replace('ca' , 'P')
    decoder = decoder.replace('cb' , 'Q')
    decoder = decoder.replace('cc' , 'R')
    decoder = decoder.replace('cd' , 'S')
    decoder = decoder.replace('ce' , 'T')
    decoder = decoder.replace('cf' , 'U')
    decoder = decoder.replace('d0' , 'V')
    decoder = decoder.replace('d1' , 'W')
    decoder = decoder.replace('d2' , 'X')
    decoder = decoder.replace('d3' , 'Y')
    decoder = decoder.replace('d4' , 'Z')
    decoder = decoder.replace('d5' , 'a')
    decoder = decoder.replace('d6' , 'b')
    decoder = decoder.replace('d7' , 'c')
    decoder = decoder.replace('d8' , 'd')
    decoder = decoder.replace('d9' , 'e')
    decoder = decoder.replace('da' , 'f')
    decoder = decoder.replace('db' , 'g')
    decoder = decoder.replace('dc' , 'h')
    decoder = decoder.replace('dd' , 'i')
    decoder = decoder.replace('de' , 'j')
    decoder = decoder.replace('df' , 'k')
    decoder = decoder.replace('e0' , 'l')
    decoder = decoder.replace('e1' , 'm')
    decoder = decoder.replace('e2' , 'n')
    decoder = decoder.replace('e3' , 'o')
    decoder = decoder.replace('e4' , 'p')
    decoder = decoder.replace('e5' , 'q')
    decoder = decoder.replace('e6' , 'r')
    decoder = decoder.replace('e7' , 's')
    decoder = decoder.replace('e8' , 't')
    decoder = decoder.replace('e9' , 'u')
    decoder = decoder.replace('ea' , 'v')
    decoder = decoder.replace('eb' , 'w')
    decoder = decoder.replace('ec' , 'x')
    decoder = decoder.replace('ed' , 'y')
    decoder = decoder.replace('ee' , 'z')
    decoder = decoder.replace('ff','')
    decoder = decoder.replace(' ','')
    var = decoder
    return var

#* Gender Decoder
def decodeGender(var):
    decoder = str(var)[2:-1]
    decoder = decoder.replace("\\"," ")
    decoder = decoder.replace('x','')
    decoder = decoder.replace('00','Boy')
    decoder = decoder.replace('01','Girl')
    decoder = decoder.replace(' ','')
    var = decoder
    return var



#* Trainer Data
print('\n'+'-Trainer Info-'+'\n')

# Trainer Name
savFile.seek(0x2000)
trainerName = savFile.read(7)
trainerName = decodeText(trainerName)
print('Name: '+trainerName)


# Trainer Gender
savFile.seek(0x2008)
trainerGender = savFile.read(1)
trainerGender = decodeGender(trainerGender)
print('Gender: '+trainerGender)


# Trainer ID
savFile.seek(0x200B)
trainerID0 = savFile.read(1)
trainerID0 = trainerID0.hex()
savFile.seek(0x200A)
trainerID1 = savFile.read(1)
trainerID1 = trainerID1.hex()
trainerID = int(trainerID0+trainerID1, 16)
trainerID = str(trainerID)
print('Trainer ID: '+trainerID)

# Secret ID
savFile.seek(0x200D)
secretID0 = savFile.read(1)
secretID0 = secretID0.hex()
savFile.seek(0x200C)
secretID1 = savFile.read(1)
secretID1 = secretID1.hex()
secretID = int(secretID0+secretID1, 16)
secretID = str(secretID)
print('Secret ID: '+secretID)

# Time Played
savFile.seek(0x200F)
timePLH1 = savFile.read(1)
timePLH1 = timePLH1.hex()
savFile.seek(0x200E)
timePLH2 = savFile.read(1)
timePLH2 = timePLH2.hex()
timePLH = timePLH1+timePLH2
timePLH = int(timePLH, 16)
timePLH = str(timePLH)
savFile.seek(0x2010)
timePLM = savFile.read(1)
timePLM = timePLM.hex()
timePLM = int(timePLM, 8)
timePLM = str(timePLM)
print('Time Played: '+timePLH+':'+timePLM)


#* Team/Items
print('\n'+'-Team/Items-'+'\n')
# Team PKMN
#*WIP
savFile.seek(0x2038)
teamPKMN = savFile.read(600)
teamPKMN = teamPKMN
teamPKMN = str(teamPKMN)

print(teamPKMN)

#* Security Key
#savFile.seek(0x2AF8)
#secKey = savFile.read(4)
#secKey = bin.hexlify(secKey)
#print(secKey)
'XORed'

# PC Items
#savFile.seek(0x2298)
#pcItm = savFile.read(120)

# Item Pocket
#savFile.seek(0x2310)
#itmPk = savFile.read(168)
#print(itmPk)