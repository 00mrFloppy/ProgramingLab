class NumericalCSVFile():

    # Definisco attributo che contenga il nome
    def __init__(self,file_name):
        self.name =file_name
 
    # Definisco il metodo che restituisca il CSV come lista di lista
    def get_data(self):
        # Creo la lsita dati vuota
        lista_dati=[]
        # Provo ad aprire il file, altrimenti genero un errore
        try:    
            my_file=open(self.name, 'r')
            # Ciclo il file CSV, elimino la , e tolgo il dacapo finale
            for i,line in enumerate(my_file):
                linee_elem=line.split(',')
                linee_elem[-1]=linee_elem[-1].strip()
                # Provo a convertire i numeri della seconda colonna a float, e poi carico nella lista da restituire a print
                try:
                    linee_elem[1]=float(linee_elem[1])
                    if linee_elem[0] != 'Date':
                        lista_dati.append(linee_elem)
                except Exception as errore:
                    if linee_elem[0] != 'Date':
                        print('Valore numerico non trovato nella seguente riga: "{}"'.format(linee_elem))
                        print('Presente nella riga numero: "{}"'.format(i+1))
                        print('E questo è l"Errore generato: "{}"'.format(errore))
                        print()

            my_file.close
            return lista_dati
            
        except Exception as errore:
            print('Errore: Non posso aprire il file')
            print('Questo è l"errore generato: "{}"'.format(errore))        

file=NumericalCSVFile('shampoo_sales_lezione5.csv')
print(file.get_data())



        