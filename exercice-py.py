#exercice 17  
#1)
#programme 1
L= [] 
for k in range (1,100+1): 
    L+= [k]
print (L)  
#programe 2  
L = [] 
for k in range (1,100):
    L.append(k) 
print(L)
#programme 3 

L = [] 
L = 100*[0] 
for k in range (100): 
    L [k] = k + 1
print (L)  
#2) 
L = [] 
for k in range (1,101): 
    L = L+ [k*2]
print (L) 
#3 
L = [] 
for k in range (1,101): 
    L = L+ [k*2]
print (L)  

def carre(n): 
    carre = [] 
    for k in range(1,n+1): 
        carre.append(k**2) 
    return carre 
print (carre(5)) 
#exercice 21
def tous_positifs(L):
    for nombre in L:
        if nombre < 0:
            return False  
    return True  
#exercice 22  
#exercice 1)
def positif(L): 
    c = 0
    for nombre in L: 
        if nombre >= 0: 
             c =c+ 1 
    return c 
print(positif([2, -1, 3, 4, -6, 0, 6])) 
#exercice 2) 
def rangs_negatifs(L):
    indices_negatifs = [] 
    for i, nombre in enumerate(L):
        if nombre < 0:  
            indices_negatifs.append(i)  
    return indices_negatifs
print(rangs_negatifs([2,-2,1,1])) 
def notice(L)
     
