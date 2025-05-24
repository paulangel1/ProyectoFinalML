import numpy as np
import matplotlib.pyplot as plt
from entorno_pm25 import PM25Env

env = PM25Env()
q_table = np.zeros((9, 3))  # 9 estados x 3 acciones

alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodios = 500

rewards_totales = []

for ep in range(episodios):
    estado = env.reset()
    total_reward = 0
    done = False

    while not done:
        idx = env.get_state_index(estado)
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(env.actions)
        else:
            action = np.argmax(q_table[idx])

        siguiente_estado, reward, done = env.step(action)
        idx_siguiente = env.get_state_index(siguiente_estado)

        q_table[idx, action] = q_table[idx, action] + alpha * (
            reward + gamma * np.max(q_table[idx_siguiente]) - q_table[idx, action]
        )

        estado = siguiente_estado
        total_reward += reward

    rewards_totales.append(total_reward)

# Graficar evolución de recompensas
plt.plot(rewards_totales)
plt.title('Recompensa por episodio')
plt.xlabel('Episodio')
plt.ylabel('Recompensa total')
plt.savefig("static/recompensas.png")
plt.close()

np.save("models/q_table.npy", q_table)
