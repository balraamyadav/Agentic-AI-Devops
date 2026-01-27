# agent/agent.py
from tools.docker_tool import check_docker
from tools.k8s_tool import check_kubernetes
from tools.alert_tool import check_alerts   # <- correct file name
from datetime import datetime

def run_agent(docker_enabled, k8s_enabled, alert_enabled, alert_url, interval, model):
    """
    Run Agentic DevOps AI checks for Docker, Kubernetes, and Alertmanager
    and log results with timestamps.
    """
    log = []
    log.append(f"Agent started @ {datetime.now()}")
    log.append(f"Model: {model}")

    # ---------------- Docker Check ----------------
    if docker_enabled:
        log.append(f"[{datetime.now()}] Running Docker Checks...")
        try:
            docker_logs = check_docker()
            log.extend(docker_logs)
        except Exception as e:
            log.append(f"[{datetime.now()}] Docker check failed: {e}")

    # --------------- Kubernetes Check -------------
    if k8s_enabled:
        log.append(f"[{datetime.now()}] Running Kubernetes Checks...")
        try:
            k8s_logs = check_kubernetes()
            log.extend(k8s_logs)
        except Exception as e:
            log.append(f"[{datetime.now()}] Kubernetes check failed: {e}")

    # --------------- Alertmanager Check ------------
    if alert_enabled:
        log.append(f"[{datetime.now()}] Checking Alertmanager at {alert_url}...")
        try:
            alert_logs = check_alerts(alert_url)
            log.extend(alert_logs)
        except Exception as e:
            log.append(f"[{datetime.now()}] Alertmanager check failed: {e}")

    # ---------------- Decision --------------------
    log.append(f"[{datetime.now()}] Decision: System analyzed successfully")

    return "\n".join(log)

