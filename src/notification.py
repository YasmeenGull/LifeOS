from plyer import notification


def send_desktop_notification(title, message):
    """
    Send a desktop notification.
    """

    try:
        notification.notify(
            title=title,
            message=message,
            app_name="LifeOS",
            timeout=10
        )

        print(f"Notification Sent: {title}")

    except Exception as error:

        print("Notification Error:", error)


def distraction_alert():
    """
    Notify user about distraction.
    """

    send_desktop_notification(
        "LifeOS Alert",
        "You have been distracted for too long. Stay focused!"
    )


def study_break_alert():
    """
    Notify user to take a break.
    """

    send_desktop_notification(
        "LifeOS Reminder",
        "Great work! Take a short break to refresh."
    )


def late_night_alert():
    """
    Notify user about late-night usage.
    """

    send_desktop_notification(
        "LifeOS Warning",
        "Late-night activity detected. Consider getting some rest."
    )