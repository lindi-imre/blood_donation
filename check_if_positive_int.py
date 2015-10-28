__author__ = 'Kozma Balazs'


class CheckIfPositiveInteger(object):
    @staticmethod
    def check_if_positive_integer(positive_integer):
        if (str(positive_integer).isdigit()) and (int(positive_integer) > 0):
            return True
        else:
            return False
