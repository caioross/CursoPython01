# trabalhando com orientação a objeto e polimorfismo

class Animal :
    def fazer_som(self):
        pass

class Cachorro(Animal) :
    def fazer_som(self):
       return "Au au"

class Gato(Animal) :
    def fazer_som(self):
        return "Miau"
    
# Usando o polimorfismo 
def fazer_animal_falar(x: Animal) :
    print(x.fazer_som())

#criando os objetos
cachorro = Cachorro()
gato = Gato()

# chamando o metodo de cada animal de forma polimorfica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)
