import torch
import transformers
from typing import Literal


def _load_pipeline(
        model_name: Literal['Bllossom-ELO']
    ) -> transformers.Pipeline:
    """ load llm

    [Param]
    model_name : Literal['Bllossom-ELO']

    [Return]
    pipeline : transformers.Pipeline
    """
    if model_name in PIPELINE_BUFFER:
        return PIPELINE_BUFFER[model_name]

    if model_name == 'Bllossom-ELO':
        pipeline = transformers.pipeline(
            task='text-generation',
            model='MLP-KTLim/llama-3-Korean-Bllossom-8B',
            model_kwargs={'torch_dtype': torch.bfloat16},
            device_map='auto'
        )
        
        pipeline.model.eval()
    
    PIPELINE_BUFFER[model_name] = pipeline
    return pipeline


if __name__ == 'hate_speech_mitigation.utils._load_pipeline':
    PIPELINE_BUFFER = dict()
