#####################################################################################################################
#   Final Project: A program to place order and set appointment for delivery of goods from a grocery store          #
#   Course: CIS 30A - Python                                                                                        #
#   Professor: Kasey Nguyen                                                                                         #
#   Student: Thi Nguyen                                                                                             #
#   Created date: January 28th 2024                                                                                 #
#####################################################################################################################

#-------------------------------------------------Libraries----------------------------------------------------------
import tkinter as tk 	# import GUI library
from tkinter import ttk
from PIL import Image, ImageTk  # library for images has extensions which are png,...
import myclasses as mc  # import module has Product class, Customer class, Order class
from datetime import datetime,timedelta # library for datetime object
from tkcalendar import DateEntry    # library for calendar widgets
import os   # import module use for get path of current source file.
#--------------------------------------------------------------------------------------------------------------------

      
#-------------------------------------------------------Controls-----------------------------------------------------
# main window
main = tk.Tk()
main.title("Target")    
main.geometry("1200x500")
main.configure(background = "#f2f2f2", padx = 2, pady = 2)

#-------------------------------------------------Variables and Functions--------------------------------------------
# initialize variables
customer = mc.Customer()        # initialize a customer object
dt = datetime.now() # datetime in current
productList = [mc.Product("Jumbo blue berries - 9.8oz",5.02,0.2,dt+timedelta(days=2))
               ,mc.Product("Organic banabas - 2lb",1.99)
               ,mc.Product("2% Reduced Fat Milk - 1gal - Good & Gather™",5.02,0.2,+timedelta(days=2)) 
               ,mc.Product("2% Reduced Fat Milk - 1gal - Good & Gather™",2.69)
               ,mc.Product("M&M's Valentine's Cupid's Mix Milk Chocolate Candies",4.49,0.2,dt+timedelta(days=2))
               ,mc.Product("Cashew Nut Clusters - 10oz - Good & Gather™",6.99,0.5,dt+timedelta(days=2))
               ,mc.Product("Wonderful Roasted & Salted Pistachios - 8oz",4.29,0.1,dt+timedelta(days=2))
               ,mc.Product("Plantain Chips Sea Salt - 6oz - Good & Gather™",2.99)
               ,mc.Product("GimMe Organic Roasted Seaweed Snack Sea Salt .35oz",2.19)
               ,mc.Product("King's Hawaiian Original Hawaiian Sweet Rolls - 12oz/12ct",4.99)
               ,mc.Product("Haagen-Dazs Vanilla Swiss Almond Ice Cream - 14",4.39)
               ,mc.Product("Starry Lemon Lime Soda - 12pk/12 fl oz Cans",7.19)
               ,mc.Product("Pepsi Cola Soda - 12pk/12 fl oz Cans",7.19,0.2,dt+timedelta(days=2))
               ,mc.Product("Lunchables Extra Cheesy Pizza - 4.2oz",1.99,0.25,dt+timedelta(days=2))
               ,mc.Product("Live Sansevieria Snake Plant in Repose Rustic Stone Planter",30)
               ,mc.Product("Uncured Ham & Cheddar Cheese Lunch Kit - 3oz - Good & Gather™",1.99)
               ]                # initialize data of products

vProductChoice = tk.StringVar() # variable to get selected item from combobox products
vDeliveryDate = tk.StringVar()  # variable to get selected date from calendar
productListChoice = []          # list of choosen products
vCustomerName = tk.StringVar()  # variable to get value of entry name of customer
vCustomerAddress = tk.StringVar() # variable to get value of entry address of customer
vCustomerEmail = tk.StringVar() # variable to value of entry email of customer
vChoiceList = tk.StringVar()    # variable to link to text of label lChoiceList which display choosen products

# function: handler event when change selected item in combobox products or when press enter keys on combobox
def addProduct():
    choiceProduct = productList[cbbProducts.current()]  # get selected item
    vChoiceList.set(vChoiceList.get() + vProductChoice.get() + " $"+ str(choiceProduct.price) +"\n") # set variable that links to lProductChoice
    productListChoice.append(choiceProduct) # add choosen product from combobox into list choice product to list of choosen products
    lChoiceList.config(text = vChoiceList.get()) # add currently choosen products to display in lable lProductChoice

