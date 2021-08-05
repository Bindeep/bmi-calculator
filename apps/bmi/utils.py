def calculate_bmi(weight: int, height: int) -> float:
    return weight / (height / 100) ** 2


UNDERWEIGHT = "You are underweight."
HEALTHY = "You are healthy."
OVERWEIGHT = "You are over weight."
SEVERELY_OVERWEIGHT = "You are severely over weight."
OBESE = "You are obese."
SEVERELY_OBESE = "You are severely obese."


def get_weight_group(bmi: float) -> str:
    """
    Calculate Weight Group w.r.to bmi
    """
    if bmi <= 18.4:
        weight_group = UNDERWEIGHT
    elif bmi <= 24.9:
        weight_group = HEALTHY
    elif bmi <= 29.9:
        weight_group = OVERWEIGHT
    elif bmi <= 34.9:
        weight_group = SEVERELY_OVERWEIGHT
    elif bmi <= 39.9:
        weight_group = OBESE
    else:
        weight_group = SEVERELY_OBESE

    return weight_group
