from PyQt6 import QtCore, QtGui
import sys
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import (
    QComboBox,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QSpinBox,
    QPushButton,
    QCheckBox,
    QApplication,
    QMainWindow
)
import os
from PyQt6.QtCore import QRect, QProcess


class Ui_MainWindow(object):
    """
    Classe complexe et complète permettant à l'aide PyQt6 de développer une interface utilisateur l'autorisant à rentrer les informatiosn de son véhicule pour procéder
    à une estimation par la base de données scrappé et au modèle choisi.
    """

    def setupUi(self, MainWindow):
        """
        Méthode permettant de créer l'interface graphique
        """
        MainWindow.setObjectName("fenetre")
        MainWindow.resize(550, 550)
        MainWindow.setWindowTitle("Estimation Peugeot")
        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QRect(320, 40, 191, 261))

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QRect(30, 40, 271, 351))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_caracvehic_titre = QLabel(self.centralwidget)
        self.label_caracvehic_titre.setGeometry(QRect(60, 10, 201, 31))
        font_caracvehic_titre = QtGui.QFont()
        font_caracvehic_titre.setPointSize(11)
        font_caracvehic_titre.setBold(False)
        font_caracvehic_titre.setItalic(False)
        self.label_caracvehic_titre.setFont(font_caracvehic_titre)
        self.label_caracvehic_titre.setStyleSheet('font: 11pt "Arial Rounded MT Bold";')
        self.label_caracvehic_titre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_caracvehic_titre.setWordWrap(False)
        self.label_caracvehic_titre.setObjectName("label_caracvehic_titre")

        self.comboBox_modele = QComboBox(self.layoutWidget_2)
        self.comboBox_modele.setEnabled(True)
        self.comboBox_modele.setObjectName("comboBox_modele")
        self.comboBox_modele.addItems(("108","208", "308", "308 SW", "408", "508", "508 SW", "2008", "3008", "4008", "5008", "Boxer", "Expert", "Partner", "Rifter"))
        self.gridLayout.addWidget(self.comboBox_modele, 1, 0, 1, 1)

        self.label_modele = QLabel(self.layoutWidget_2)
        self.label_modele.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_modele.setObjectName("label_modele")
        self.label_modele.setText("Modèle")
        self.gridLayout.addWidget(self.label_modele, 0, 0, 1, 1)


        self.comboBox_silhouette = QComboBox(self.layoutWidget_2)
        self.comboBox_silhouette.setObjectName("comboBox_silhouette")
        self.comboBox_silhouette.addItems(("Berline", "Break", "Citadine", "Coupé-Cabriolet", "Familiale", "SUV-4x4", "Utilitaire"))
        self.gridLayout.addWidget(self.comboBox_silhouette, 1, 1, 1, 1)

        self.label_silhouette = QLabel(self.layoutWidget_2)
        self.label_silhouette.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_silhouette.setObjectName("label_silhouette")
        self.label_silhouette.setText("Silhouette")
        self.gridLayout.addWidget(self.label_silhouette, 0, 1, 1, 1)


        self.comboBox_carburant = QComboBox(self.layoutWidget_2)
        self.comboBox_carburant.setObjectName("comboBox_carburant")
        self.comboBox_carburant.addItems(("Essence", "Diesel", "Hybride", "Electrique", "Hybride rechargeable"))
        self.gridLayout.addWidget(self.comboBox_carburant, 3, 0, 1, 1)

        self.label_carburant = QLabel(self.layoutWidget_2)
        self.label_carburant.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_carburant.setObjectName("label_carburant")
        self.label_carburant.setText("Carburant")
        self.gridLayout.addWidget(self.label_carburant, 2, 0, 1, 1)


        self.comboBox_couleur = QComboBox(self.layoutWidget_2)
        self.comboBox_couleur.setObjectName("comboBox_couleur")
        self.comboBox_couleur.addItems(('Blanc', 'Gris', 'Noir', 'Bleu', 'Rouge', 'Orange', 'Jaune',
       'Vert', 'Sable', 'Brun'))
        self.gridLayout.addWidget(self.comboBox_couleur, 3, 1, 1, 1)

        self.label_couleur = QLabel(self.layoutWidget_2)
        self.label_couleur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_couleur.setObjectName("label_couleur")
        self.label_couleur.setText("Couleur")
        self.gridLayout.addWidget(self.label_couleur, 2, 1, 1, 1)


        self.comboBox_transmission = QComboBox(self.layoutWidget_2)
        self.comboBox_transmission.setObjectName("comboBox_transmission")
        self.comboBox_transmission.addItems(("2 roues motrices", "4 roues motrices"))
        self.gridLayout.addWidget(self.comboBox_transmission, 5, 0, 1, 1)

        self.label_transmission = QLabel(self.layoutWidget_2)
        self.label_transmission.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_transmission.setObjectName("label_transmission")
        self.label_transmission.setText("Transmission")
        self.gridLayout.addWidget(self.label_transmission, 4, 0, 1, 1)


        self.comboBox_bdv = QComboBox(self.layoutWidget_2)
        self.comboBox_bdv.setObjectName("comboBox_bdv")
        self.comboBox_bdv.addItems(("Manuelle", "Automatique"))
        self.gridLayout.addWidget(self.comboBox_bdv, 5, 1, 1, 1)

        self.label_bdv = QLabel(self.layoutWidget_2)
        self.label_bdv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bdv.setObjectName("label_bdv")
        self.label_bdv.setText("Boîte de vitesse")
        self.gridLayout.addWidget(self.label_bdv, 4, 1, 1, 1)


        self.comboBox_annee = QComboBox(self.layoutWidget_2)
        self.comboBox_annee.setObjectName("comboBox_annee")
        self.comboBox_annee.addItems(("2018", "2019", "2020", "2021", "2022"))

        self.gridLayout.addWidget(self.comboBox_annee, 7, 0, 1, 1)
        self.label_annee = QLabel(self.layoutWidget_2)
        self.label_annee.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_annee.setObjectName("label_annee")
        self.label_annee.setText("Année")
        self.gridLayout.addWidget(self.label_annee, 6, 0, 1, 1)


        self.comboBox_utilprec = QComboBox(self.layoutWidget_2)
        self.comboBox_utilprec.setObjectName("comboBox_utilprec")
        self.comboBox_utilprec.addItems(("Particulier", "Entreprise"))
        self.gridLayout.addWidget(self.comboBox_utilprec, 7, 1, 1, 1)

        self.label_utilprec = QLabel(self.layoutWidget_2)
        self.label_utilprec.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_utilprec.setObjectName("label_utilprec")
        self.label_utilprec.setText("Utilisation précédente")
        self.gridLayout.addWidget(self.label_utilprec, 6, 1, 1, 1)


        self.comboBox_places = QComboBox(self.layoutWidget_2)
        self.comboBox_places.setObjectName("comboBox_places")
        self.comboBox_places.addItems(("1", "2", "3", "4", "5", "6", "7"))
        self.gridLayout.addWidget(self.comboBox_places, 9, 0, 1, 1)

        self.label_places = QLabel(self.layoutWidget_2)
        self.label_places.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_places.setObjectName("label_places")
        self.label_places.setText("Nombre de places")
        self.gridLayout.addWidget(self.label_places, 8, 0, 1, 1)


        self.comboBox_portes = QComboBox(self.layoutWidget_2)
        self.comboBox_portes.setObjectName("comboBox_portes")
        self.comboBox_portes.addItems(("3", "5"))
        self.gridLayout.addWidget(self.comboBox_portes, 9, 1, 1, 1)

        self.label_portes = QLabel(self.layoutWidget_2)
        self.label_portes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_portes.setObjectName("label_portes")
        self.label_portes.setText("Nombre de portes")
        self.gridLayout.addWidget(self.label_portes, 8, 1, 1, 1)
        

