import subprocess
import sys
from pathlib import Path

# Ensure repository root is on the Python path so ``cluster`` can be imported
sys.path.append(str(Path(__file__).resolve().parents[2]))

from cluster.local.cluster_ips import get_local_container_ips


def test_get_local_container_ips_handles_missing_docker(monkeypatch):
    """If Docker is not installed, function should return empty lists."""

    def fake_run(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(subprocess, "run", fake_run)
    ips, udp_ports, tcp_ports = get_local_container_ips()
    assert ips == []
    assert udp_ports == []
    assert tcp_ports == []

