from kivy.lang import Builder
from kivymd.app import MDApp
from mysql.connector import Error as erreur
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.toast import toast

import configparser
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout




details = {}
mydb = mysql.connector.connect(
    host="localhost", user ="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
)
cursor= mydb.cursor()

cursor.execute("SELECT * FROM Vehicule")
billings_detail = cursor.fetchall()
for x in range(1,len(billings_detail)+1):
    billings_detail[x-1] = (x,)+billings_detail[x-1]
for x in cursor.fetchall():
    x = list(x)
    username, password = x[1], x[2]
    details[username] = password
mydb.commit()
mydb.close()



mydb = mysql.connector.connect(
    host="localhost", user ="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
)
cursor= mydb.cursor()

#['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
#Poppins-SemiBold.ttf





class FirstWindow(Screen):
    user_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    icon = ObjectProperty(None)

    def refuser_useru(self):
        toast("Veillez entrer d'abord en fin de créer un autre compte")

    def lock_word(self):
        #self.icon = "eye" if self.icon == "eye-off" else "eye-off"
        self.ids.password_input.password = False if self.ids.password_input.password is True else True







    def validate_user(self, user_input, password_input):

        mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                       database="apprenants_kalanso2")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM utilisateur ")
        i = mycursor.fetchall()
        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            db = mydb.cursor()
            db.execute("SELECT Utilisateur, Pass FROM utilisateur")
            lst = db.fetchall()

            if self.ids.user_input.text == "" or self.ids.password_input.text == "":
                toast("Vous devez insérer un Id avec un mot de pass")
                self.ids.user_input.text = ""
                self.ids.password_input.text = ""

            elif not str(self.ids.user_input.text) and str(self.ids.password_input) in lst:
                toast("Verifier l'address")

                self.ids.user_input.text= ""
                self.ids.password_input.text=""
            elif (self.ids.user_input.text, self.ids.password_input.text) in lst:

                self.manager.current = "second"
                self.ids.user_input.text = ""
                self.ids.password_input.text = ""
            else:
                toast("Nom d'utilisateur ou mot de pass Incorrect")
                self.ids.user_input.text = ""
                self.ids.password_input.text = ""
                self.ids.user_input.text = ""
                self.ids.password_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.user_input.text = ""
            self.ids.password_input.text = ""

