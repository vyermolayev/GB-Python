from modules import UIModule as UI
from modules import fileModule as FM

FM.loadPhoneDirectory()
UI.showMenu()
FM.storePhoneBook()