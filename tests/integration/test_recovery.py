import pytest
import numpy as np
from aegis.zeta_flux.reverse_period.meta.ensemble import MetaEnsemble

def generate_stalled_distribution(bars=20, volatility=0.3):
    """Generate synthetic regime: bars of distribution-without-expansion (stalled)"""
    # Mocking stalled signal as small values
    return [0.1 for _ in range(bars)]

def generate_displacement(atr_multiple=2.5):
    """Generate displacement tick"""
    return {'type': 'displacement', 'value': atr_multiple}

@pytest.mark.slow
def test_reverse_period_recovery():
    """Full pipeline: synthetic chop → reverse detected → displacement → normal"""
    
    # Generate synthetic regime: 20 bars of distribution-without-expansion
    synthetic = generate_stalled_distribution(bars=20, volatility=0.3)
    
    detector = MetaEnsemble.from_config({'obnfe': {}, 'tda': {}})
    reverses = []
    
    for tick in synthetic:
        r = detector.update(tick)
        reverses.append(r)
    
    # Should trigger reverse period
    assert any(reverses[10:18])  # Mid-period detection
    
    # Add displacement
    displacement_tick = generate_displacement(atr_multiple=2.5)
    r_post = detector.update(displacement_tick)
    
    # Should exit reverse mode
    assert detector.phase == 2  # Back to distribution/expansion
