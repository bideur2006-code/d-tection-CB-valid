from math import *
import time
# demande des 15 chiffre de la carte bancaire
# ---------------------------------------
repeat = 0
while repeat == 0:
    CB_number = []
    for HDU_boucle in range (1,16):
        verif = input("entré le chffre n°" + str(HDU_boucle) + " de votre carte bancaire\n")
        try:
            CB_number.append(int(verif))
            repeat = 1
        except:
            print("Erreur : veuillez mettre un chiffre")
            repeat = 0
            break
    print("sortie de boucle")
# -------------------------------------------------
# multiplication de chffre de rang impaire
# --------------------------------------------------
CB_number[0] = CB_number[0]*2
CB_number[2] = CB_number[2]*2
CB_number[4] = CB_number[4]*2
CB_number[6] = CB_number[6]*2
CB_number[8] = CB_number[8]*2
CB_number[10] = CB_number[10]*2
CB_number[12] = CB_number[12]*2
CB_number[14] = CB_number[14]*2
# ----------------------------------------------
#savoir si le résultat de la multiplication est égal ou supérieur a 10
# -------------------------------------------------------------------------
if CB_number[0] >= 10:
    q = CB_number[0] // 10
    r = CB_number[0] % 10
    CB_number[0] = q+r
if CB_number[2] >= 10:
    q = CB_number[2] // 10
    r = CB_number[2] % 10
    CB_number[2] = q+r
if CB_number[4] >= 10:
    q = CB_number[4] // 10
    r = CB_number[4] % 10
    CB_number[4] = q+r
if CB_number[6] >= 10:
    q = CB_number[6] // 10
    r = CB_number[6] % 10
    CB_number[6] = q+r
if CB_number[8] >= 10:
    q = CB_number[8] // 10
    r = CB_number[8] % 10
    CB_number[8] = q+r
if CB_number[10] >= 10:
    q = CB_number[10] // 10
    r = CB_number[10] % 10
    CB_number[10] = q+r
if CB_number[12] >= 10:
    q = CB_number[12] // 10
    r = CB_number[12] % 10
    CB_number[12] = q+r
if CB_number[14] >= 10:
    q = CB_number[14] // 10
    r = CB_number[14] % 10
    CB_number[14] = q+r
# ----------------------------------------------------------
rew15 = CB_number[0] + CB_number[1] + CB_number[2] + CB_number[3] + CB_number[4] + CB_number[5] + CB_number[6] + CB_number[7] + CB_number[8] + CB_number[9] + CB_number[10] + CB_number[11] + CB_number[12] + CB_number[13] + CB_number[14]
result = rew15 % 10
result = 10 - result
#------------------------------------------------------------
# vérification si la carte est valide 
# ---------------------------------------------------------------
chiffre_16 = int(input("quel est votre 16ème chiffre sur votre carte bancaire"))
if result == chiffre_16:
    print("votre carte bancaire est valide ✔")
    time.sleep(10)
    print(result)
else:
    print("votre carte bancaire n'est pas valide ❌")
    time.sleep(10)
    print(result)
# -----------------------------------------------------------------------
