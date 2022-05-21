import turtle,pandas,random
from testoasa_judet import Judet
from tkinter import messagebox
from titlu import Titlu

#PARTEA 1
screen = turtle.Screen()
screen.title("Judetele Romaniei")
screen.bgcolor("black")

harta= "harta.gif"
screen.addshape(harta)
turtle.shape(harta)

titlu=Titlu()

#
coor=pandas.read_csv("coordonate.csv")
judete_list=coor["judet"].to_list()
x_list = coor["x"].to_list()
y_list = coor["y"].to_list()


judete_dict={}
for i in range(len(judete_list)):
    denumire_judet_dict=judete_list[i]
    tuplu_coordonate=(x_list[i], y_list[i])

    judete_dict[denumire_judet_dict]=tuplu_coordonate

#>PARTEA 2
#scrie toate judetele
messagebox.showinfo("Avertisment", "Judetele sunt scrise fara diacritice si fara cratima (ex:Bistrita-Nasaud -> Bistrita Nasaud. Literele initiale pot fi scrise cu litera mare sau mica(restul trebuie scrise cu litera mica). "
                                   "Pentru a incheia programul mai devreme introduceti 'gata'")

nr_total_judete=len(judete_list)

lista_obiecte=[]

lista_numere=[] #NOU
for i in range(nr_total_judete):
    lista_numere.append(i+1)

for judet_nume_dict in judete_dict:
    ceva_judet = Judet()
    ceva_judet.nume_judet=judet_nume_dict
    ceva_judet.locatie=judete_dict[judet_nume_dict]

    numar_random=random.choice(lista_numere)
    ceva_judet.numar_judet=numar_random
    lista_numere.remove(numar_random)

    lista_obiecte.append(ceva_judet)
    ceva_judet.write_number()




#Partea3
joc_activ=True
box=messagebox.askquestion("Start","Gata de joc?")
if box=='no':
    joc_activ=False

#jocul nou
nr_ghiciri=0
nr_corecte=0
if joc_activ:
    while nr_ghiciri<nr_total_judete:
        judet_curent=random.choice(lista_obiecte)
        judet_curent.now_color()
        raspuns = screen.textinput(title=f" {nr_ghiciri+1}/{nr_total_judete}", prompt=f"Numele judetului cu numarul {judet_curent.numar_judet} este:")
        if raspuns is None:
            break
        elif raspuns is not None:
            raspuns=raspuns.title()
        if raspuns=="Gata":
            for obiect in lista_obiecte:
                obiect.write_gresit()
            break
        elif raspuns==judet_curent.nume_judet:
            judet_curent.write_judet()
            nr_ghiciri+=1
            nr_corecte+=1
            lista_obiecte.remove(judet_curent)
        else:
            judet_curent.write_gresit()
            nr_ghiciri += 1
            lista_obiecte.remove(judet_curent)
    messagebox.showinfo("Program Incheiat",f"Ai ghicit {nr_corecte} din {nr_total_judete} judete.")
else:
    messagebox.showinfo("Avertisment","Program Incheiat")
    screen.bye()

if joc_activ==True:
    turtle.mainloop()

