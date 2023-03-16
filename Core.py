# this module should used by the log module and independent of it
# it is not the main module

import colorama


# ------------------------
# |       Classes        | 
# ------------------------

class Policy:
    # initialization
    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.uuid = None

class Device:
    # initialization
    def __init__(self):
        self.name = None
        self.id = None

class Application:
    # initialization
    def __init__(self):
        self.id = None
        self.name = None
        self.category = None
        self.risk = None
        self.list = None

class Endpoint:
    # initialization
    def __init__(self):
        self.ip = None
        self.port = None
        self.name = None
        self.interface = None
        self.interface_role = None
        self.country = None
        self.mac = None

class Log:
    # initialization
    def __init__(self):
        self.id = None
        self.date = None
        self.time = None
        self.event_time = None
        self.time_zone = None
        self.level = None


class alert:
    def __init__(self):
        self.color = colorama.Fore.YELLOW
        self.clear = colorama.Style.RESET_ALL
        self.NoneMainModule = self.color + "[NOTICE] this should not run as a main module" + self.clear

notice = alert()





# ----------------------
# |       CLASSES      |
# ----------------------

# some classes here to store parsed log
# probably not needed
# most likely virtual

# ---------------------
# | UTILITY FUNCTIONS |
# ---------------------
 
# read the raw log file into array of raw log data
def read(filepath):
    # read raw tickets from files
    file = open(filepath, 'r')  
    tickets = file.readlines()
    file.close()
    return tickets

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

    

# allow usage as a module
if __name__ == "__main__": 
    print(notice.NoneMainModule)
