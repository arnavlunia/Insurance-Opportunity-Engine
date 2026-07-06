def segment(score):
    if score >= 75:
        return "HOT"
    elif score >= 35:
        return "WARM"
    else:
        return "COLD"