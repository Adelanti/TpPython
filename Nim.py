#!/usr/bin/python3 

import random
import sys,os 
import math 




#Calcule de score 	
def nscore(nbrcoup):
    scorre = 0
    i = 1
    while i <= nbrcoup:
        scorre += i * pow(10, i)
        i += 1
    return scorre

#Verifier existence d'un score
def score(nom):
    f = open('score.txt', 'r')
    v = f.readline()
    while v :
        y = v.split(';')
        if nom == y[0]:
            f.close()
            return y
        v = f.readline()
    f.close()
    return []


def save_score(nom, meilleur, precd):
    f = open('score.txt', 'a')
    f.write(nom+";"+str(meilleur)+";"+str(precd)+"\n")
    f.close()

 
#Fonction qui vérifie si un tas est vide 
def verifie(liste) :
    for i in range(len(liste)) :
        if (liste[i]==0) :
            return 1
    return 0
        
#Fonctoin qui donne le nombre aléatoire de tas et de pierres par tas 
def begingame():
    x=random.randint(3, 7)
    y=[]
    for i in range(x) :
        y.append(random.randint(5, 23))    
    return y 

#Fonction qui affiche l'état du jeu a chaque role 
def affichage(y):
    print("\n")
    print("*****************"+" "+"L'état du jeu"+" "+"**********************")
    m = max(y)
    i=1 
    for l in y :
        print(str(i)+"| "+"* "*l+"  "*(m-l)+" |"+str(l))
        i=i+1
    print("\n") 
    
joueur1 = input("veuillez entrer le nom du premier joueur : ")   
joueur2 = input("veuillez entrer le nom du deuxième joueur : ")
s1=score(joueur1)
s2=score(joueur2)
if s1 == []:
	s1 = [joueur1,"inf","inf"]
if s2 == []:
	s2 = [joueur1,"inf","inf"]
f = open('score.txt', 'w')
   
liste=begingame()
affichage(liste)
nbrcoup=0;


while(not verifie(liste)) :
    test=1
    print("**********************"+"  "+"c'est le tour de"+" "+str(joueur1)+" "+"***************************")
    while test==1 :
        j1 = input("Donner le numero de tas ainsi que le nombre de pierres a retirer : \n >>")
        l1 = j1.split('-')
        if(0<int(l1[1])<=liste[int(l1[0])-1]):
        	nbrcoup += 1
        	test=0
        else: 
            print("Il n'existe pas autant de pierres dans ce tas")
    liste[int(l1[0])-1]=liste[int(l1[0])-1]-int(l1[1])
    print("\n")
    affichage(liste)
    if (verifie(liste)) :
        print("Le jeu est terminer ")
        test=1
        break
    else :
        test=2
        print("**********************"+"  "+"c'est le tour de"+" "+str(joueur2)+" "+"***************************")
        while test==2 :
            j2 = input("Donner le numero de tas ainsi que le nombre de pierres a retirer : \n >>")
            l2 = j2.split('-')
            if(0<int(l2[1])<=liste[int(l2[0])-1]):
            	nbrcoup+=1
            	test=0
            else : 
                print("Il n'existe pas autant de pierres dans ce tas")
        liste[int(l2[0])-1]=liste[int(l2[0])-1]-int(l2[1])
        affichage(liste)
	      
    
sc=nscore(nbrcoup)  
if test == 2:	
	if int(s1[1])>sc:
		best=sc
	else:
		best=s1[1]
	save_score(joueur1,best,sc)
	save_score(joueur2,s2[1],"inf")
if test == 1:	
	if int(s2[1])>sc:
		best=sc
	else:
		best=s2[1]
	save_score(joueur2,best,sc)
	save_score(joueur1,s1[1],"inf")




		
	
















