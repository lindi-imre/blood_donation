__author__ = 'Kozma Balazs'


class NameFormat(object):
    @staticmethod
    def name_corr_format(get_name):
        is_list = type(get_name) == list
        if not is_list:
            get_name = get_name.split( )
        for i, one_name in enumerate(get_name):
            if len(one_name) > 1:
                get_name[i] = one_name[0].upper() + one_name[1:].lower()
            else:
                get_name[i] = one_name.upper()
        if not is_list:
            get_name = " ".join(get_name)
        return get_name