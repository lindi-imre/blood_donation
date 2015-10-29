__author__ = 'Kozma Balazs'


class NameFormat(object):
    @staticmethod
    def name_corr_format(get_name):
        if type(get_name) != list:
            if len(get_name) > 1:
                get_name = get_name[0].upper() + get_name[1:].lower()
            else:
                get_name = get_name.upper()
        else:
            for i, one_name in enumerate(get_name):
                if len(one_name) > 1:
                    get_name[i] = one_name[0].upper() + one_name[1:].lower()
                else:
                    get_name[i] = one_name.upper()
        return get_name
