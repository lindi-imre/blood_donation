class GenerateButtons:
    @staticmethod
    def generate():
        valid_buttons = []
        i = 48
        while i != 57:
            valid_buttons.append(i)
            i += 1
        i = 65
        while i != 90:
            valid_buttons.append(i)
            i += 1
        i = 97
        while i != 122:
            valid_buttons.append(i)
            i += 1
        valid_buttons.append(139)
        valid_buttons.append(138)
        valid_buttons.append(163)
        valid_buttons.append(233)
        valid_buttons.append(130)
        valid_buttons.append(144)
        valid_buttons.append(160)
        valid_buttons.append(181)
        valid_buttons.append(251)
        valid_buttons.append(235)
        valid_buttons.append(148)
        valid_buttons.append(153)
        valid_buttons.append(129)
        valid_buttons.append(154)
        valid_buttons.append(162)
        valid_buttons.append(224)
        valid_buttons.append(161)
        valid_buttons.append(214)

        return valid_buttons
