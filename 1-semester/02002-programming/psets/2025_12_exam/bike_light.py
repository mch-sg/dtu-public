class BikeLight():
    def __init__(self):
        self.on = False
        self.mode = 'off'

    def long_press(self) -> str:
        if self.on == False:
            self.on = True
            self.mode = 'weak'
            return self.mode
        else:
            self.on = False
            self.mode = 'off'
            return self.mode

    def short_press(self) -> str:
        if self.on == True:
            if self.mode == 'weak':
                self.mode = 'strong'
                return self.mode 
            elif self.mode == 'strong':
                self.mode = 'flash'
                return self.mode 
            elif self.mode == 'flash':
                self.mode = 'weak'
                return self.mode
