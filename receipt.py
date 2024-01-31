# store selected product, save detail of a receipt: name of product, price, subtotal, tax, shippingCost, grandTotal, discount
import os
def storeCustomerInfo(filename, orderID, customerName, customerAddress, customerEmail):
    try:
        file = open(filename,'a+',encoding = 'utf-8')
        file.write("\n{}: {}\n".format("Order ID",orderID))
        file.write("{}: {}\n".format("Delivery address".ljust(10),customerName))
        file.write("{}{}\n".format("".ljust(10+len("Customer Address")),customerAddress))
        file.write("{}: {}\n".format("Email address".ljust(10),customerEmail))
        file.write("-"*100)
        file.write("\n\n")  
    finally:
        file.close()
def storeProduct(filename, productName, productPrice):
    try:
        file = open(filename,'a+',encoding = 'utf-8')
        file.write("{}: $ {}\n".format((productName).ljust(25,' '),productPrice))
    finally:
        file.close()
def saveOrder(filename,subTotal,tax,shippingCost,grandTotal,discount = 0):
    try:
        file = open(filename,'a+',encoding = 'utf-8')
        file.write('\n'+'-'*50+'\n')
        file.write('{}: $ {:.2f}\n'.format('Discount'.ljust(25),discount))
        file.write('{}: $ {:.2f}\n'.format('SubTotal'.ljust(25),subTotal))
        file.write('{}: $ {:.2f}\n'.format('Tax'.ljust(28),tax))
        file.write('{}: $ {:.2f}\n'.format('Shipping cost'.ljust(24),shippingCost))
        file.write('{}: $ {:.2f}\n'.format('GrandTotal'.ljust(24),grandTotal))
    finally:
        file.close()
def printOrder(filename):
    content = "\n"+"*"*50
    try:
        file = open(filename,'r',encoding = 'utf-8')
        content += file.read() +"\n"
        content += "*"*50
    finally:
        file.close()
        print('Thank you for shopping with us')
        return content
def removeOrder(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return 1
    else:
        print("file is not exists")
        return 0
        