# function: save to file and display receipt
def saveOrder():
    order = mc.Order(vCustomerName.get(), vCustomerAddress.get(), vCustomerEmail.get(),productListChoice,vDeliveryDate.get())
    lReceipt.insert(0.0,order.displayOrder())
    #lReceipt.config(text = order.displayOrder())
    order.removeOrder()
#--------------------------------------------------------------------------------------------------------------------  

#------------------------------------------------------Controls------------------------------------------------------ 
# configure row and column to layout form
main.grid_columnconfigure(0, weight = 1)    # config column 0
main.grid_columnconfigure(1, weight = 1)    # config column 1
main.grid_rowconfigure(0, weight = 1)       # config row 0
main.grid_rowconfigure(1, weight = 1)       # config row 1

# layout using frame: left frame contains customer infomation, products choice, right frame print out receipt
cFrame = tk.Frame(main, background = "#e6ffe6", highlightbackground= '#002200', highlightthickness=1, highlightcolor="#fff", borderwidth = 2)   # main container
lFrame = tk.Frame(cFrame, background = '#e6ffe6', highlightbackground= '#004d00', highlightthickness=2) # left container
rFrame = tk.Frame(cFrame, background = '#e6ffe6', highlightbackground= '#004d00', highlightthickness=2) # right container

# place and display cFrame into its position
cFrame.grid(row = 1, column = 0, sticky = "nswe")

# configure row and column of cFrame to layout
cFrame.grid_rowconfigure(0, weight = 1)
cFrame.grid_columnconfigure(0, weight = 1)
cFrame.grid_columnconfigure(1, weight = 1)

# place and display lFrame and rFrame into its position
lFrame.grid(row = 0, column = 0, sticky = "nswe")
rFrame.grid(row = 0, column = 1, sticky = "nswe")


# configure row and column of lFrame to layout
lFrame.grid_columnconfigure(0, weight=1)
lFrame.grid_rowconfigure(0, weight=1)
lFrame.grid_rowconfigure(1, weight=5)
lFrame.grid_rowconfigure(2, weight=5)

# create main controls in left frame
titleFont = ("Comic Sans MS", 13, "bold")
fCustomer = tk.Frame(lFrame, background = '#e6ffe6', borderwidth = 1)
fProducts = tk.Frame(lFrame, background = '#e6ffe6', borderwidth = 1)
lOrder = ttk.Label(lFrame, text = "Order",font = titleFont, foreground = "#e6ffe6",background="#003300") # welcome message
lOrder.grid (row = 0, column = 0, sticky = "nsew")
fCustomer.grid(row = 1,column = 0, sticky = "nswe")
fProducts.grid(row = 2,column = 0, sticky = "sw")

# create controls in frame customer info (fCustomer)
subTitleFont = ("Comic Sans MS", 12, "bold")
titleCustomerInfo = ttk.Label(fCustomer, font = subTitleFont, text="Delivery address", background = "#e6ffe6", foreground = "#003300")
lCustomerName = ttk.Label(fCustomer, text = "Your name", background = "#e6ffe6")
eCustomerName = ttk.Entry(fCustomer, textvariable = vCustomerName, width = 80)
lCustomerAddress = ttk.Label(fCustomer,text = "Your address", background = "#e6ffe6")
eCustomerAddress = ttk.Entry(fCustomer,textvariable = vCustomerAddress, width = 80)
lCustomerEmail = ttk.Label(fCustomer,text ="Your email", background = "#e6ffe6")
eCustomerEmail = ttk.Entry(fCustomer,textvariable = vCustomerEmail, width = 80)

# configure column and row of frame customer info (fCustomer)
fCustomer.grid_columnconfigure(0, weight=1)
fCustomer.grid_columnconfigure(1, weight=5)

