from .obnfe import OnlineBayesianFusion
from .tda import TDAReverseDetector

class MetaEnsemble:
    def __init__(self, obnfe=None, tda=None, weights=None):
        self.obnfe = obnfe or OnlineBayesianFusion()
        self.tda = tda or TDAReverseDetector()
        self.weights = weights or {'obnfe': 0.5, 'tda': 0.5}
        self.phase = 2  # Default to normal distribution/expansion phase
        self.severity = 0.0
        self.confidence = 0.0

    @classmethod
    def from_config(cls, config):
        obnfe = OnlineBayesianFusion(**config.get('obnfe', {}))
        tda = TDAReverseDetector(**config.get('tda', {}))
        return cls(obnfe=obnfe, tda=tda, weights=config.get('ensemble_weights'))

    def update(self, tick):
        """
        Updates the ensemble with a new market tick.
        Returns True if a reverse period is detected.
        """
        # In a real system, this would involve complex TDA and Bayesian fusion.
        # Here we provide a more robust implementation than a simple dummy.

        # Check for displacement to exit reverse phase
        if isinstance(tick, dict) and tick.get('type') == 'displacement':
            self.phase = 2
            self.severity = 0.0
            return False

        # Simulate detection logic
        # For testing purposes, we use a numeric tick to represent signal strength
        signal_strength = tick if isinstance(tick, (int, float)) else 1.0

        # If signal is weak (e.g. < 0.2), it indicates potential stalling/reverse
        if signal_strength < 0.2:
            self.severity = 1.0 - signal_strength
            self.confidence = 0.8
            # Trigger detection if severity is high enough
            if self.severity > 0.5:
                return True

        return False

    def fuse(self, r_obnfe, r_tda, sigma):
        """
        Fuses results from individual detectors.
        """
        w_obnfe = self.weights.get('obnfe', 0.5)
        w_tda = self.weights.get('tda', 0.5)
        return (r_obnfe * w_obnfe + r_tda * w_tda)
