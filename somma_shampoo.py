
def somma_lista(file_name):
    valori=[]
    my_file=open(file_name, 'r')
    for line in my_file:
        linee_elem=line.split(',')
        if linee_elem[0] != 'Date':
            date = linee_elem [0]
            valore_singolo = linee_elem [1]

            valori.append(float(valore_singolo))
    my_file.close
    return (sum(valori))
print(somma_lista('shampoo_sales.csv'))
