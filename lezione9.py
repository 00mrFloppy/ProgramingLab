class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato') 

# creo una classe per la definizione della media degli n valori scelti
        
class FitIncrementModel(Model):        
    def final_avg_increment(self, data):
        #creo un primo valore nullo al fine di non far la differenza sul primo numero 
        # ed una lista di voalori che saranno gli incrementi singoli
        prev_value_final= None
        differenze_valore_n=[]
        # itero sui valori della lista, se è il primo valore lo salto e lui diventa l'ultimo valore
        # una volta che il primo valore diventa il secondo posso fare l edifferenze e inserirle in una lista mediate (diviso due essendo l'incremento di mese in mese) 
        if len(data) > 1:
            for value in data:
                    for item in data:
                        if prev_value_final is None:
                            prev_value_final=value
                        else:
                            valore = (value-prev_value_final)
                            prev_value_final=value
                            differenze_valore_n.append(valore)
                # sommo la sigola liste delle differenze mediate e lo sommo all'ultimo valore della lista      
            final_avg_incremented=(sum(differenze_valore_n)/(len(data)-1))
            print(final_avg_incremented)
            return final_avg_incremented
        else:
            raise Exception('Hai inserito solo un valore, non posso fare predizioni')            

            
# creo una classe per la definizione della media del dataset, ossia dei valori precedenti gli n
    def global_avg_increment(self, dataset):
            #creo un primo valore nullo al fine di non far la differenza sul primo numero 
            # ed una lista di voalori che saranno gli incrementi singoli
            prev_value= None
            differenze_valore_dataset=[]
            # itero sui valori della lista, se è il primo valore lo salto e lui diventa l'ultimo valore
            # una volta che il primo valore diventa il secondo posso fare l edifferenze e inserirle in una lista mediate (diviso due essendo l'incremento di mese in mese) 
            if len(dataset) > 1:
                for item in dataset:
                    if prev_value is None:
                        prev_value=item
                    else:
                        valore = (item-prev_value)
                        prev_value=item
                        differenze_valore_dataset.append(valore)
                # sommo la sigola liste delle differenze mediate e lo sommo all'ultimo valore della lista      
                global_incremented =(sum(differenze_valore_dataset))/(len(differenze_valore_dataset))
                print(global_incremented) 
                return global_incremented
            else:
                raise Exception('Hai inserito solo un valore, non posso fare predizioni') 


    def predict(self, globaldata, listan):
        total_avg_prediction=(self.global_avg_increment(globaldata)+self.final_avg_increment(listan))/2
        print(listan[-1])
        prediction= listan[-1]+total_avg_prediction
        return prediction
    
            
#==============================
#  Corpo del programma
#==============================
mia_lista = [8,19,31,41]
lista_n = [50,52,60]

increment_model = FitIncrementModel()
prediction_value = increment_model.predict(mia_lista, lista_n)
print(prediction_value)