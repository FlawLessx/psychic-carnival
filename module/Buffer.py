class Buffer:
    def load_file(self,path):
        file = open(path, 'r')
        result = file.read()
        return result
    
    def load_buffer(self, path):
        arq = open(path, 'r')
        text = arq.readline()

        buffer = []
        cont = 1

        # The buffer size can be changed by changing cont
        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                # Return a full buffer
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reset the buffer
                buffer = []
        
        arq.close()
