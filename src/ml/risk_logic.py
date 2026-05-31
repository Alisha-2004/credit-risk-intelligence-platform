def risk_score(probability):
    return round(probability * 100, 2)

def risk_band(score):

    if score < 30:
        return "Low Risk"

    elif score < 70:
        return "Medium Risk"

    else:
        return "High Risk"

def recommendation(score):

    if score > 70:
        return "Additional verification required"

    elif score > 40:
        return "Review manually"

    return "Eligible for standard approval"