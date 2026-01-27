import sys
import os
import time

# --------------------------------------------------
# Ensure project root is in PYTHONPATH
# --------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# --------------------------------------------------
# Imports
# --------------------------------------------------
import streamlit as st
from agent.agent import run_agent

# --------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Agentic DevOps AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.title("🤖 Agentic DevOps AI Platform")
st.caption("AI-powered monitoring for Docker, Kubernetes & Alertmanager")

# --------------------------------------------------
# Sidebar Configuration
# --------------------------------------------------
st.sidebar.header("🔧 Configuration")

docker_enabled = st.sidebar.checkbox(
    "Enable Docker Checks",
    value=True
)

k8s_enabled = st.sidebar.checkbox(
    "Enable Kubernetes Checks",
    value=True
)

alert_enabled = st.sidebar.checkbox(
    "Enable Alertmanager Checks",
    value=True
)

alert_url = st.sidebar.text_input(
    "Alertmanager URL",
    value="http://localhost:9093"
)

interval = st.sidebar.slider(
    "Agent Interval (seconds)",
    min_value=10,
    max_value=300,
    value=60,
    step=10
)

model = st.sidebar.selectbox(
    "LLM Model",
    options=["llama3", "mistral", "phi"],
    index=0
)

auto_refresh = st.sidebar.checkbox(
    "🔄 Auto refresh",
    value=False
)

# --------------------------------------------------
# Run Agent Button
# --------------------------------------------------
st.markdown("---")

if st.button("🚀 Run Agent", use_container_width=True):
    with st.spinner("Running DevOps Agent..."):
        output = run_agent(
            docker_enabled=docker_enabled,
            k8s_enabled=k8s_enabled,
            alert_enabled=alert_enabled,
            alert_url=alert_url,
            interval=interval,
            model=model
        )

    st.success("✅ Agent execution completed")
    st.code(output, language="text")

# --------------------------------------------------
# Auto Refresh Logic
# --------------------------------------------------
if auto_refresh:
    time.sleep(interval)
    st.experimental_rerun()

