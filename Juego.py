import random
import sys
class Juego:
    OPCIONES_PERMITIDAS = ["roca", "papel", "tijera"]

    def __init__(self, elecciones_jugador):
        self.elecciones_jugador = elecciones_jugador
        self.elecciones_maquina = self.generar_elecciones_maquina()
        self.puntuacion_jugador = 0
        self.puntuacion_maquina = 0

    @property
    def elecciones_jugador(self):
        return self._elecciones_jugador

    @elecciones_jugador.setter
    def elecciones_jugador(self, nuevas_elecciones):
        self._elecciones_jugador = nuevas_elecciones

    @property
    def elecciones_maquina(self):
        return self._elecciones_maquina

    @elecciones_maquina.setter
    def elecciones_maquina(self, nuevas_elecciones_maquina):
        self._elecciones_maquina = nuevas_elecciones_maquina

    @property
    def puntuacion_jugador(self):
        return self._puntuacion_jugador

    @puntuacion_jugador.setter
    def puntuacion_jugador(self, nueva_puntuacion_jugador):
        self._puntuacion_jugador = nueva_puntuacion_jugador

    @property
    def puntuacion_maquina(self):
        return self._puntuacion_maquina

    @puntuacion_maquina.setter
    def puntuacion_maquina(self, nueva_puntuacion_maquina):
        self._puntuacion_maquina = nueva_puntuacion_maquina

    def iniciar_juego(self):
        if not self.validar_entradas():
            return

        self.ejecutar_rondas()
        self.mostrar_resumen()

    def validar_entradas(self):
        try:
            if len(self.elecciones_jugador) != 3:
                raise TypeError(f"Número incorrecto de elecciones: se proporcionaron {len(self.elecciones_jugador)}, se requieren 3.  Elecciones proporcionadas: {self.elecciones_jugador}")

            for eleccion in self.elecciones_jugador:
                if eleccion not in self.OPCIONES_PERMITIDAS:
                    raise ValueError(f"Elección inválida: '{eleccion}'. Las opciones válidas son: {self.OPCIONES_PERMITIDAS}")

            return True

        except (TypeError, ValueError) as error:
            print(f"Error: {error}")
            return False

    def generar_elecciones_maquina(self):
        return [random.choice(self.OPCIONES_PERMITIDAS) for _ in range(3)]

    def ejecutar_rondas(self):
        for ronda in range(len(self.elecciones_jugador)):
            resultado_ronda = self.determinar_ganador(self.elecciones_jugador[ronda], self.elecciones_maquina[ronda])

            if resultado_ronda == 1:
                self.puntuacion_jugador += 1
            elif resultado_ronda == -1:
                self.puntuacion_maquina += 1

    @staticmethod
    def determinar_ganador(eleccion_jugador, eleccion_maquina):
        if eleccion_jugador == eleccion_maquina:
            return 0
        elif (eleccion_jugador == Juego.OPCIONES_PERMITIDAS[0] and eleccion_maquina == Juego.OPCIONES_PERMITIDAS[2]) or \
             (eleccion_jugador == Juego.OPCIONES_PERMITIDAS[1] and eleccion_maquina == Juego.OPCIONES_PERMITIDAS[0]) or \
             (eleccion_jugador == Juego.OPCIONES_PERMITIDAS[2] and eleccion_maquina == Juego.OPCIONES_PERMITIDAS[1]):
            return 1
        else:
            return -1

    def mostrar_resumen(self):
        if self.puntuacion_jugador == self.puntuacion_maquina:
            ganador = "Empate"
        elif self.puntuacion_jugador > self.puntuacion_maquina:
            ganador = "Jugador"
        else:
            ganador = "Máquina"

        print(f"""
                Puntuación Jugador: {self.puntuacion_jugador}
                Puntuación Máquina: {self.puntuacion_maquina}
                Ganador: {ganador}
            """)





if __name__ == "__main__":
    
    juego = Juego(sys.argv[1:])
    juego.iniciar_juego()
