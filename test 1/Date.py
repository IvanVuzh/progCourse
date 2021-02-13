class Date:
    attr_dict = {'day': 'day',
                 'month': 'month',
                 'year': 'year'}

    def __init__(self, string):
        data = string.split("-")
        year = int(string[2])
        month = int(string[1])
        day = int(string[0])

    def date_to_str(self):
        q = str(self.day) + "-" + str(self.month) + "-" + str(self.month)
        return q
