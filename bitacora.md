# Bitacora del capitan

## Primer contacto

Se decide experimentar siguiendo el tutorial https://gymnasium.farama.org/tutorials/training_agents/blackjack_tutorial/ de blackjack que implementa q-learning.

### Notas

Luego de seguido el tutorial de blackjack, se hizo benchmarking del algoritmo en el ambiente de cartpole.

Se probo con un agente random y luego entrenando, logrando una mejora de casi x10 en las recompensas totales.

Conclusion q learning funciona, falta ver un par de temas:

    Como almacenar el modelo entre ejecuciones (investigar pickle)
    Como benchmarkear el modelo una vez entrenado
    Probar cambios con los valores que vienen por defecto