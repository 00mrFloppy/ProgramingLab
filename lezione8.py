class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato') 

class IncrementModel(Model):
    def predict(self, data):
        #creo un primo valore nullo al fine di non far la differenza sul primo numero 
        # ed una lista di voalori che saranno gli incrementi singoli
        prev_value= None
        differenze_valore=[]
        # itero sui valori della lista, se è il primo valore lo salto e lui diventa l'ultimo valore
        # una volta che il primo valore diventa il secondo posso fare l edifferenze e inserirle in una lista mediate (diviso due essendo l'incremento di mese in mese) 
        for item in data:
            if prev_value is None:
               prev_value=item
            else:
               valore = (item-prev_value)/2
               prev_value=item
               differenze_valore.append(valore)
        # sommo la sigola liste delle differenze mediate e lo sommo all'ultimo valore della lista      
        prediction =(sum(differenze_valore))+item
        return prediction

#==============================
#  Corpo del programma
#==============================
mia_lista = [0,2,10]

increment_model = IncrementModel()
prediction_value = increment_model.predict(mia_lista)
print(prediction_value)