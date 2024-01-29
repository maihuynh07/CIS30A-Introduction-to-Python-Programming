import datetime
import receipt

# class include properties of a customer: name, id, emailAddress, address
class Customer:
    amountCustomer = 0
    
    def __init__(self, name="", address="", emailAddress=""):
        self.name = name
        self.address = address
        self.emailAddress = emailAddress
        
        Customer.amountCustomer += 1
        self.customerID = Customer.amountCustomer
    def printCustomer(self):
        print("Customer name:",self.name)
        
    def updateInfo(self, name="", address="", emailAddress=""):
        self.name = name
        self.address = address
        self.emailAddress = emailAddress
        self.customerID = self.amountCustomer
    def getID(self):
        return self.customerID
# properties of a product
class Product:
    amountProduct = 0
    
    def __init__(self,name="",price=0,discount=0,startDayDiscount="",endDayDiscount=""):
        self.name = name
        self.price = price
        self.discount = discount
        self.startDayDiscount = startDayDiscount
        self.endDayDiscount = endDayDiscount
        Product.amountProduct +=1
        self.productID = Product.amountProduct
        print(self.productID)
        
# class Order includes all information belonging to an order: customer, products, tax,...        
class Order(Customer):
    amountOrder = 0
    def __init__(self, name="", address="", emailAddress="", productList={}, deliveryDate=""):
        super().__init__(name,address,emailAddress)
        
        self.orderDate = datetime.datetime.now()
        self.productList = productList
        self.deliveryDate = deliveryDate
        Order.amountOrder +=1
        self.orderID = Order.amountOrder
        receipt.storeCustomerInfo(str(self.orderID) + '.txt',self.orderID,self.name,self.address,self.emailAddress)
        self.addProducts(productList)
          
    def addProducts(self, productList):
        subTotal = 0
        discount = 0
        for item in productList:
            receipt.storeProduct(str(self.orderID) + '.txt', item.name, str(item.price))
            subTotal += item.price - item.price * item.discount
            discount += item.price * item.discount
        tax = 0.0775 * subTotal
        shippingCost = 0.05 * subTotal
        grandTotal = subTotal + shippingCost + tax
        receipt.saveOrder(str(self.orderID) + '.txt',subTotal,tax,shippingCost,grandTotal,discount)
        
    def displayOrder(self):
        content = receipt.printOrder(str(self.orderID) + '.txt')
        print("Thank you for your shopping with us")
        return content
    def removeOrder(self):
        isRemoved = receipt.removeOrder(str(self.orderID) + '.txt')
        if isRemoved == 1: print("Removed",str(self.orderID))
        else: print("File not exists",str(self.orderID))
        
