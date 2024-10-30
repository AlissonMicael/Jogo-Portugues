import time


class Cronometro:
    def __init__(self):
        self.inicio = None
        self.pausado = False
        self.pausa_inicial = None
        self.total_pausa = 0

    def iniciar(self):
        self.inicio = time.time()

    def pausar(self):
        if not self.pausado:
            self.pausa_inicial = time.time()
            self.pausado = True

    def retomar(self):
        if self.pausado:
            pausa_atual = time.time()
            self.total_pausa += pausa_atual - self.pausa_inicial
            self.pausado = False

    def reiniciar(self):
        self.inicio = None
        self.pausado = False
        self.pausa_inicial = None
        self.total_pausa = 0

    def tempo_decorrido(self):
        if self.inicio is None:
            return 0

        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - self.inicio - self.total_pausa
        return tempo_decorrido

