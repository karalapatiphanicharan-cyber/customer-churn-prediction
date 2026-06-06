import joblib
import os
import sys

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_project_root

class ModelLoader:
    _instance = None
    _model = None
    _pipeline = None
    _target_encoder = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            cls._load_artifacts()
        return cls._instance

    @classmethod
    def _load_artifacts(cls):
        project_root = get_project_root()
        artifacts_dir = os.path.join(project_root, 'artifacts')

        model_path = os.path.join(artifacts_dir, 'best_model.pkl')
        pipeline_path = os.path.join(artifacts_dir, 'preprocessing_pipeline.pkl')
        target_encoder_path = os.path.join(artifacts_dir, 'target_encoder.pkl')

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")
        if not os.path.exists(pipeline_path):
            raise FileNotFoundError(f"Pipeline not found at {pipeline_path}")

        cls._model = joblib.load(model_path)
        cls._pipeline = joblib.load(pipeline_path)
        cls._target_encoder = joblib.load(target_encoder_path)

    @property
    def model(self):
        return self._model

    @property
    def pipeline(self):
        return self._pipeline

    @property
    def target_encoder(self):
        return self._target_encoder

def get_model_loader():
    return ModelLoader()
