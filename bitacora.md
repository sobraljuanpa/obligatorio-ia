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

## Experimentacion
Una vez logrado un agente satisfactorio, se procede a realizar investigacion sobre los hyperparametros de q learning.
Estos son los valores de epsilon inicial, epsilon final, discount factor y learning rate.

El agente de entrenamiento va a mantener la cantidad de iteraciones en 10 000 y la cantidad de bins constantes.

### Valores iniciales

| Parametro       | Valor          |
|-----------------|-------|
| Epsilon inicial |   |
| Epsilon final   |   |
| Discount factor |   |
| Learning rate   |   |

Info: The current hyperparameters are set to quickly train a decent agent. If you want to converge to the optimal policy, try increasing the n_episodes by 10x and lower the learning_rate

HABIENDO ENTRENADO YA EL MACACO CON 10K MUY BIEN GRACIAS AL POST, SE SUBE A 20K LA CANTIDAD DE ITERACIONES Y SE ARRANCA A PROBAR HYPERPARAMS HASTA ENCONTRAR UN MEJOR RESULTADO

| Parametro       | Valor |
|-----------------|-------|
| Epsilon inicial |  1    |
| Epsilon final   |  0.1  |
| Discount factor |  0.95 |
| Learning rate   |  0.1  |

malos resultados, se vuelve a valores originales y se intenta subir la cantidad de iteraciones para ver si converge a un valor aun mejor. En caso que no lo haga se va a aumentar la cantidad de bins

| Parametro       | Valor |
|-----------------|-------|
| Epsilon inicial |  1    |
| Epsilon final   |  0.1  |
| Discount factor |  0.95 |
| Learning rate   |  0.1  |

con 50kits no mejora demasiado, sigue estando el tope en 100 movimientos, se va a probar alterando los bins que abarcan mas datos a 5 
y se arranca d enuevo desde 10kits






PROBAR PARAM POR PARAM

EPSILON INICIAL POR EJ, DETERMINA EN QUE PUNTO MAS O MENOS DEL ENTRENAMIENTO SE PONE A EXPLOTAR
EPSILON FINAL, INDICA QUE TAN CLUSTEREADOS ESTAN LOS RESULTADOS A MEDIDA QUE NOS ACERCAMOS AL FINAL
LR NO SE AUN
DISCOUNT FACTOR NO SE AUN