#################################################################################################

        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_valnum_titre = QLabel(self.centralwidget)
        self.label_valnum_titre.setGeometry(QRect(310, 10, 201, 31))
        font_valnum_titre = QtGui.QFont()
        font_valnum_titre.setPointSize(11)
        font_valnum_titre.setBold(False)
        font_valnum_titre.setItalic(False)
        self.label_valnum_titre.setFont(font_valnum_titre)
        self.label_valnum_titre.setStyleSheet('font: 11pt "Arial Rounded MT Bold";')
        self.label_valnum_titre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_valnum_titre.setWordWrap(False)
        self.label_valnum_titre.setObjectName("label_valnum_titre")


        self.label_prix = QLabel(self.layoutWidget)
        self.label_prix.setTabletTracking(False)
        self.label_prix.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_prix.setObjectName("label_prix")
        self.label_prix.setText("Prix")
        self.verticalLayout_2.addWidget(self.label_prix)

        self.spinBox_prix = QSpinBox(self.layoutWidget)
        self.spinBox_prix.setMaximum(100000)
        self.spinBox_prix.setProperty("value", 30000)
        self.spinBox_prix.setSuffix(' €')
        self.spinBox_prix.setObjectName("spinBox_prix")
        self.verticalLayout_2.addWidget(self.spinBox_prix)


        self.label_cv = QLabel(self.layoutWidget)
        self.label_cv.setTabletTracking(False)
        self.label_cv.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cv.setObjectName("label_cv")
        self.label_cv.setText("Puissance")
        self.verticalLayout_2.addWidget(self.label_cv)

        self.spinBox_cv = QSpinBox(self.layoutWidget)
        self.spinBox_cv.setMaximum(400)
        self.spinBox_cv.setProperty("value", 130)
        self.spinBox_cv.setSuffix(' cv')
        self.spinBox_cv.setObjectName("spinBox_cv")
        self.verticalLayout_2.addWidget(self.spinBox_cv)

        self.label_pf = QLabel(self.layoutWidget)
        self.label_pf.setTabletTracking(False)
        self.label_pf.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_pf.setObjectName("label_pf")
        self.label_pf.setText("Puissance fiscale")
        self.verticalLayout_2.addWidget(self.label_pf)

        self.spinBox_pf = QSpinBox(self.layoutWidget)
        self.spinBox_pf.setMaximum(20)
        self.spinBox_pf.setProperty("value", 6)
        self.spinBox_pf.setSuffix(' cv fiscaux')
        self.spinBox_pf.setObjectName("spinBox_pf")
        self.verticalLayout_2.addWidget(self.spinBox_pf)
        

        self.label_ptac = QLabel(self.layoutWidget)
        self.label_ptac.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ptac.setObjectName("label_ptac")
        self.label_ptac.setText("PTAC")
        self.verticalLayout_2.addWidget(self.label_ptac)

        self.spinBox_ptac = QSpinBox(self.layoutWidget)
        self.spinBox_ptac.setMaximum(3500)
        self.spinBox_ptac.setProperty("value", 1500)
        self.spinBox_ptac.setSuffix(' kg')
        self.spinBox_ptac.setObjectName("spinBox_ptac")
        self.verticalLayout_2.addWidget(self.spinBox_ptac)

        
        self.label_kil = QLabel(self.layoutWidget)
        self.label_kil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_kil.setObjectName("label_kil")
        self.label_kil.setText("Kilométrage")
        self.verticalLayout_2.addWidget(self.label_kil)

        self.spinBox_kil = QSpinBox(self.layoutWidget)
        self.spinBox_kil.setMaximum(250000)
        self.spinBox_kil.setProperty("value", 60000)
        self.spinBox_kil.setSuffix(' km')
        self.spinBox_kil.setObjectName("spinBox_kil")
        self.verticalLayout_2.addWidget(self.spinBox_kil)

        

