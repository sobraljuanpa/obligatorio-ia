def play_vs_other_agent(env, agent1, agent2, render = False):
    done = False
    obs = env.reset()
    winner = 0
    while not done:
        if render: env.render()
        action = agent1.next_action(obs)
        obs, _, done, winner, _ = env.step(action)
        
        if render: env.render()
        if not done:
            next_action = agent2.next_action(obs)
            _, _, done, winner, _ = env.step(next_action)

    if render: env.render()
    final_msg = "Player " + str(winner) + " WON"
    print(final_msg)

def play_vs_other_agent_and_accumulate_results(env, agent1, agent2, count):
    agent1_wins = 0
    agent2_wins = 0
    for i in range(count):
        done = False
        obs = env.reset()
        winner = 0
        while not done:
            action = agent1.next_action(obs)
            obs, _, done, winner, _ = env.step(action)
            
            if not done:
                next_action = agent2.next_action(obs)
                _, _, done, winner, _ = env.step(next_action)

        if winner == 1:
            agent1_wins += 1
        else:
            agent2_wins += 1
    print("Agent 1 wins: " + str(agent1_wins))
    print("Agent 2 wins: " + str(agent2_wins))
