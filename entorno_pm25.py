import numpy as np

class PM25Env:
    def __init__(self):
        self.states = [(p, b) for p in range(3) for b in range(3)]  # 3 niveles de PM2.5 x 3 niveles de biciusuarios
        self.actions = [0, 1, 2]  # Aumentar, mantener, reducir campañas
        self.state = (1, 1)  # Estado inicial: medio PM2.5 y biciusuarios
        self.done = False

    def reset(self):
        self.state = (1, 1)
        self.done = False
        return self.state

    def step(self, action):
        p, b = self.state

        # Lógica ficticia: acción 0 mejora PM2.5, acción 2 empeora
        if action == 0 and p > 0:
            p -= 1
            b = min(b + 1, 2)
            reward = 1
        elif action == 2 and p < 2:
            p += 1
            b = max(b - 1, 0)
            reward = -1
        else:
            reward = 0

        self.state = (p, b)
        self.done = p == 0 or p == 2  # termina si es muy bueno o muy malo
        return self.state, reward, self.done

    def get_state_index(self, state):
        return self.states.index(state)
