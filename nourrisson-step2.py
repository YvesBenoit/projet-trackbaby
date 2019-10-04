# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv
repertoire="/home/bnp-renault-004/Bureau/ProjetTrackbaby/python-project-trackbaby/"
liste_csv=[]

Month=[]
P5=[]
P25=[]
P50=[]
P75=[]
P95=[]
lignes2_et_suivantes = False
with open(repertoire+'poids-age-fille-0-60-light.csv', 'r' , newline='') as csvfile:
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

lignes2_et_suivantes = False
Poids=[0]
x_mesures=[0]
with open(repertoire+'mesures.csv', 'r' , newline='') as csvfile:
  plot = csv.reader(csvfile, delimiter=';')
  for row in plot:
      if lignes2_et_suivantes :
        Poids.append(float(row[1]))
        x_mesures.append(int(row[0]))
      lignes2_et_suivantes = True


plt.xlabel('Age en mois')
plt.ylabel('Poids en Kg')
plt.xlim(0,60)
plt.ylim(0,22.5)

plt.plot(Month,P5,label='5% poids')
plt.plot(Month,P25,label='25% poids')
plt.plot(Month,P50,label='50% poids')
plt.plot(Month,P75,label='75% poids')
plt.plot(Month,P95,label='95% poids')
plt.scatter(x_mesures,Poids,color='k')
plt.xlim(0,60)
plt.ylim(2,22.5)

plt.title('Afficher par plt.title')
plt.legend()  # provoque l'affichage des label de plt.plot(xxx , xxx ,label = "toto")
plt.grid()
plt.show()

plt.show()


print(Month)






# plt.plot([1, 2, 3, 4])
# 

# Affichage des graphiques à faire



