import math
print('Ohjelma laskee suorakulmion pinta-alan ja piirin.')
print('-------------------------------------------------')
kanta = int (input("Anna kanta: "))
korkeus = int (input("Anna korkeus: "))
print('-----------------------------')

piiri = (kanta + kanta + korkeus + korkeus)
pinta_ala = (kanta * korkeus)


print(' Suorakulmion piiri on:', piiri,'\n','Pinta-ala:', pinta_ala)
print('-----------------------------')