class SecondWindow(Screen):
    id_input = ObjectProperty(None)
    model_input = ObjectProperty(None)
    couleur_input = ObjectProperty(None)
    action_input = ObjectProperty(None)
    fournisseur_input = ObjectProperty(None)
    quantité_input = ObjectProperty(None)
    scroll_input = ObjectProperty(None)
    label_input= ObjectProperty(None)
    recherche_input = ObjectProperty(None)

    def ajouter(self, id_input, model_input, couleur_input, action_input, fournisseur_input, quantité_input):

        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        try:


            if self.ids.id_input.text=='' or self.ids.model_input.text == '' or self.ids.couleur_input.text == '' or self.ids.action_input.text == '' or self.ids.fournisseur_input.text=='' or self.ids.quantité_input.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.id_input.text = ""
                self.ids.model_input.text = ""
                self.ids.couleur_input.text = ""
                self.ids.action_input.text = ""
                self.ids.fournisseur_input.text = ""
                self.ids.quantité_input.text = ""

            elif self.ids.action_input.text != "Disponible":
                toast("veillez ecrire Disponible pour l'action")
            elif  not self.ids.quantité_input.text.isdigit()  or int(self.ids.quantité_input.text) <= 0:
                toast("La quantité doit être un chiffre et ne doit pas être inférieur à 1 ")
            else:

                sql_command= " INSERT INTO Vehicule(Id, Model, Couleur, Action, Fournisseur, Quantité) VALUES(%s, %s, %s, %s, %s, %s)"
                values= (self.ids.id_input.text, self.ids.model_input.text, self.ids.couleur_input.text, self.ids.action_input.text, self.ids.fournisseur_input.text, self.ids.quantité_input.text)
                cursor.execute(sql_command, values)
                toast("Acheter avec Succès!")





                mydb.commit()
                self.ids.id_input.text = ""
                self.ids.model_input.text = ""
                self.ids.couleur_input.text = ""
                self.ids.action_input.text = ""
                self.ids.fournisseur_input.text = ""
                self.ids.quantité_input.text = ""

        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.id_input.text = ""
            self.ids.model_input.text = ""
            self.ids.couleur_input.text = ""
            self.ids.action_input.text = ""
            self.ids.fournisseur_input.text = ""
            self.ids.quantité_input.text= ""
    def otherfunc(self):
        self.manager.current = "third"
    def listdispo(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT Id, Model, Action, Quantité FROM Vehicule WHERE Action='Disponible'")
        req = cursor.fetchall()
        if not req:
            toast("Aucun Véhicule n'est disponible actuellement !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.9),
                pos_hint= {"center_x": .5, "center_y": .5},

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(40)),
                    ("Action", dp(40)),
                    ("Quantité", dp(40)),],
                row_data=[
                    (N[0], N[1], N[2], N[3],) for N in req
                ],
            )
            popup = Popup(title="Voici la liste des véhicule disponible",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()
    def listlouer(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Louer'")

        req = cursor.fetchall()
        if not req:
            toast("Aucun Véhicule n'est louer actuellement !")
        else:

            content = MDDataTable(
                size_hint=(0.9, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle avec Prix", dp(40)),
                    ("Date", dp(40)),
                    ("Action", dp(30)),
                    ("Locateur", dp(40)),
                    ("Quantité", dp(30))],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5],) for N in req
                ],
            )
            popup = Popup(title="Voici la liste des véhicule Loués",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()
    def listavendre(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Mainténance'")
        req = cursor.fetchall()
        if not req:
            toast("Il n'y a aucune voiture en mainténance actuellement")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Destination", dp(40)),
                    ("Action", dp(30)),
                    ("Description", dp(40)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste des véhicule en Mainténance !",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()

    def recherche(self, recherche_input):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Vehicule WHERE Model='{self.ids.recherche_input.text}'")
            i = mycursor.fetchone()

            if self.ids.recherche_input.text =="" :
                toast("Vous devez enter un nom de véhicule!")

            elif not i:
                toast("Cette marque n'existe pas dans la base de données !")
                self.ids.recherche_input.text = ""
            else:
                mydb = mysql.connector.connect(
                    host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
                )
                cursor = mydb.cursor()
                cursor.execute(f"SELECT Id, Model, Action, Quantité FROM Vehicule WHERE Model = '{recherche_input.text}' ")
                req = cursor.fetchall()
                content = MDDataTable(
                    size_hint=(0.9, 1),

                    use_pagination=True,
                    column_data=[

                        ("Id", dp(30)),
                        ("Modèle", dp(30)),
                        ("Action", dp(30)),
                        ("Quantité", dp(30)),
                         ],
                    row_data=[
                        (N[0], N[1], N[2], N[3]) for N in req
                    ],
                )
                popup = Popup(title= f"Voici la liste des véhicules de marque {recherche_input.text} ", content=content, auto_dismiss=True,
                              size=(200, 200), size_hint=(0.9, 0.9))

                # bind the on_press event of the button to the dismiss function
                content.bind(on_press=popup.dismiss)

                # open the popup
                popup.open()
                self.ids.recherche_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.recherche_input.text = ""
    def listannuler(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Vendu'")
        req = cursor.fetchall()
        if not req:
            toast("Aucun véhicule n'est vendu actuellement !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Prix", dp(30)),
                    ("Action", dp(30)),
                    ("Client", dp(40)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste des véhicule Vendu",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()
    def listtout(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Vehicule ")
        data = cursor.fetchall()
        if not data:
            toast("La liste est vide !")
        else:


            cursor.execute("SELECT Id, Model, Action, Quantité FROM Vehicule ")
            req = cursor.fetchall()
            content = MDDataTable(
                size_hint=(0.9, 1),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Action", dp(30)),
                    ("Quantité", dp(30)),
                     ],
                row_data=[
                    (N[0], N[1], N[2], N[3]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les véhicules ", content=content, auto_dismiss=True,
                          size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()

    def modifier(self,id_input, model_input, couleur_input, action_input, fournisseur_input):


        try:
            mydb= mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Vehicule WHERE Id='{self.ids.id_input.text}'")
            i = mycursor.fetchone()

            if self.ids.id_input.text=='' or self.ids.model_input.text == '' or self.ids.couleur_input.text == '' or self.ids.action_input.text == '' or self.ids.fournisseur_input.text=='' or self.ids.quantité_input.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.id_input.text = ""
                self.ids.model_input.text = ""
                self.ids.couleur_input.text = ""
                self.ids.action_input.text = ""
                self.ids.fournisseur_input.text = ""
                self.ids.quantité_input.text = ""
            elif self.ids.action_input.text != "Disponible":
                toast("veillez ecrire Disponible pour l'action")
            elif  not self.ids.quantité_input.text.isdigit()  or int(self.ids.quantité_input.text) <= 0:
                toast("La quantité doit être un chiffre et ne doit pas être inférieur à 1 ")
            elif not i:
                toast("Cet identifiant n'existe pas !")
                self.ids.id_input.text = ""
                self.ids.model_input.text = ""
                self.ids.couleur_input.text = ""
                self.ids.action_input.text = ""
                self.ids.fournisseur_input.text = ""
                self.ids.quantité_input.text = ""


            else:

                mycursor.execute(f"UPDATE Vehicule SET Id = '{self.ids.id_input.text}', Model ='{self.ids.model_input.text}', Couleur = '{self.ids.couleur_input.text}', Action='{self.ids.action_input.text}', Fournisseur= '{self.ids.fournisseur_input.text}', Quantité={self.ids.quantité_input.text}  WHERE Id = {self.ids.id_input.text}")


                mydb.commit()
                toast("Modifier avec succès")

                self.ids.id_input.text = ""
                self.ids.model_input.text = ""
                self.ids.couleur_input.text = ""
                self.ids.action_input.text = ""
                self.ids.fournisseur_input.text = ""
                self.ids.quantité_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.id_input.text = ""
            self.ids.model_input.text = ""
            self.ids.couleur_input.text = ""
            self.ids.action_input.text = ""
            self.ids.fournisseur_input.text = ""
            self.ids.quantité_input.text = ""
class ThirdWindow(Screen):
    id_input1 = ObjectProperty(None)
    model_input1 = ObjectProperty(None)
    prix_input1 = ObjectProperty(None)
    action_input1 = ObjectProperty(None)
    client_input1 = ObjectProperty(None)
    quantité_input1 = ObjectProperty(None)
    liste = ObjectProperty(None)

    def listtout(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT Id, Model, Action, Quantité FROM Vehicule ")
        req = cursor.fetchall()
        if not req:
            toast("La base de donné ne contient actuellement aucun Véhicule !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 1),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Action", dp(30)),
                    ("Quantité", dp(30)),
                     ],
                row_data=[
                    (N[0], N[1], N[2], N[3]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les véhicules ", content=content, auto_dismiss=True,
                          size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()


    def liste_vente_liste(self, liste):
        mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2")
        cursor= mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Vendu'")
        req = cursor.fetchall()
        if not req:
            toast("Aucun Véhicule n'est vendu")
        else:
            content = MDDataTable(
                size_hint=(1.50, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(20)),
                    ("Modèle", dp(30)),
                    ("Prix", dp(40)),
                    ("Action", dp(30)),
                    ("Client", dp(40)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            self.manager.get_screen("third").ids.liste.add_widget(content)
            self.manager.current="third"


    def vente(self,id_input1, model_input1, prix_input1, action_input1, client_input1, quantité_input1):


        try:
            mydb= mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Vehicule WHERE Id='{self.ids.id_input1.text}'")
            i = mycursor.fetchone()
            if self.ids.id_input1.text=='' or self.ids.model_input1.text == '' or self.ids.prix_input1.text == '' or self.ids.action_input1.text == '' or self.ids.client_input1.text=='' or self.ids.quantité_input1.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.id_input1.text = ""
                self.ids.model_input1.text = ""
                self.ids.prix_input1.text = ""
                self.ids.action_input1.text = ""
                self.ids.client_input1.text = ""
                self.ids.quantité_input1.text = ""

            elif not i:
                toast("Cet identifiant n'existe pas !")
                self.ids.id_input1.text = ""
                self.ids.model_input1.text = ""
                self.ids.prix_input1.text = ""
                self.ids.action_input1.text = ""
                self.ids.client_input1.text = ""
                self.ids.quantité_input1.text = ""

            elif self.ids.action_input1.text != "Vendu":
                toast("Vérifier si vous avez bien écrit (Vendu) pour l'action")

            else:

                mycursor.execute(f"UPDATE Vehicule SET Id = '{self.ids.id_input1.text}', Model ='{self.ids.model_input1.text}', Couleur = '{self.ids.prix_input1.text}', Action='{self.ids.action_input1.text}', Fournisseur= '{self.ids.client_input1.text}', Quantité= {self.ids.quantité_input1.text}  WHERE Id = {self.ids.id_input1.text}")


                mydb.commit()
                toast("Vendu avec succès")

                self.ids.id_input1.text = ""
                self.ids.model_input1.text = ""
                self.ids.prix_input1.text = ""
                self.ids.action_input1.text = ""
                self.ids.client_input1.text = ""
                self.ids.quantité_input1.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.id_input1.text = ""
            self.ids.model_input1.text = ""
            self.ids.prix_input1.text = ""
            self.ids.action_input1.text = ""
            self.ids.client_input1.text = ""
            self.ids.quantité_input1.text = ""
    def vente_liste(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Vendu'")
        req = cursor.fetchall()
        if not req:
            toast("Auncun véhicule n'est vendu !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.6),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Prix", dp(30)),
                    ("Action", dp(30)),
                    ("Client", dp(30)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste des véhicule Vendues !",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))
            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)
            # open the popup
            popup.open()
    def otherfunc(self):
        self.manager.current = "third"
    def otherother(self):
        self.manager.current = "second"
class FourWindow(Screen):
    id_input2 = ObjectProperty(None)
    model_input2 = ObjectProperty(None)
    datelocation_input2 = ObjectProperty(None)
    action_input2 = ObjectProperty(None)
    locateur_input2 = ObjectProperty(None)
    quantité_input2 = ObjectProperty(None)
    def listtout(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT Id, Model, Action, Quantité FROM Vehicule ")
        req = cursor.fetchall()
        if not req:
            toast("La base de donnée ne contient aucun véhicule actuellement")
        else:
            content = MDDataTable(
                size_hint=(0.9, 1),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Action", dp(30)),
                    ("Quantité", dp(30)),
                     ],
                row_data=[
                    (N[0], N[1], N[2], N[3]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les véhicules ", content=content, auto_dismiss=True,
                          size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()

    def louer(self, id_input2, model_input2, datelocation_input2, action_input2, locateur_input2, quantité_input2):

        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Vehicule WHERE Id='{self.ids.id_input2.text}'")
            i = mycursor.fetchone()

            if self.ids.id_input2.text=='' or self.ids.model_input2.text == '' or self.ids.datelocation_input2.text == '' or self.ids.action_input2.text == '' or self.ids.locateur_input2.text=='' or self.ids.quantité_input2.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.id_input2.text = ""
                self.ids.model_input2.text = ""
                self.ids.datelocation_input2.text = ""
                self.ids.action_input2.text = ""
                self.ids.locateur_input2.text = ""
                self.ids.quantité_input2.text = ""

            elif not i:
                toast("Cet identifiant n'existe pas !")
                self.ids.id_input2.text = ""
                self.ids.model_input2.text = ""
                self.ids.datelocation_input2.text = ""
                self.ids.action_input2.text = ""
                self.ids.locateur_input2.text = ""
                self.ids.quantité_input2.text = ""

            elif self.ids.action_input2.text != "Louer":
                toast("Vérifier si vous avez bien écrit Louer pour l'action")

            else:

                mycursor.execute(
                    f"UPDATE Vehicule SET Id = '{self.ids.id_input2.text}', Model ='{self.ids.model_input2.text}', Couleur = '{self.ids.datelocation_input2.text}', Action='{self.ids.action_input2.text}', Fournisseur= '{self.ids.locateur_input2.text}', Quantité= {self.ids.quantité_input2.text}  WHERE Id = {self.ids.id_input2.text}")

                mydb.commit()
                toast("Louer avec succès")

                self.ids.id_input2.text = ""
                self.ids.model_input2.text = ""
                self.ids.datelocation_input2.text = ""
                self.ids.action_input2.text = ""
                self.ids.locateur_input2.text = ""
                self.ids.quantité_input2.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.id_input2.text = ""
            self.ids.model_input2.text = ""
            self.ids.datelocation_input2.text = ""
            self.ids.action_input2.text = ""
            self.ids.locateur_input2.text = ""
            self.ids.quantité_input2.text = ""
    def louer_liste(self, liste1):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Louer'")
        req = cursor.fetchall()
        if not req:
            toast("Auncun véhicule n'est louer actuellement !")
        else:
            content = MDDataTable(
                size_hint=(1.50, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(20)),
                    ("Modèle&Prix", dp(30)),
                    ("Date", dp(40)),
                    ("Action", dp(30)),
                    ("Locateur", dp(40)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            self.manager.get_screen("four").ids.liste1.add_widget(content)
            self.manager.current="four"
class FiveWindow(Screen):
    id_input3 = ObjectProperty(None)
    model_input3 = ObjectProperty(None)
    guarrage_input3 = ObjectProperty(None)
    action_input3 = ObjectProperty(None)
    description_input3 = ObjectProperty(None)
    quantité_input3 = ObjectProperty(None)
    def listtout(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT Id, Model, Action, Quantité FROM Vehicule ")
        req = cursor.fetchall()
        if not req:
            toast("La base de donné ne contient aucun véhicule actuellement !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 1),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Modèle", dp(30)),
                    ("Action", dp(30)),
                    ("Quantité", dp(30)),
                     ],
                row_data=[
                    (N[0], N[1], N[2], N[3]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les véhicules ", content=content, auto_dismiss=True,
                          size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()
    def maintenance(self, id_input3, model_input3, guarrage_input3, action_input3, description_input3, quantité_input3):
        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Vehicule WHERE Id='{self.ids.id_input3.text}'")
            i = mycursor.fetchone()

            if self.ids.id_input3.text=='' or self.ids.model_input3.text == '' or self.ids.guarrage_input3.text == '' or self.ids.action_input3.text == '' or self.ids.description_input3.text=='' or self.ids.quantité_input3.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.id_input3.text = ""
                self.ids.model_input3.text = ""
                self.ids.guarrage_input3.text = ""
                self.ids.action_input3.text = ""
                self.ids.description_input3.text = ""
                self.ids.quantité_input3.text = ""

            elif not i:
                toast("Cet identifiant n'existe pas !")
                self.ids.id_input3.text = ""
                self.ids.model_input3.text = ""
                self.ids.guarrage_input3.text = ""
                self.ids.action_input3.text = ""
                self.ids.description_input3.text = ""
                self.ids.quantité_input3.text = ""

            elif self.ids.action_input3.text != "Mainténance":
                toast("Vérifier si vous avez bien écrit Mainténance pour l'action")

            else:
                mycursor.execute(
                    f"UPDATE Vehicule SET Id = '{self.ids.id_input3.text}', Model ='{self.ids.model_input3.text}', Couleur = '{self.ids.guarrage_input3.text}', Action='{self.ids.action_input3.text}', Fournisseur= '{self.ids.description_input3.text}', Quantité= {self.ids.quantité_input3.text}  WHERE Id = {self.ids.id_input3.text}")

                mydb.commit()
                toast("Mis en Mainténance avec succès")

                self.ids.id_input3.text = ""
                self.ids.model_input3.text = ""
                self.ids.guarrage_input3.text = ""
                self.ids.action_input3.text = ""
                self.ids.description_input3.text = ""
                self.ids.quantité_input3.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.id_input3.text = ""
            self.ids.model_input3.text = ""
            self.ids.guarrage_input3.text = ""
            self.ids.action_input3.text = ""
            self.ids.description_input3.text = ""
            self.ids.quantité_input3.text = ""

    def maintenance_liste(self, liste2):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Vehicule WHERE Action='Mainténance'")
        req = cursor.fetchall()
        if not req:
            toast("Auncun véhicule n'est en mainténance actuellement !")
        else:
            content = MDDataTable(
                size_hint=(1.50, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(10)),
                    ("Modèle", dp(40)),
                    ("Destination", dp(40)),
                    ("Action", dp(30)),
                    ("Description", dp(40)),
                    ("Quantité", dp(30)), ],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5]) for N in req
                ],
            )
            self.manager.get_screen("five").ids.liste2.add_widget(content)
            self.manager.current = "five"
class CreerUsers(Screen):

    logout_btn = ObjectProperty(None)
    logout = ObjectProperty(None)

    def logout_btn(self, logout):
        self.manager.current="first"

    def refuser_useru(self):
        toast("Veillez entrer d'abord en fin de créer un autre compte")
    def create_user(self):

        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        try:
            if self.ids.utilisateur_input.text=='' or self.ids.pass_input.text == '' or self.ids.repeter_input.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.utilisateur_input.text = ""
                self.ids.pass_input.text = ""
                self.ids.repeter_input.text = ""
            elif self.ids.pass_input.text != self.ids.repeter_input.text:
                toast("Les mot de pass sont différent")
                self.ids.utilisateur_input.text = ""
                self.ids.pass_input.text = ""
                self.ids.repeter_input.text = ""
            elif len(self.ids.pass_input.text) < 8 or self.ids.pass_input.text.isdigit():
                toast("Les mot de pass doivent etre au moins 8 carractères à savoir les lettres avec des chiffres")

                self.ids.pass_input.text = ""
                self.ids.repeter_input.text = ""
            else:
                sql_command= " INSERT INTO utilisateur( Utilisateur, Pass) VALUES( %s, %s)"
                values= (self.ids.utilisateur_input.text, self.ids.pass_input.text)
                cursor.execute(sql_command, values)
                toast("Créer avec Succès!")
                mydb.commit()
                self.ids.utilisateur_input.text = ""
                self.ids.pass_input.text = ""
                self.ids.repeter_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.utilisateur_input.text = ""
            self.ids.pass_input.text = ""
            self.ids.repeter_input.text = ""
class PassOublier(Screen):
    def refuser_userp(self):
        toast("Veillez se locker d'abord en fin de créer un autre compte")
    def lock_eye(self):
        #self.icon = "eye" if self.icon == "eye-off" else "eye-off"
        self.ids.password_input1.password = False if self.ids.password_input1.password is True else True
    def forget_password(self):

        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM utilisateur WHERE Utilisateur='{self.ids.utilisateur_input1.text}'")
            i = mycursor.fetchone()
            if not i:
                toast("Cet nom d'utilisateur n'existe pas !")
                self.ids.utilisateur_input1.text = ""
                self.ids.pass_input1.text = ""
                self.ids.repeter_input1.text = ""
            elif self.ids.utilisateur_input1.text=='' or self.ids.pass_input1.text == '' or self.ids.repeter_input1.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.utilisateur_input1.text = ""
                self.ids.pass_input1.text = ""
                self.ids.repeter_input1.text = ""
            elif self.ids.pass_input1.text != self.ids.repeter_input1.text:
                toast("Les mot de pass sont différent")
                self.ids.utilisateur_input1.text = ""
                self.ids.pass_input1.text = ""
                self.ids.repeter_input1.text = ""

            elif len(self.ids.pass_input1.text) < 8 or self.ids.pass_input1.text.isdigit():
                toast("Les mot de pass doivent etre au moins 8 carractères à savoir les lettre avec des chiffre")

                self.ids.pass_input1.text = ""
                self.ids.repeter_input1.text = ""
            else:
                mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                               database="apprenants_kalanso2")
                mycursor = mydb.cursor()
                mycursor.execute(
                    f"UPDATE utilisateur SET Utilisateur = '{self.ids.utilisateur_input1.text}', Pass ='{self.ids.pass_input1.text}' WHERE Utilisateur = '{self.ids.utilisateur_input1.text}'")
                mydb.commit()
                toast("Mot de pass modifié avec Succès!")
                self.manager.current= "first"
                self.ids.utilisateur_input1.text = ""
                self.ids.pass_input1.text = ""
                self.ids.repeter_input1.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.utilisateur_input1.text = ""
            self.ids.pass_input1.text = ""
            self.ids.repeter_input1.text = ""
class CustomerWindow(Screen):
    nom_cos_input = ObjectProperty(None)
    num_cos_input = ObjectProperty(None)
    date_cos_input = ObjectProperty(None)
    email_cos_input = ObjectProperty(None)
    produit_cos_input = ObjectProperty(None)
    quantité_cos_input = ObjectProperty(None)
    def liste_fourni(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Fournisseur")
        req = cursor.fetchall()
        if not req:
            toast("Aucun fournisseur n'est enrégistrer d'abord !")
        else:
            content = MDDataTable(
                size_hint=(1.50, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(10)),
                    ("Nom", dp(40)),
                    ("Téléphone", dp(40)),
                    ("Date", dp(30)),
                    ("Email", dp(40)),
                    ("Produit", dp(40)),
                    ("Quantité", dp(30)), ],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5], N[6]) for N in req
                ],
            )
            self.manager.get_screen("customer").ids.list_customer.add_widget(content)
            self.manager.current = "customer"
    def ajouter(self, nom_cos_input, num_cos_input, date_cos_input, email_cos_input, produit_cos_input, quantité_cos_input):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()
        try:
            if self.ids.nom_cos_input.text=='' or self.ids.num_cos_input.text == '' or self.ids.date_cos_input.text == '' or self.ids.email_cos_input.text == '' or self.ids.produit_cos_input.text=='' or self.ids.quantité_cos_input.text == '':
                toast("Vous devez remplir tous les champs")
                self.ids.nom_cos_input.text = ""
                self.ids.num_cos_input.text = ""
                self.ids.date_cos_input.text = ""
                self.ids.email_cos_input.text = ""
                self.ids.produit_cos_input.text = ""
                self.ids.quantité_cos_input.text = ""

            else:

                sql_command= " INSERT INTO Fournisseur( Nom, Numero, Date, Email, Produit, Quantite) VALUES(%s, %s, %s, %s, %s, %s)"
                values= (self.ids.nom_cos_input.text, self.ids.num_cos_input.text, self.ids.date_cos_input.text, self.ids.email_cos_input.text, self.ids.produit_cos_input.text, self.ids.quantité_cos_input.text)
                cursor.execute(sql_command, values)
                toast("Ajouterer avec Succès!")
                mydb.commit()
                self.ids.nom_cos_input.text = ""
                self.ids.num_cos_input.text = ""
                self.ids.date_cos_input.text = ""
                self.ids.email_cos_input.text = ""
                self.ids.produit_cos_input.text = ""
                self.ids.quantité_cos_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.nom_cos_input.text = ""
            self.ids.num_cos_input.text = ""
            self.ids.date_cos_input.text = ""
            self.ids.email_cos_input.text = ""
            self.ids.produit_cos_input.text = ""
            self.ids.quantité_cos_input.text = ""

    def mod(self, nom_cos_input):
        try:
            mydb = mysql.connector.connect(host="localhost", user="Lancine", passwd="KAMBa@98",
                                           database="apprenants_kalanso2")
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM Fournisseur WHERE Nom='{self.ids.nom_cos_input.text}'")
            i = mycursor.fetchone()

            if self.ids.nom_cos_input.text=='':
                toast("Vous devez entrer le nom du fournisseur ! ")
                self.ids.nom_cos_input.text = ""


            elif not i:
                toast("Cet fournisseur n'existe pas !")
                self.ids.nom_cos_input.text = ""
            else:
                mycursor.execute(
                    f"DELETE FROM Fournisseur WHERE Nom ='{self.ids.nom_cos_input.text}'")

                mydb.commit()
                toast("Supprimer avec succès")

                self.ids.nom_cos_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.ids.nom_cos_input.text = ""
class WindowManager(ScreenManager):
    manager = ObjectProperty(None)
class AutoApp(MDApp):
    nom_cos_input = ObjectProperty(None)
    num_cos_input = ObjectProperty(None)
    date_cos_input = ObjectProperty(None)
    email_cos_input = ObjectProperty(None)
    produit_cos_input = ObjectProperty(None)
    quantite_cos_input = ObjectProperty(None)
    def build(self):
        self.icon = "login.PNG"
        self.title = "GESTION DU PARC AUTO-MOBILE"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file("loglog.kv")
    def liste_useru(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Utilisateur")
        req = cursor.fetchall()
        if not req:
            toast("Il n'y a aucun utilisateur actuellement !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(20)),
                    ("Nom_d'utilisateur", dp(30)),
                    ("Mot de Passe", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2],) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les utilisateurs",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()
    def liste_fournisseur(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Fournisseur")
        req = cursor.fetchall()
        if not req:
            toast("Aucun fournisseur n'est enregistrer actuellement !")
        else:
            content = MDDataTable(
                size_hint=(0.9, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(30)),
                    ("Nom", dp(30)),
                    ("Numéro", dp(30)),
                    ("Date", dp(30)),
                    ("Email", dp(40)),
                    ("Produit", dp(40)),
                    ("Quantité", dp(30)),],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5], N[6]) for N in req
                ],
            )
            popup = Popup(title="Voici la liste de tous les fournisseur",  content=content, auto_dismiss=True, size=(200, 200), size_hint=(0.9, 0.9))

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)

            # open the popup
            popup.open()

    def liste_fourni(self):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM Fournisseur")
        req = cursor.fetchall()
        if not req:
            toast("Aucun fournisseur n'est enregistrer actuellement !")
        else:
            content = MDDataTable(
                size_hint=(1.50, 0.9),

                use_pagination=True,
                column_data=[

                    ("Id", dp(10)),
                    ("Nom", dp(40)),
                    ("Téléphone", dp(40)),
                    ("Date", dp(30)),
                    ("Email", dp(40)),
                    ("Produit", dp(40)),
                    ("Quantité", dp(30)), ],
                row_data=[
                    (N[0], N[1], N[2], N[3], N[4], N[5], N[6]) for N in req
                ],
            )
            self.root.get_screen("customer").ids.list_customer.add_widget(content)
            self.root.current = "customer"

    def ajouter(self, nom_cos_input, num_cos_input, date_cos_input, email_cos_input, produit_cos_input, quantité_cos_input):
        mydb = mysql.connector.connect(
            host="localhost", user="Lancine", passwd="KAMBa@98", database="apprenants_kalanso2"
        )
        mycursor = mydb.cursor()
        try:
            if self.root.ids.nom_cos_input.text=='' or self.root.ids.num_cos_input.text == '' or self.root.ids.date_cos_input.text == '' or self.root.ids.email_input.text == '' or self.root.ids.produit_cos_input.text=='' or self.root.ids.quantité_cos_input.text == '':
                toast("Vous devez remplir tous les champs")
                self.root.ids.nom_cos_input.text = ""
                self.root.ids.num_cos_input.text = ""
                self.root.ids.date_cos_input.text = ""
                self.root.ids.email_cos_input.text = ""
                self.root.ids.produit_cos_input.text = ""
                self.root.ids.quantité_cos_input.text = ""
            else:

                sql_command= " INSERT INTO Fournisseur( Nom, Numero, Date, Email, Produit, Quantite) VALUES(%s, %s, %s, %s, %s, %s)"
                values= (self.root.ids.nom_cos_input.text, self.root.ids.num_cos_input.text, self.root.ids.date_cos_input.text, self.root.ids.email_cos_input.text, self.root.ids.produit_cos_input.text, self.root.ids.quantité_cos_input.text)
                mycursor.execute(sql_command, values)
                toast("Ajouterer avec Succès!")
                mydb.commit()
                self.root.ids.nom_cos_input.text = ""
                self.root.ids.num_cos_input.text = ""
                self.root.ids.date_cos_input.text = ""
                self.root.ids.email_cos_input.text = ""
                self.root.ids.produit_cos_input.text = ""
                self.root.ids.quantité_cos_input.text = ""
        except mysql.connector.Error as err:
            toast(f"{err}")
            self.root.ids.nom_cos_input.text = ""
            self.root.ids.num_cos_input.text = ""
            self.root.ids.date_cos_input.text = ""
            self.root.ids.email_cos_input.text = ""
            self.root.ids.produit_cos_input.text = ""
            self.root.ids.quantité_cos_input.text = ""
    def otherfunc(self, buy):
        self.root.current = "third"
    def otherfunc1(self, buy):
        self.root.current = "four"
    def otherfunc2(self, buy):
        self.root.current = "five"

    def logout_btn(self, logout):
        self.root.current = "first"

    def logout_btn1(self, logout):
        self.root.current = "first"

    def home_btn1(self, home):
        self.root.current = "second"
    def home_btn(self, home):
        self.root.current = "second"
    def home_btn2(self, home):
        self.root.current = "second"

    def refuser_useru(self):
        toast("Veillez entrer d'abord en fin de créer un autre compte")
    def refuser_userp(self):
        toast("Veillez entrer d'abord en fin de créer un autre compte")

    def listvehiculedispo(self):
        pass
AutoApp().run()