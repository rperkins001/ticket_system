from time import sleep



class Create_Event():
    
    def __init__(self):
        eventtitle = self.specify('event title', 80)   
        self.eventvenue = self.specify('event venue', 45)
        self.eventaddress = self.specify('event street address', 80)
        self.eventzip = self.numberlength('zip code of the event', "exactly", 5, range(5, 6))
        self.ticketquant = self.numberlength('total number of tickets to be sold', "at most", 5, range(1, 6))
        self.eventyear = self.numberlength('year of the event', "exactly", 4, range(4, 5))
        self.eventmonth = self.numberlength('month of the event', "at most", 2, range(1, 3))
        self.eventday = self.numberlength('day of the event', "at most", 2, range(1, 3))
        self.eventhour = self.numberlength('hour of the event', "at most", 2, range(1, 3))
        self.eventminute = self.numberlength('minute of the event', "at most", 2, range(1, 3))
        self.meridian = self.ampm()
        self.timezone = self.zone()
        self.eventrecall()

    def specify(self, spec, limit): 
        inp = input(f"Specify {spec}: ")
        if len(inp) > limit:
            print(f"Error: Event Title cannot exceed {limit} characters.")
            self.specify()
        else:
            pass
    
    def numberlength(self, category, quantqual, numlenexp, numlenrange):
        while True:
            try:
                self.var = int(input(f"Indicate the {category}: "))
                break
            except ValueError:
                print(f"Error: {category} must be a number and {quantqual} {numlenexp} characters.")

        num = self.var    
        a_string = str(num)
        length = len(a_string)

        if length not in numlenrange:
            print(f"Error: {category} must be a number and {quantqual} {numlenexp} characters.")  
            self.numberlength(category, quantqual, numlenexp, numlenrange)
            
        else:
            pass

    def ampm(self):
        valid_mer = ["am", "pm"]
        self.meridian = input ("Indicate the meridian AM or PM: ").lower()
        if self.meridian in valid_mer:
            pass
        else:
            raise ("Error: Please input AM or PM.")
            self.ampm()

    def zone(self):
        zone_values = ["e", "c", "c", "p"]
        self.timezone = input(
            """ please indicate timezone?: 
                Select which applies:
                    (E) for Eastern time zone.
                    (C) for Central time zone.
                    (M) for Mountain time zone.
                    (P) for Pacific time zone:  """).lower()
        if self.timezone in zone_values:
            pass
        else: 
            raise ("Error: Please indicate E, C, M, or P according to your relevent timezone region.")
            self.zone()

    def eventrecall(self):
        print(f"""
                Event set:
                      Event Title:    {__init__.eventtitle}
                            Venue:    {self.eventvenue}
                          Address:    {self.eventaddress}
                              Zip:    {self.eventzip}
                Tickets Available:    {self.ticketquant}
                       Event Date:    {self.eventmonth}.zfill(2), {self.eventday}.zfill(2), {self.eventyear}
                       Event Time:    {self.eventhour}.zfill(2):{self.eventminute}zfill(2) {self.meridian}
                        Time Zone:    {self.timezone} """)



class Ticket_Type():
    tickettypes = []
    rate = []
    def __init__(self):
        self.type_choice()
        pass

    def type_choice(self):
        self.valid_inputs = ["r", "a", "l", "sc", "st", "c", "d"]
        self.ticktype = input(
            """ Select ticket categories by the letter representing the selection.
                Select all that apply:
                    (R)  for Regular Adult Ticket.
                    (A)  for Regular - Advanced Purchase 
                    (L)  for Regular - Late Purchase
                    (SC) for Senior Citizen 
                    (ST) for Student
                    (C)  for Children 
                    Type (D)  for Done when finished.     """).lower()
        
        if self.ticktype in self.valid_inputs[0:6]:
            self.tickettypes.append(self.ticktype)
            print(self.tickettypes)
            type = input(f"What percentage of the regular price is the price of tickets in category {self.ticktype}? ")
            self.rate.append(type) 
            print(self.rate)
            self.type_choice()

        elif self.ticktype not in self.valid_inputs:
            raise ("Error: Please select a valid tickettype.")
            self.type_choice()
        else:
            print("Ticket types set.")
            pass
            sleep (2)
        
        
 
        




Create_Event()
sleep(10)
Ticket_Type()       

class See_Event():

    pass

class Cancel_Event():
    pass

