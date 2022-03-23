class CSVFile():

    # Definisco attributo che contenga il nome
    def __init__(self,file_name):
        if type(file_name) is not str:
            raise Exception ('Errore:il nome file non è una stringa')
        self.name = file_name


    # Definisco il metodo che restituisca il CSV come lista di lista
    def get_data(self, start=None, end=None):
        lista_dati=[]
        my_file=open(self.name, 'r')
        for i,line in enumerate(my_file):
            linee_elem=line.split(',')
            linee_elem[-1]=linee_elem[-1].strip()
            if i+1 >= start and i+1 <= end:
                if linee_elem[0] != 'Date':
                        lista_dati.append(linee_elem)
        my_file.close
        return lista_dati


file=CSVFile('shampoo_sales.csv')
print(file.get_data(10,15))




        