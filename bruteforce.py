import itertools
import time
import pyautogui

number = ("0123456789")
others = ("-_.")
capitals = ("ABCDEFGHIJKLMNOPQRSTUVWXyZ")
non_capitals = ("abcdefghijklmnopqrstuvwxyz")
num_caps = ("ABCDEFGHIJKLMNOPQRSTUVWXyZ1234567890")
num_nocaps = ("abcdefghijklmnopqrstuvwxyz1234567890")
num_others = ("1234567890-_.")
caps_nocaps = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXyZ")
caps_num_others = ("ABCDEFGHIJKLMNOPQRSTUVWXyZ1234567890-_.")
nocaps_others = ("abcdefghijklmnopqrstuvwxyz-_.")
num_caps_nocaps = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXyZ1234567890")
num_caps_other = ("ABCDEFGHIJKLMNOPQRSTUVWXyZ1234567890-_.")
num_nocaps_other = ("abcdefghijklmnopqrstuvwxyz1234567890-_.")
caps_nocaps_other = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXyZ-_.")
everything = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXyZ1234567890-_.")

CharLength = 1

while True:
	try:
		a = int(input("Minimum char amount: "))
		b = int(input("Maximum char amount: "))
		break
	except Exception as e:
		print("Please numbers \n")

while True:

	isNum = input("Do you want numbers?(y/n) ")
	isNonCaps = input("Do you want non-capital letters?(y/n) ")
	isCaps = input("Do you want capitals?(y/n) ")
	isOther = input("Do you want others(like - . *) [y/n] ")

	if (isNum == "y" and isNonCaps == "y" and isCaps == "y" and isOther == "y"):
		selection = everything
		break

	elif (isNum == "y" and isNonCaps != "y" and isCaps != "y" and isOther != "y"):
		selection = number
		break

	elif (isNum != "y" and isNonCaps == "y" and isCaps != "y" and isOther != "y"):
		selection = non_capitals
		break

	elif (isNum != "y" and isNonCaps != "y" and isCaps == "y" and isOther != "y"):
		selection = capitals
		break

	elif (isNum != "y" and isNonCaps != "y" and isCaps != "y" and isOther == "y"):
		selection = others
		break

	elif (isNum == "y" and isNonCaps != "y" and isCaps == "y" and isOther != "y"):
		selection = num_caps
		break

	elif (isNum == "y" and isNonCaps == "y" and isCaps != "y" and isOther != "y"):
		selection = num_nocaps
		break

	elif (isNum == "y" and isNonCaps != "y" and isCaps != "y" and isOther == "y"):
		selection = num_others
		break

	elif (isNum != "y" and isNonCaps == "y" and isCaps == "y" and isOther != "y"):
		selection = caps_nocaps
		break

	elif (isNum != "y" and isNonCaps != "y" and isCaps == "y" and isOther == "y"):
		selection = caps_num_others
		break

	elif (isNum != "y" and isNonCaps == "y" and isCaps != "y" and isOther == "y"):
		selection = nocaps_others
		break

	elif (isNum == "y" and isNonCaps == "y" and isCaps == "y" and isOther != "y"):
		selection = num_caps_nocaps
		break

	elif (isNum == "y" and isNonCaps == "y" and isCaps != "y" and isOther == "y"):
		selection = num_nocaps_other
		break

	elif (isNum == "y" and isNonCaps != "y" and isCaps == "y" and isOther == "y"):
		selection = num_caps_other
		break

	elif (isNum != "y" and isNonCaps == "y" and isCaps == "y" and isOther == "y"):
		selection = caps_nocaps_other
		break

	else:
		print("Try Again \n\n")


time.sleep(5)

for Index in range(a,b):

	passwords = (itertools.product(selection, repeat=Index))

	for i in passwords:

		i = str(i)
		i = i.replace("[", "")
		i = i.replace("]", "")
		i = i.replace("'", "")
		i = i.replace(" ", "")   
		i = i.replace(",", "")
		i = i.replace("(", "")
		i = i.replace(")", "")

		pyautogui.typewrite(i)
		pyautogui.keyDown("enter")
		pyautogui.keyUp("enter")



	Index += 1