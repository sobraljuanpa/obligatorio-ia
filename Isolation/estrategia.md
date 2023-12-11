# Algoritmo
Se eligio implementar minimax dado que no hay aleatoriedad mas alla de la posicion inicial, y esa posicion inicial es a partir de la cual
se puede arrancar a analizar las decisiones que tome el agente.

El agente final utilizado fue ```final_agent.py``` y se jugo en ```isolation.ipynb```.

El agente logro un buen winrate con una profundidad de 2 movimientos (1 propio y 1 del oponente), logrando matchear el rendimiento de Stratagem con un runtime
de un tercio (12m 1000 jugadas agent vs stratagem, comparado con 35m 1000 jugadas stratagem vs agent).

Se probo tambien aumentar la profundidad en 1, simplemente para ver en igualdad de condiciones en cuanto al tiempo (mi agente es mas rapido) que tanta ventaja
podiamos obtener. Dado que no se estaba utilizando pruning, el tiempo de ejecucion resulto altisimo y no se presento una ganancia en rendimiento, por lo cual quedo descartado.

Luego se experimento con alfa beta pruning, pero los arboles no son tan altos como para ameritarlo. No logre que rinda igual que el agente que mira 2 movimientos
ni aumentando la profundidad a 6. Tal vez fue un problema de mi implementacion, pero me dio la impresion que estaba descartando ramas que no deberia, porque
rendia peor que un agente con un tercio de la profundidad pero sin pruning.

En conclusion, se logro una implementacion de minimax satisfactoria, creo que el exito estuvo en la buena calibracion de las heuristicas para luego ya 
dedicarme al tuneo del minimax.

# Heuristica

Para establecer la heuristica a utilizar se realizo benchmarking, utilizando una version modificada del agente final vs el Stratagem jugando 1000 partidas.
Se utilizo el notebook ```heuristic_test.ipynb``` en el cual se usa una funcion que cree para estos propositos: ```play_vs_other_agent_and_accumulate_results```.
El agente benchmarkeado es HeuristicAgent.

Se realiza minimax con profundidad 0, es decir, se realiza una accion y se evalua la heuristica, y se toma la mejor accion en funcion de eso.
Esto nos permitio experimentar bastante con la heuristica antes de comprometernos a una.

## Primer componente

La primer cosa a determinar es si vale la pena separar los movimientos de las acciones, es decir, si podemos tomar los movimientos como un componente separado que 
las destrucciones en la funcion de evaluacion.

### Rendimiento con acciones

``` py
def heuristic_utility(self, board):
        player_actions = board.get_possible_actions(self.player)
        board_actions = board.get_possible_actions(self.board)
        return (player_actions.__len__() - board_actions.__len__())
```

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  32.5%|
| Runtime         |  13min|

### Rendimiento con movimientos

``` py
def heuristic_utility(self, board):
        player_actions = board.get_possible_actions(self.player)
        board_actions = board.get_possible_actions(self.board)
        player_moves = self.split_actions(player_actions).keys().__len__()
        board_moves = self.split_actions(board_actions).keys().__len__()
        return (player_moves - board_moves)
```

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  34.7%|
| Runtime         |  12min|


Conclusion, vale mas la pena guiarse solamente por los movimientos posibles que por las acciones totales (lo cual tiene sentido).

## Segundo componente

Se hablo con el profe de practico en busqueda de mejorar la heuristica, y nos sugirio la distancia al centro como un potencial componente extra.
En lugar de calcular la distancia al centro en si, decidi dar un bonus si se encontraba en alguna de las 4 posiciones centrales ((1,1)(1,2),(2,2),(2,1)).

Se decidio tambien benchmarkear esta heuristica sola, no se espera que sea tan buena como la anterior simplemente un extra para que rinda aun mejor.

