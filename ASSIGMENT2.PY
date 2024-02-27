def addproduct():
    numofproducts = int(input("Enter the number of products you want to add: "))
    for i in range(numofproducts):
        name = input("Name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        with open("product.txt", "a") as f:
            f.write("Name: " + name + " " + "Price: " + price + " " + "Quantity:" + quantity + "\n")
            f.close()
def updateproduct():
    search = input('Enter name: ')
    with open("product.txt", 'r') as f:
        lines = f.readlines()
    with open("product.txt", "w") as f:
        for line in lines:
            if search in line:
                print(line)
                name = input('Name: ')
                price = input('Price: ')
                quantity = input('Quantity: ')
                f.write("Name: " + name + " " + "Price: " + price + " " + "Quantity:" + quantity + "\n")
            else:
                f.write(line)
def available():
    quantity = []
    with open("product.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            sline=line.strip().split()
            for i in sline:
                if i.startswith('Quantity'):
                    quantity.append(int(i[9:]))
    for i in quantity:
        with open("product.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                sline=line.strip().split()
                for j in sline:
                    if j.startswith('Quantity'):
                        if i == int(j[9:]) and i != 0:
                            print(line)
                            break
def allproducts():
    with open("product.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
def main():
    print("Welcome to the product management system remember DO NOT open the data file it cause feature error.")
    print("Data file is product.txt please do not open it.")
    print("Data file was preloaded with some test data.")
    print("1. Add product")
    print("2. Update product")
    print("3. Available products")
    print("4. All products")
    print("5. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addproduct()
        elif choice == 2:
            updateproduct()
        elif choice == 3:
            available()
        elif choice == 4:
            allproducts()
        else:
            break 
main()
