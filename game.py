import random

class Play (): 
    
    # La lista debe ir en este orden ["piedra","papel","tijera"]
    PERMITIDOS = ["piedra","papel","tijera"]
    
    def __init__(self, jugadas):
        self.__jugadas = jugadas
        self.__jugadasMaquina = self.maquinaJugadas()
        self.__scorePlayer = 0
        self.__scoreMaquina = 0
        
        
    @property
    def jugadas(self):
        return self.__jugadas
    
    @jugadas.setter
    def jugadas(self,newListJugadas):
        self.__jugadas = newListJugadas
    
    @property
    def jugadasMaquina(self):
        return self.__jugadasMaquina
    
    @jugadasMaquina.setter
    def jugadasMaquina(self,newListJugadasMaquina):
        self.__jugadasMaquina = newListJugadasMaquina
        
    @property
    def scorePlayer(self):
        return self.__scorePlayer
        
    @scorePlayer.setter
    def scorePlayer(self,newScorePlayer):
        self.__scorePlayer = newScorePlayer
        
    @property
    def scoreMaquina(self):
        return self.__scoreMaquina

    @scoreMaquina.setter
    def scoreMaquina(self,newScoreMaquina):
        self.__scoreMaquina = newScoreMaquina

    def startGame(self):
        if not self.validations():
            return
        
        self.maquinaVsPlayer()
        
        self.feedback()
        
    def validations(self):
        
        try:
            if len(self.jugadas) != 3:
                raise TypeError(f"No hay suficientes parametros en la jugada: hay {len(self.jugadas)} los cuales son {self.jugadas}: pero se necesitan 3")
            
            for jugada in self.jugadas :
                if not jugada in self.PERMITIDOS:
                    raise TypeError(f"La juagada ' {jugada} ' no existe, solo puedes usar estas juagadas {self.PERMITIDOS}")
            
            return True
        
        except TypeError as e:
            print(f"Error de tipo: {e}")
            return False
    
    def maquinaJugadas(self):
        jugadasMaquina = []
        
        for juagadaEscojer in range(3):
            jugadasMaquina.append(random.choice(self.PERMITIDOS))
            
        return jugadasMaquina
    
    def maquinaVsPlayer(self):
        print ('----- JUEGO -----\n')
        for jugadasVs in range(len(self.jugadas)):
            
            verificacion = self.processGanador(playerJ=self.jugadas[jugadasVs] , maquinaJ=self.jugadasMaquina[jugadasVs])
            
            if verificacion == 1:
                self.scorePlayer += 1
            elif verificacion == -1:
                self.scoreMaquina +=1
            
    
    @staticmethod
    def processGanador(playerJ , maquinaJ):
        
        if playerJ == maquinaJ:
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Empate -- No gana nadie\n")
            return 0
        
        elif (playerJ == Play.PERMITIDOS[0] and maquinaJ == Play.PERMITIDOS[2]) or \
            (playerJ == Play.PERMITIDOS[1] and maquinaJ == Play.PERMITIDOS[0]) or \
            (playerJ == Play.PERMITIDOS[2] and maquinaJ == Play.PERMITIDOS[1]):
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Ganador -- Player\n")
            return 1
        
        else:
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Ganador -- Maquina\n")
            return -1
    
    def feedback(self):
        
        ganador = ""
        
        if (self.scorePlayer == self.scoreMaquina):
            ganador = "Empate"
        
        elif (self.scorePlayer > self.scoreMaquina):
            ganador = "Player"
        
        else:
            ganador = "Maquina"
        
        print(f"""
            
            ----- FEEDBACK -----
            
            Player: -- {self.scorePlayer}
            
            Maquina: -- {self.scoreMaquina}
            
            Ganador: -- {ganador}
            
            """)
    PERMITIDOS = ["piedra","papel","tijera"]
    
    def _init_(self, jugadas):
        self.__jugadas = jugadas
        self.__jugadasMaquina = self.maquinaJugadas()
        self.__scorePlayer = 0
        self.__scoreMaquina = 0
        
        
    @property
    def jugadas(self):
        return self.__jugadas
    
    @jugadas.setter
    def jugadas(self,newListJugadas):
        self.__jugadas = newListJugadas
    
    @property
    def jugadasMaquina(self):
        return self.__jugadasMaquina
    
    @jugadasMaquina.setter
    def jugadasMaquina(self,newListJugadasMaquina):
        self.__jugadasMaquina = newListJugadasMaquina
        
    @property
    def scorePlayer(self):
        return self.__scorePlayer
        
    @scorePlayer.setter
    def scorePlayer(self,newScorePlayer):
        self.__scorePlayer = newScorePlayer
        
    @property
    def scoreMaquina(self):
        return self.__scoreMaquina

    @scoreMaquina.setter
    def scoreMaquina(self,newScoreMaquina):
        self.__scoreMaquina = newScoreMaquina

    def startGame(self):
        if not self.validations():
            return
        
        self.maquinaVsPlayer()
        
        self.feedback()
        
    def validations(self):
        
        try:
            if len(self.jugadas) != 3:
                raise TypeError(f"No hay suficientes parametros en la jugada: hay {len(self.jugadas)} los cuales son {self.jugadas}: pero se necesitan 3")
            
            for jugada in self.jugadas :
                if not jugada in self.PERMITIDOS:
                    raise TypeError(f"La juagada ' {jugada} ' no existe, solo puedes usar estas juagadas {self.PERMITIDOS}")
            
            return True
        
        except TypeError as e:
            print(f"Error de tipo: {e}")
            return False
    
    def maquinaJugadas(self):
        jugadasMaquina = []
        
        for juagadaEscojer in range(3):
            jugadasMaquina.append(random.choice(self.PERMITIDOS))
            
        return jugadasMaquina
    
    def maquinaVsPlayer(self):
        print ('----- JUEGO -----\n')
        for jugadasVs in range(len(self.jugadas)):
            
            verificacion = self.processGanador(playerJ=self.jugadas[jugadasVs] , maquinaJ=self.jugadasMaquina[jugadasVs])
            
            if verificacion == 1:
                self.scorePlayer += 1
            elif verificacion == -1:
                self.scoreMaquina +=1
            
    
    @staticmethod
    def processGanador(playerJ , maquinaJ):
        
        if playerJ == maquinaJ:
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Empate -- No gana nadie\n")
            return 0
        
        elif (playerJ == Play.PERMITIDOS[0] and maquinaJ == Play.PERMITIDOS[2]) or \
            (playerJ == Play.PERMITIDOS[1] and maquinaJ == Play.PERMITIDOS[0]) or \
            (playerJ == Play.PERMITIDOS[2] and maquinaJ == Play.PERMITIDOS[1]):
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Ganador -- Player\n")
            return 1
        
        else:
            #print(f"--- Player -{playerJ}-  VS  -{maquinaJ}- Maquina --- Ganador -- Maquina\n")
            return -1
    
    def feedback(self):
        
        ganador = ""
        
        if (self.scorePlayer == self.scoreMaquina):
            ganador = "Empate"
        
        elif (self.scorePlayer > self.scoreMaquina):
            ganador = "Player"
        
        else:
            ganador = "Maquina"
        
        print(f"""
            
            ----- FEEDBACK -----
            
            Player: -- {self.scorePlayer}
            
            Maquina: -- {self.scoreMaquina}
            
            Ganador: -- {ganador}
            
            """)