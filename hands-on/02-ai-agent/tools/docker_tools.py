"""LangChain tools that shell out to the Docker CLI to inspect containers."""

import subprocess

from langchain_core.tools import tool


def _run_docker(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["docker", *args],
            capture_output=True,
            text=True,
            timeout=15,
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except FileNotFoundError:
        return "docker not found. Is Docker installed and running?"
    except subprocess.TimeoutExpired:
        return "docker command timed out."


@tool
def list_containers() -> str:
    """List currently running Docker containers."""
    return _run_docker(["ps"])


@tool
def inspect_container(container_name: str) -> str:
    """Get detailed configuration and state info for a specific container.

    Args:
        container_name: Name or ID of the container to inspect.
    """
    return _run_docker(["inspect", container_name])


@tool
def container_logs(container_name: str, tail: int = 50) -> str:
    """Fetch recent logs from a specific container.

    Args:
        container_name: Name or ID of the container.
        tail: Number of recent log lines to return (default: 50).
    """
    return _run_docker(["logs", "--tail", str(tail), container_name])
