import subprocess
from datetime import datetime

def get_pods(namespace="default"):
    """
    Returns Kubernetes pod status for a namespace
    """
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace],
            capture_output=True,
            text=True
        )
        return result.stdout.splitlines()
    except Exception as e:
        return [f"Error getting pods: {e}"]

def get_nodes():
    """
    Returns Kubernetes node status
    """
    try:
        result = subprocess.run(
            ["kubectl", "get", "nodes"],
            capture_output=True,
            text=True
        )
        return result.stdout.splitlines()
    except Exception as e:
        return [f"Error getting nodes: {e}"]

def check_kubernetes():
    """
    Full Kubernetes health check
    """
    logs = [f"[{datetime.now()}] Kubernetes Health Check"]

    # Nodes
    logs.append("Nodes:")
    nodes = get_nodes()
    logs.extend(nodes)

    # Pods (default namespace)
    logs.append("Pods (default namespace):")
    pods = get_pods("default")
    logs.extend(pods)

    return logs

