import datetime
import pdb; pdb.set_trace()

class tickettype():
    ticketprice = 50
    def __init__(self):
        pass

    def tickettype(self):
        valid_choices = ["r", "s"]
        choice = input("Press'R' to purchase a regular ticket.  Press 'S' to purchase a student ticket.").lower()
        if choice in valid_choices:
            if choice == 'r':
                tickettype.regularticket()
            else:
                tickettype.studentticket()
        else:
            print("Error: Please choose between (R) for regular or (S) for student.")
            tickettype.tickettype()

    def regularticket(self):
        concert_date = ["31","12","2021"]
        early_date = ["01","11","2021"]
        late_date = ["21","12","2021"]
        time_now = datetime.datetime.now()
        adj_time_now= [time_now.strftime("%d"), time_now.strftime("%m"), time_now.strftime("%Y")]
        advance_purchase_price =   tickettype.ticketprice * .6
        late_purchase_price = tickettype.ticketprice * 1.1    

        if adj_time_now < early_date:
            print (advance_purchase_price)
        elif adj_time_now > late_date:
            print (late_purchase_price)
        else: 
            print (tickettype.ticketprice)
        numbersystem.ticketnumber()

    def studentticket(self):
        studentprice = tickettype.ticketprice * .5
        print (studentprice)
        numbersystem.ticketnumber()


class numbersystem():
    number = [] 

    def __init__(self):
        numbersystem.ticketnumber(self)

    def ticketnumber(self):
        newnumb = (len(numbersystem.number) + 1)
        self.number.append(newnumb)


        print(numbersystem.number)

   
pdb.set_trace()


