def calculate_bmi(weight: int, height: int) -> float:
    return weight / (height / 100) ** 2


def get_weight_group(bmi: float) -> str:
    """
    Calculate Weight Group w.r.to bmi
    """
    if bmi <= 18.4:
        weight_group = "You are underweight."
    elif bmi <= 24.9:
        weight_group = "You are healthy."
    elif bmi <= 29.9:
        weight_group = "You are over weight."
    elif bmi <= 34.9:
        weight_group = "You are severely over weight."
    elif bmi <= 39.9:
        weight_group = "You are obese."
    else:
        weight_group = "You are severely obese."

    return weight_group
