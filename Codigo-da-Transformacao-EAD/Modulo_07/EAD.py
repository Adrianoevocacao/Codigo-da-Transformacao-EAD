class carro: 

    def __init__(self, marca, cor ):
        self.marca=marca
        self.cor=cor

        def buzinar(self):
            print(f'O{self.marca} da cor {self.cor} fez: bip bip!')

            meu_carro = carro('fiat , vermelho')
            
            carro_do_cliente = carro ('ford , azul')


            meu_carro.buzinar()
            carro_do_cliente.buzinar()        