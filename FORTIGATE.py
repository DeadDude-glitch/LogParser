from Core import *

class Ticket:
    # initialization
    def __init__(self):
        # End-devices
        self.source = Endpoint()
        self.destination = Endpoint()
        self.session_id = None
        self.protocol = None
        
        # Firewall
        self.log = Log()
        self.device = Device()
        self.action = None
        self.type = None
        self.subtype = None
        
        # Active Directory
        self.user = None
        self.authentication_server = None
        
        # Network 
        self.service = None
        self.NATip = None
        self.NATtype = None
        self.transport = None
        self.application = Application()
        
        # Connection Statistics
        self.duration = None
        self.sent_byte = None
        self.received_byte = None
        self.sent_packet = None
        self.received_packet = None
        
        # stuff to disscus
        self.virtual_domain = None
        self.count_app = None               # count of apps connected or connections to the app?
        # -------------------------------
        self.operating_system = None
        self.sourceHardWareVendor = None    # of what?
        self.sourceSoftWareVersion = None
        # -------------------------------
        self.unauthuser = None              # what are these?
        self.unauthusersource = None
        # -------------------------------
        self.master_source_MAC = None       # belongs to what exactly?
        self.source_MAC = None              # define src
        self.source_server = None           # is the src server?


# format data of one ticket into parameters
def format(values): 
    # format the data in a dictionary
    dictionary = {"NULL" : None}
    # move character by character
    start, end = 0, 1
    inside_quotation = False
    while end <= len(values):
        # handle spaces inside quotation marks
        # using a boolean value as a flag
        if values == '\"': 
            # flip flag
            bracket_counter = not(bracket_counter)
        # when parameter value ends
        elif values[end] == ' ' and not(inside_quotation):
            tmp = values[start:end].split('=')
            dictionary[tmp[0]] = tmp[1]
            start = end
        # move to next character
        end += 1
    return dictionary



if __name__ == "__main__": 
    print(notice.NoneMainModule)
