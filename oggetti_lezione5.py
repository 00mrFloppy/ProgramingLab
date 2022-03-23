class NumericalCSVFile():

    # Definisco attributo che contenga il nome
    def __init__(self,file_name):
        self.name =file_name

            
    # Definisco il metodo che restituisca il CSV come lista di lista
    def get_data(self):
        lista_dati=[]
        try:    
            my_file=open(self.name, 'r')
            for line in my_file:
                linee_elem=line.split(',')
                linee_elem[-1]=linee_elem[-1].strip()
                if linee_elem[0] != 'Date':
                    lista_dati.append(linee_elem)
            my_file.close
            return lista_dati
            
        except Exception as errore:
            print('Errore: non posso aprire il file')
            print('Questo è l"errore generato: "{}"'.format(errore))        

file=NumericalCSVFile('xxxx.csv')
print(file.get_data())



        