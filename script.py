jd = input("enter the class name for the JD subkey: ").strip()
skew1 = input("enter the class name for the skew1 subkey: ").strip()
gbg = input("enter the class name for the GBG subkey: ").strip()
data = input("enter the class name for the Data subkey: ").strip()

#The class name values are hexadecimal values.

joined = jd + skew1 + gbg + data

#The joined string contains 32 hexadecimal digits. Every two hexadecimal digits corresponds to 1 binary byte so the joined string is 16 bytes

#Create a list and split the string so each byte becomes a list item
list = []
for i in range(0, len(joined), 2): 
    #print(i)
    #print(joined[i:i+2])
    list.append(joined[i:i+2]) # [start:end] keep in mind that end index is not included, the range is between start index - one index before end. Let's say string = 75292931; string[0:2] would return 75  string[0:3] would return 752  string[1:5] would return 52929

    
#print(list)

# The permutation box tells us how we should rearrange each byte. https://en.wikipedia.org/wiki/Permutation_box https://www.geeksforgeeks.org/computer-networks/what-is-p-box-in-cryptography/
# So let's say list = [1c, 72, d7, c4] and permutationBox = [2, 0, 3, 1]. The rearranged list items would become [d7, 1c, c4, 72] 
 
permutationBox = [8, 5, 4, 2, 11, 9, 13, 3, 0, 6, 1, 12, 14, 10, 15, 7]
keyList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for index, value in enumerate(permutationBox):
    keyList[index] = list[value]
    
hexBootKey = "".join(keyList)

print(f"The boot key: {hexBootKey}")


#This script was created with the help of https://winreg-kb.readthedocs.io/en/latest/sources/system-keys/Local-security-authority.html and https://github.com/mkorman90/regipy/blob/master/regipy/plugins/system/bootkey.py


