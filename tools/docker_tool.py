import docker

def check_docker():
    results = []
    try:
        client = docker.from_env()
        containers = client.containers.list()
        if not containers:
            results.append("No running Docker containers")
        for c in containers:
            results.append(f"{c.name} → {c.status}")
    except Exception as e:
        results.append(f"Docker error: {e}")
    return results

