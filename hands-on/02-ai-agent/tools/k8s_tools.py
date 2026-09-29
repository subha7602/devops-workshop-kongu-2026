"""LangChain tools that shell out to kubectl to inspect a cluster."""

import subprocess

from langchain_core.tools import tool


def _run_kubectl(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["kubectl", *args],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except FileNotFoundError:
        return "kubectl not found. Is it installed and on your PATH?"
    except subprocess.TimeoutExpired:
        return "kubectl command timed out."


@tool
def list_pods() -> str:
    """List all pods across all namespaces in the current Kubernetes cluster."""
    return _run_kubectl(["get", "pods", "--all-namespaces"])


@tool
def describe_pod(pod_name: str, namespace: str = "default") -> str:
    """Get detailed status, events, and runtime info for a specific pod.

    Args:
        pod_name: Name of the pod to inspect.
        namespace: Namespace the pod lives in (default: "default").
    """
    return _run_kubectl(["describe", "pod", pod_name, "-n", namespace])


@tool
def find_unhealthy_pods() -> str:
    """List pods that are not in Running/Completed state, to spot issues quickly."""
    output = _run_kubectl(["get", "pods", "--all-namespaces"])
    lines = output.splitlines()
    if not lines:
        return "No pods found or kubectl returned no output."

    header, rows = lines[0], lines[1:]
    unhealthy = [row for row in rows if "Running" not in row and "Completed" not in row]

    if not unhealthy:
        return "All pods look healthy (Running/Completed)."

    return "\n".join([header, *unhealthy])
