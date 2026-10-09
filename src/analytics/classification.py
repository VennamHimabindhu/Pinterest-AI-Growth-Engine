def calculate_percentile(score, all_scores):
    if len(all_scores) <= 1:
        return 100.0

    sorted_scores = sorted(all_scores)
    rank = sorted_scores.index(score)

    return (rank / (len(sorted_scores) - 1)) * 100


def get_data_status(impressions):
    if impressions == 0:
        return "insufficient_data"

    if impressions < 100:
        return "early_signal"

    if impressions < 1000:
        return "developing_signal"

    return "usable_signal"


def classify_performance(percentile, impressions):
    data_status = get_data_status(impressions)

    if data_status in ["insufficient_data", "early_signal"]:
        return data_status

    if percentile >= 80:
        return "winner"

    if percentile <= 20:
        return "laggard"

    return "normal"