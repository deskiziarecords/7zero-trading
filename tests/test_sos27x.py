import pytest
from aegis.adelic_manifold.adelic_tube import AdelicTube as SOS27XProductionSystem

def test_initialization():
    system = SOS27XProductionSystem()
    assert system.max_positions == 3
    assert system.equity == 50000.0