# place and display controls in fCustomer
titleCustomerInfo.grid(row = 0, column = 0, sticky="nw", padx = 5, pady = 15)
lCustomerName.grid(row = 1, column = 0, padx = 10, pady = 5, sticky="nw")
eCustomerName.grid(row = 1, column = 1, padx = 0, pady = 5, sticky="nw")
lCustomerAddress.grid(row = 2, column = 0, padx = 10, pady = 5, sticky="nw")
eCustomerAddress.grid(row = 2, column = 1, padx = 0, pady = 5, sticky="nw")
lCustomerEmail.grid(row = 3, column = 0, padx = 10, pady = 5, sticky="nw")
eCustomerEmail.grid(row = 3, column = 1, padx = 0, pady = 5, sticky="nw")

# create controls in frame customer info (fProducts)
titleProductInfo = ttk.Label(fProducts, text="Items", font = subTitleFont, background = "#e6ffe6", foreground = "#003300") 
lCalendar = ttk.Label(fProducts, text="Choose delivery date", background = "#e6ffe6", foreground = "#003300")
calendar = DateEntry(fProducts, width=12, background='darkblue',
                    foreground='white', borderwidth=2, textvariable = vDeliveryDate) # calendar to choose a delivery date

# combobox list of products
lProductName = ttk.Label(fProducts,text="Choose a product", background = "#e6ffe6", foreground = "#003300")
cbbProducts = ttk.Combobox(fProducts, width=80, height=50, textvariable = vProductChoice)   # combobox contains products
cbbProducts['values'] = [str(x.productID)+"-"+x.name for x in productList]  # add data for combobox dropdownlist

# load image using for image button
cwd = os.path.dirname(os.path.abspath(__file__))    # get current directory of current source file
buttonImage = ImageTk.PhotoImage(Image.open(cwd+r"\images\button_rect.png").resize((120,50)))
# button to add a new choosen product
btAddProduct = tk.Button(fProducts,text="Add", command = addProduct, image = buttonImage, compound = "center", borderwidth = 0, background = "#e6ffe6")
# label to display list of choosen products
lChoiceList = tk.Label(fProducts, width = 80, text = "", textvariable = vChoiceList, background = "white", highlightthickness=1, highlightcolor="#fff", highlightbackground= '#002200', borderwidth = 2)
# button place order
btPlaceOrder = tk.Button(fProducts,text="Place order",  command = saveOrder, image = buttonImage, compound = "center", borderwidth = 0, height=33, background = "#e6ffe6")

# configure row and column of fProducts to layout
fProducts.grid_rowconfigure(1, weight=1)
fProducts.grid_columnconfigure(0, weight=1)

# place and display controls of fProducts
titleProductInfo.grid(row = 0, column = 0, sticky="nw", padx = 5, pady = 15)
lProductName.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "nw")
cbbProducts.grid(row = 1, column = 1,  padx = 10, pady = 5, sticky = "nw")
btAddProduct.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
lChoiceList.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = "nse")
lCalendar.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "nw")
calendar.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = "nw")
btPlaceOrder.grid(row = 4, column = 0, columnspan = 3,  pady = 5, sticky = "ns")


# configure row and column of rFrame to layout
rFrame.grid_columnconfigure(0, weight=1)
# create controls in right framw
lReceiptTitle = ttk.Label(rFrame,  font = titleFont, text = "Receipt",foreground = "#e6ffe6",background="#003300")
lReceiptTitle.grid(row = 0, column = 0, sticky="nwe")
fReceipt  = tk.Frame(rFrame, background = '#e6ffe6', highlightbackground= '#004d00', highlightthickness=1)
fReceipt.grid(row = 1,column = 0,sticky = "nwe" )
lReceipt = tk.Text(fReceipt,font=("Times New Roman", 11, "normal"),background="#fff")
lReceipt.grid(row = 1, column = 0, padx = 10, pady = 5, sticky="nswe")

scrollbar = ttk.Scrollbar(fReceipt, orient='horizontal', command=lReceipt.xview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)
#  communicate back to the scrollbar
lReceipt['xscrollcommand'] = scrollbar.set

main.mainloop()

