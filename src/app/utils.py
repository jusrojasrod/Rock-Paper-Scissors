CLASS_MAP = {
    'Rock': "Piedra",
    'Paper': 'Papel',
    'Scissors': 'Tijera'
}

def determine_winner(pred_a, pred_b, conf_thresh=0.4):
    """
    Determine the winner between two players based on their predictions.

    Parameters
    ----------
    pred_a: 
    pred_b: 
    conf_thresh: float, optional 
        by default 0.4.
        
    Returns
    -------
    winner: str
        "player_a", "player_b", "tie", or "undecided"
        
    """
    if not pred_a or pred_a["confidense" < conf_thresh]:
        return "undecided", "low confidence in player a"
    if not pred_b or pred_b["confidense" < conf_thresh]:
        return "undecided", "low confidence in player b"
    
    a_es = pred_a["prediction"]
    b_es = pred_b["prediction"]
    
    if a_es == b_es:
        return "tie", f"both players chose {a_es}"
    
    rules = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }
    
    if rules.get(a_es) == b_es:
        return "player_a", f"{a_es} beats {b_es}"
    else:
        return "playes_b", f"{b_es} beats {a_es}"