class UtilDict(dict):

    def foreach(self, function):
        for k, v in self.items():
            function(k, v)
