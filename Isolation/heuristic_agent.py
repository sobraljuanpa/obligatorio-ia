from agent import Agent
from board import Board

class HeuristicAgent(Agent):
    def __init__(self, player=1):
        super().__init__(player)
    
    def next_action(self, obs):
        return self.best_action(obs)

    def split_actions(self, actions):
        actions_dict = {}
        
        for action in actions:
            move, coords = action
            if move not in actions_dict:
                actions_dict[move] = [coords]
            else:
                actions_dict[move].append(coords)

        return actions_dict
    
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
        return (player_moves - board_moves) + 0.5*(player_pos_bonus - board_pos_bonus)
    
    def best_action(self, board: Board):
        best_action = None
        max_score = float('-inf')

        for action in board.get_possible_actions(self.player):
            aux_board = board.clone()
            aux_board.play(action, self.player)
            current_score = self.minimax(aux_board, 0, False)
            
            if current_score > max_score:
                best_action = action
                max_score = current_score
        
        if best_action is None:
            best_action = board.get_possible_actions(self.player)[0]
        
        return best_action

    def minimax(self, board: Board, depth, is_maximizing):
        if board.is_end(self.player)[0]:
            if board.is_end(self.player)[1] == self.player:
                return 100
            else:
                return -100
        elif depth == 0:
            return self.heuristic_utility(board)

        if is_maximizing:
            max_score = float('-inf')
            for action in board.get_possible_actions(self.player):
                aux_board = board.clone()
                aux_board.play(action, self.player)
                score = self.minimax(aux_board, depth + 1, False)
                max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for action in board.get_possible_actions(self.board):
                aux_board = board.clone()
                aux_board.play(action, self.board)
                score = self.minimax(aux_board, depth + 1, True)
                min_score = min(min_score, score)
            return min_score
