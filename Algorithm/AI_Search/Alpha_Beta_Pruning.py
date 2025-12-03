import math

SCORES = [3, 5, 2, 9, 12, 5, 23, 23]
MAX_DEPTH = 3
NODE_INDEX = 0

def minimax_alpha_beta(depth, current_node_index, is_max_turn, alpha, beta):
    global NODE_INDEX

    # Base case
    if depth == MAX_DEPTH:
        value = SCORES[current_node_index]
        return value, current_node_index + 1

    if is_max_turn:
        max_eval = -math.inf
        for _ in range(2):
            eval_score, NODE_INDEX = minimax_alpha_beta(
                depth + 1, NODE_INDEX, False, alpha, beta
            )
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, max_eval)

            # Alpha-beta pruning
            if beta <= alpha:
                print(f"Pruning at depth {depth}: beta ({beta}) <= alpha ({alpha})")
                break

        return max_eval, NODE_INDEX

    else:
        min_eval = math.inf
        for _ in range(2):
            eval_score, NODE_INDEX = minimax_alpha_beta(
                depth + 1, NODE_INDEX, True, alpha, beta
            )
            min_eval = min(min_eval, eval_score)
            beta = min(beta, min_eval)

            # Alpha-beta pruning
            if beta <= alpha:
                print(f"Pruning at depth {depth}: beta ({beta}) <= alpha ({alpha})")
                break

        return min_eval, NODE_INDEX


# Run minimax
optimal_value, _ = minimax_alpha_beta(
    depth=0,
    current_node_index=0,
    is_max_turn=True,
    alpha=-math.inf,
    beta=math.inf
)

print("Optimal value:", optimal_value)
