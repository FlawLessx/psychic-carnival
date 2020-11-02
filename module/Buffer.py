class Buffer:
    def load_file(self,path):
        file = open(path, 'r')
        result = file.read()
        return result
