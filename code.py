# Task 1
from collections import Counter
class user(object):
    def __init__(self):
        self.total = 0
        self.items = []
    def addproduct(self, productname, price):
        self.productname = productname
        self.price = price
        self.items.append(self.productname)
        self.total += self.price
    def removeproduct(self, productname):
        self.productname = productname
        self.items.remove(productname)
    def showcart(self):
        c = Counter(self.items)
        print("****************************************************")
        print("Items: ",c)
        print("Total Bill: ", self.total)
        print("****************************************************")
    def total_and_exit(self):
        return self.total
    
if __name__ == "__main__":
    user = user()
    print("Welcome to the cart!")
    print("Hey User, Add products!!!")
    while True:
        print("\nItems in our Store: \nApple => 10 Rupees \nToffee => 5 Rupees \nToy => 15 Rupees")
        print("\nYour Choices: \n1.Add Product \n2.Remove Product \n3.Show Cart \n4.Total and Exit")
        print("****************************************************")
        task = int(input("What are you like to do: "))
        print("****************************************************")
        if task==1:
            print("Adding Product...")
            print("\nProducts: \n1.Apple \n2.Toffee \n3.Toy")
            print("****************************************************")
            addproduct = int(input("Choose: "))
            print("****************************************************")
            if addproduct == 1:
                user.items.append("apple")
                user.total += 10
            elif addproduct == 2:
                user.items.append("toffee")
                user.total += 5
            elif addproduct == 3:
                user.items.append("toy")
                user.total += 15
            else:
                print("Choose the right product")
                break

        elif task==2:
            print("Removing Product...")
            print("\nProducts: \n1.Apple \n2.Toffee \n3.Toy")
            print("****************************************************")
            remproduct = int(input("Choose: "))
            print("****************************************************")
            if remproduct == 1:
                user.items.remove("apple")
                user.total -= 10
            elif remproduct == 2:
                user.items.remove("toffee")
                user.total -= 5
            elif remproduct == 3:
                user.items.remove("toy")
                user.total -= 15
            else:
                print("Choose the right product")
                break
        elif task==3:
            user.showcart()
            # print("Items",user.items)
            # print("Total",user.total)
        elif task == 4:
            print("Total Bill: ",user.total)
            print("Thankyou for Shopping!")
            break

