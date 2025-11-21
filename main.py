# main.py - ejemplo mínimo AutoGen (simulado si no tienes LLM)
# Este es un ejemplo educativo que demuestra la arquitectura.
class Agent:
    def __init__(self, name):
        self.name = name
    def send(self, msg, to):
        print(f"[{self.name} -> {to.name}]: {msg}")

strategist = Agent("Strategist")
analyst = Agent("Analyst")
writer = Agent("Writer")

# Flujo simulado
strategist.send("Define la estrategia para el correo a VELOX", analyst)
analyst.send("Puntos clave: experiencia, tiempos, tarifa preferencial", writer)
writer.send("Borrador: Estimado..., ofrecemos...", strategist)
print("Flujo AutoGen simulado finalizado.")
