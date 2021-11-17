import datetime

class tickettype():
    ticketprice = 50
    concert_date = ["31","12","2021"]
    early_date = ["01","11","2021"]
    late_date = ["21","12","2021"]
    time_now = datetime.datetime.now()
    adj_time_now= [time_now.strftime("%d"), time_now.strftime("%m"), time_now.strftime("%Y")]
    advance_purchase_price =   ticketprice * .6
    late_purchase_price = ticketprice * 1.1   
    studentprice = ticketprice * .5

    def __init__(self):
        self.tickettype()

    def tickettype(self):
        valid_choices = ["c", "r", "s"]
        choice = input("Press'R' to purchase a regular ticket,  press 'S' to purchase a student ticket, or press 'C' to check prices. ").lower()
        if choice in valid_choices:
            if choice == 'c':
                self.pricecheck()
            elif choice == 'r':
                self.regularticket()
            else:
                self.studentticket()
        else:
            print("Error: Please choose between (R) for regular or (S) for student.")
            self.tickettype()

    def pricecheck(self):
        if self.adj_time_now < self.early_date:
            print (f"Currently, regular tickets are ${self.advance_purchase_price}.  Whereas Student tickets remain ${self.studentprice}.")
        elif self.adj_time_now > self.late_date:
            print (f"Currently, regular tickets are ${self.late_purchase_price}.  Whereas Student tickets remain ${self.studentprice}.")
        else: 
            print (f"Currently, regular tickets are ${self.ticketprice}.  Whereas Student tickets remain ${self.studentprice}.")
        
        tickettype()

    def regularticket(self):
        if self.adj_time_now < self.early_date:
            print ("Regular: Advanced Purchase")
            print (f"{self.advance_purchase_price}") 
        elif self.adj_time_now > self.late_date:
            print ("Regular: Late Purchase")
            print (f"{self.late_purchase_price}")
        else: 
            print ("Regular Ticket") 
            print (f"{self.ticketprice}")
       
        numbersystem()

    def studentticket(self):
        print ("Student Ticket")
        print (f"{self.studentprice}") 
        
        numbersystem()

class numbersystem():
    number = [] 
    def __init__(self):
        self.ticketnumber()

    def ticketnumber(self):
        newnumb = (len(numbersystem.number) + 1)
        numbersystem.number.append(newnumb)
        print(newnumb)
    
        tickettype()
   
tickettype()