```py
def heuristic_utility(self, board):
        player_col, player_row = board.find_player_position(self.player)
        board_col, board_row = board.find_player_position(self.board)
        player_pos_bonus, board_pos_bonus = 0, 0
        if player_col == 1 or player_col == 2:
            player_pos_bonus += 2
        if player_row == 1 or player_row == 2:
            player_pos_bonus += 2
        if board_col == 1 or board_col == 2:
            board_pos_bonus += 2
        if board_row == 1 or board_row == 2:
            board_pos_bonus += 2
        return (player_pos_bonus - board_pos_bonus)
```

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  32.2%|
| Runtime         |  12min|

Alentadores, tenemos nuestro segundo compoente para la heuristica

## Heuristica final

Para definir la heuristica final, seguimos experimentando con heuristic_agent, la idea es determinar los pesos, partiendo de 1, 1

```py
def heuristic_utility(self, board):
        player_col, player_row = board.find_player_position(self.player)
        board_col, board_row = board.find_player_position(self.board)
        player_actions = board.get_possible_actions(self.player)
        board_actions = board.get_possible_actions(self.board)
        player_moves = self.split_actions(player_actions).keys().__len__()
        board_moves = self.split_actions(board_actions).keys().__len__()
        player_pos_bonus, board_pos_bonus = 0, 0
        if player_col == 1 or player_col == 2:
            player_pos_bonus += 2
        if player_row == 1 or player_row == 2:
            player_pos_bonus += 2
        if board_col == 1 or board_col == 2:
            board_pos_bonus += 2
        if board_row == 1 or board_row == 2:
            board_pos_bonus += 2
        return (player_moves - board_moves) + (player_pos_bonus - board_pos_bonus)
```

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  32.6%|
| Runtime         |  12min|

Se prueba con pesos 1, 0.75 

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  32.1%|
| Runtime         |  12min|

Se prueba con pesos 1, 0.5 

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  34.6%|
| Runtime         |  12min|

Buenos resultados, comparables a los conseguidos con 1 de los componentes de la heuristica en el mejor caso obtenido.
Ultima prueba con pesos 1, 0.25 dado que la reduccion del peso del componente de posicion fue positiva

| Parametro       | Valor |         
|-----------------|-------|
| Cant iteraciones| 1000  |
| Winrate         |  32.5%|
| Runtime         |  12min|

Dada la reduccion en performance vamos a mantener el peso del segundo componente en 0.5, tambien podriamos reducir el bonus a +1 y alcanzar el mismo resultado.

# Niveles
Teniendo seleccionados los componentes y peso para la heuristica, corresponde aumentar la cantidad de niveles que se van a analizar.

Se va a benchmarkear utilizando el notebook ```isolation.ipynb``` y el agente ```final_agent.py```, pero con una nueva metodologia. Dado que el ir primero o segundo 
tiene un impacto tangible sobre los resultados, se van a ejecutar 1000 partidas con el agente yendo primero y 1000 partidas con el agente yendo segundo.

### 2 niveles

2 niveles quiere decir que el agente revisa los potenciales movimientos del oponente. Es decir, dado un estado, simula un movimiento y luego simula tambien 
la respuesta del oponente a ese movimiento.

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Winrate primero |  69.4%|
| Runtime primero |  12min|
| Winrate segundo |  69.2%|
| Runtime segundo |  35min|

Bueno, nuestro agente es objetivamente mejor que el agente contra el que competimos. Podriamos dar por terminado el ejercicio pero vamos a benchmarkear tambien 2
niveles. Solamente quiero ver cuanto mejor puede hacer rendir a mi agente yendo primero, dado que basandome en el runtime de este experimento anterior, yendo
segundo seguramente este 1h o mas.


### 3 niveles

Ahora el agente proyecta 1 jugada mas alla de la respuesta del oponente al movimiento inicial.

Los resultados fueron los siguientes:

| Parametro       | Valor |         
|-----------------|-------|
| Winrate primero |  67.9%|
| Runtime primero |  90min|

Sorprendentemnete los resultados no solamente no mejoraron si no que empeoraron, y el tiempo de ejecucion es altisimo tambien, por lo cual no se va a utilizar
esta cantidad de niveles