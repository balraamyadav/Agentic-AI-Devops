# tools/alert_tool.py
import requests

def check_alerts(alert_url="http://localhost:9093"):
    """
    Check Alertmanager for active alerts
    Returns a list of log strings
    """
    logs = []
    try:
        response = requests.get(f"{alert_url}/api/v2/alerts", timeout=5)
        if response.status_code == 200:
            alerts = response.json()
            if alerts:
                logs.append(f"Active Alerts: {len(alerts)}")
                for alert in alerts:
                    logs.append(f"- {alert.get('labels', {})}")
            else:
                logs.append("No active alerts found")
        else:
            logs.append(f"Alertmanager returned status code {response.status_code}")
    except Exception as e:
        logs.append(f"Failed to connect to Alertmanager: {e}")

    return logs

