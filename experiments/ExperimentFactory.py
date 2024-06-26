from experiments.segmentation import Segmentation

class ExperimentFactory:
    def __init__(self, config, debug=False):
        self.name = config.experiment.name
        self.config = config
        self.debug = debug

    def get(self):
        if self.name == 'Segmentation':
            experiment = Segmentation(self.config, self.debug)
        else:
            raise ValueError(f'Experiment \'{self.name}\' not found')
        return experiment