########################################################################################################

        self.label_garanties_titre = QLabel(self.centralwidget)
        self.label_garanties_titre.setGeometry(QRect(320, 310, 201, 31))
        font_garanties_titre = QtGui.QFont()
        font_garanties_titre.setPointSize(11)
        font_garanties_titre.setBold(False)
        font_garanties_titre.setItalic(False)
        self.label_garanties_titre.setFont(font_garanties_titre)
        self.label_garanties_titre.setStyleSheet('font: 11pt "Arial Rounded MT Bold";')
        self.label_garanties_titre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_garanties_titre.setWordWrap(False)
        self.label_garanties_titre.setObjectName("label_garanties_titre")
        
        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QRect(340, 340, 160, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")

        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.checkBox_kilgar = QCheckBox(self.layoutWidget_3)
        self.checkBox_kilgar.setObjectName("checkBox_kilgar")
        self.checkBox_kilgar.setText("Garantie kilométrique")
        self.verticalLayout.addWidget(self.checkBox_kilgar)

        self.checkBox_gar = QCheckBox(self.layoutWidget_3)
        self.checkBox_gar.setObjectName("checkBox_gar")
        self.checkBox_gar.setText("Garantie")
        self.verticalLayout.addWidget(self.checkBox_gar)

        self.pushButton_valider = QPushButton(self.centralwidget)
        self.pushButton_valider.setGeometry(QRect(130, 420, 301, 31))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_valider.setText("Valider")
        self.pushButton_valider.clicked.connect(self.start_process)

        MainWindow.setCentralWidget(self.centralwidget)

    def start_process(self):
        """
        Méthode permettant de lier l'exécution de l'estimation à tous les paramètres choisis par l'utilisateur à l'actionnement de bouton "Valider".
        """
        self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        path = os.path.dirname(os.path.realpath(__file__))

        modele = int(self.comboBox_modele.currentText())
        silhouette = str(self.comboBox_silhouette.currentText())
        carburant = str(self.comboBox_carburant.currentText())
        couleur = str(self.comboBox_couleur.currentText())
        transmission = str(self.comboBox_transmission.currentText())
        bdv = str(self.comboBox_bdv.currentText())
        annee = int(self.comboBox_annee.currentText())
        util_prec = str(self.comboBox_utilprec.currentText())
        nb_places = int(self.comboBox_places.currentText())
        nb_portes = int(self.comboBox_portes.currentText())
        prix = int(self.spinBox_prix.value())
        ptac = int(self.spinBox_ptac.value())
        kilometrage = int(self.spinBox_kil.value())
        puissance = int(self.spinBox_cv.value())
        puissance_fiscal = int(self.spinBox_pf.value())
        if self.checkBox_gar.isChecked() == True:
            garantie = "oui"
        else:
            garantie = "non"
        
        if self.checkBox_kilgar.isChecked() == True:
            gar_kil = "oui"
        else:
            gar_kil = "non"
        print(modele, silhouette, carburant, couleur,transmission, bdv, annee, util_prec, nb_places, nb_portes, prix, ptac, kilometrage, garantie, gar_kil)
        self.p.execute('py', [f'{path}/dummy_script.py'])
        self.p.exitCode()


interface = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
apply_stylesheet(interface, theme='dark_amber.xml')
MainWindow.show()
sys.exit(interface.exec())
