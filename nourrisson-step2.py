# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv
repertoire="/home/bnp-renault-004/Bureau/ProjetTrackbaby/python-project-trackbaby/"



# 

# Affichage des graphiques à faire

#---------lecture mesure------------------
lignes2_et_suivantes = False
Poids=[]
Taille=[]
Perimetre=[]
x_mesures=[]
fic_csv = 'mesures.csv'
with open(repertoire+fic_csv, 'r' , newline='') as csvfile:
  plot = csv.reader(csvfile, delimiter=';')
  for row in plot:
      if lignes2_et_suivantes :
        x_mesures.append(int(row[0]))
        Poids.append(float(row[1]))
        Taille.append(float(row[2]))
        Perimetre.append(float(row[3]))
      lignes2_et_suivantes = True



#---------------------------
#--------------1er Graphique
#---------------------------
plt.subplot(131)


#---------lecture poids age fille------------------
Month=[]
P5=[]
P25=[]
P50=[]
P75=[]
P95=[]
fic_csv = 'poids-age-fille-0-60-light.csv'

lignes2_et_suivantes = False
with open(repertoire+fic_csv, 'r' , newline='') as csvfile:
  plot = csv.reader(csvfile, delimiter=';')
  for row in plot:
      if lignes2_et_suivantes :
        Month.append(int(row[0]))
        P5.append(float(row[1]))
        P25.append(float(row[2]))
        P50.append(float(row[3]))
        P75.append(float(row[4]))
        P95.append(float(row[5]))
      lignes2_et_suivantes = True
  


plt.xlabel('Age en mois')
plt.ylabel('Poids en Kg')

plt.plot(Month,P5,label='5% poids')
plt.plot(Month,P25,label='25% poids')
plt.plot(Month,P50,label='50% poids')
plt.plot(Month,P75,label='75% poids')
plt.plot(Month,P95,label='95% poids')
plt.scatter(x_mesures,Poids,color='k')
plt.title('Courbes des Poids')
plt.legend()  # provoque l'affichage des label de plt.plot(xxx , xxx ,label = "toto")
plt.grid()

#---------------------------
#--------------2eme Graphique
#---------------------------


#---------lecture taille age fille------------------
Month=[]
P5=[]
P25=[]
P50=[]
P75=[]
P95=[]
fic_csv = 'taille-age-fille-0-60-light.csv'

lignes2_et_suivantes = False
with open(repertoire+fic_csv, 'r' , newline='') as csvfile:
  plot = csv.reader(csvfile, delimiter=';')
  for row in plot:
      if lignes2_et_suivantes :
        Month.append(int(row[0]))
        P5.append(float(row[1]))
        P25.append(float(row[2]))
        P50.append(float(row[3]))
        P75.append(float(row[4]))
        P95.append(float(row[5]))
      lignes2_et_suivantes = True
plt.subplot(132)


plt.xlabel('Age en mois')
plt.ylabel('Taille en cm')


plt.plot(Month,P5,label='5% taille')
plt.plot(Month,P25,label='25% taille')
plt.plot(Month,P50,label='50% taille')
plt.plot(Month,P75,label='75% taille')
plt.plot(Month,P95,label='95% taille')
plt.scatter(x_mesures,Taille,color='k')
plt.title('Courbes des Tailles')
plt.legend()  # provoque l'affichage des label de plt.plot(xxx , xxx ,label = "toto")
plt.grid()

#---------------------------
#--------------3eme Graphique
#---------------------------

plt.subplot(133)

Month=[]
P5=[]
P25=[]
P50=[]
P75=[]
P95=[]
fic_csv = 'perim-cra-age-fille-0-60-light.csv'

lignes2_et_suivantes = False
with open(repertoire+fic_csv, 'r' , newline='') as csvfile:
  plot = csv.reader(csvfile, delimiter=';')
  for row in plot:
      if lignes2_et_suivantes :
        Month.append(int(row[0]))
        P5.append(float(row[1]))
        P25.append(float(row[2]))
        P50.append(float(row[3]))
        P75.append(float(row[4]))
        P95.append(float(row[5]))
      lignes2_et_suivantes = True

plt.xlabel('Age en mois')
plt.ylabel('Périmetre cranien en cm')


plt.plot(Month,P5,label='5% Périm.cranien')
plt.plot(Month,P25,label='25% Périm.cranien')
plt.plot(Month,P50,label='50% Périm.cranien')
plt.plot(Month,P75,label='75% Périm.cranien')
plt.plot(Month,P95,label='95% Périm.cranien')
plt.scatter(x_mesures,Perimetre,color='k')
plt.title('Courbes des Périmetres craniens')
plt.legend()  # provoque l'affichage des label de plt.plot(xxx , xxx ,label = "toto")
plt.grid()



plt.show()




