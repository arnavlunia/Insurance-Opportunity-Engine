def segment(score):
    if score >= 70:
        return "HOT"
    elif score >= 30:
        return "WARM"
    else:
        return "COLD"