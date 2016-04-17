#!/usr/local/bin/python3

database = {
	'home': 'ngoi nha',
	'baby': 'em be',
	'school': 'truong hoc'
}

def show_menu():
	print("---------------------------")
	print("-TU DIEN viet bang Python3-")
	print("---------------------------")
	print("1. Them tu")
	print("2. Tim tu")
	print("3. Xoa tu")
	print("4. Xem tat ca")
	print("An 0 de thoat chuong trinh")
	print("---------------------------")

def add():
	word = input("Tu moi: ")
	mean = input("Nghia la: ")
	database[word] = mean
	print("+ Tu moi da duoc them.")

def find():
	word = input("+ Tim tu gi: ")
	if word in database:
		print("Tim thay: [ %s : %s ]" % (word, database[word]))
	else:
		print("Khong tim thay tu [ %s ]" % word)

def remove():
	word = input("+ Xoa tu gi: ")
	if word in database:
		del database[word]
		print("Tu [ %s ] da bi xoa" % word)
	else:
		print("Khong tim thay tu [ %s ]" % word)

def view_all():
	print("+ Xem tat ca: ")
	for word, mean in database.items():
		print("[ %s: %s ]" % (word, mean))

# Hien menu
show_menu()

# Chuong trinh chinh
choice = int(input("Lua chon: "))

while choice != 0:
	if choice == 0:
		break
	elif choice == 1:
		add()
	elif choice == 2:
		find()
	elif choice == 3:
		remove()
	elif choice == 4:
		view_all()
	else:
		print("Khong co lua chon nay!")

	choice = int(input("Lua chon: "))

print("Hen gap lai!")