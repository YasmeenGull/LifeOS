from datetime import datetime


def detect_distraction(dataframe):
    """
    Detect distraction activities.
    """

    distraction_apps = [
        "YouTube",
        "Facebook",
        "Instagram",
        "TikTok",
        "Netflix"
    ]

    for activity in dataframe["activity"]:

        if activity in distraction_apps:
            return True

    return False


def detect_long_study(dataframe):
    """
    Detect long study sessions.
    """

    total_duration = dataframe["duration"].sum()

    if total_duration >= 180:
        return True

    return False


def detect_late_night():
    """
    Detect late-night usage.
    """

    current_hour = datetime.now().hour

    if current_hour >= 23 or current_hour <= 5:
        return True

    return False


def get_trigger(dataframe):
    """
    Return detected trigger.
    """

    if detect_distraction(dataframe):
        return "DISTRACTION"

    if detect_long_study(dataframe):
        return "LONG_STUDY"

    if detect_late_night():
        return "LATE_NIGHT"

    return "NORMAL"