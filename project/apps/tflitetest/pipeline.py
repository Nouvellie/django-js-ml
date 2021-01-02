from collections import OrderedDict
from pathlib import Path
from typing import (
    List, 
    Optional,
    Tuple,
)

import json

FUNCTIONS_PIPELINE = OrderedDict()


def register_in_pipeline(func,):
    """Collect functions for the pipeline"""
    # print(f"{func.__name__} registered in Pipeline")
    if func.__name__ not in FUNCTIONS_PIPELINE:
        FUNCTIONS_PIPELINE[func.__name__] = func
    else:
        raise Exception(f"Duplicated function with name {func.__name__}")


class Pipeline:
    """Build a pipeline of functions
    Pipeline structure: ("func_name", args, kwargs) or ("func_name", kwargs)
    x -> Pipeline(x) -> new_x
    """
    FUNCTIONS_PIPELINE = FUNCTIONS_PIPELINE
    def __init__(self, pipeline: Optional[List[Tuple[str, dict]]] = None):
        self.pipeline = pipeline if pipeline else []


    def __call__(self, x,):
        """Apply pipeline to the input 'x'"""
        for pipe in self.pipeline: 
            func_name, *args, kwargs = pipe
            assert isinstance(kwargs, dict), f"Wrong declaration in {func_name!r}. Must be (str, dict) or (str, tuple, dict)"

            # Apply preprocessing
            if args: 
                # args and kwargs provided
                x = self.apply(x, func_name, *args, **kwargs)
            
            else:
                # only kwargs provided
                x = self.apply(x, func_name, **kwargs)
        
        return x


    @classmethod
    def apply(cls, x, func, *args, **kwargs,):
        """Compute func(x, *args, **kwargs)"""
        if func in cls.FUNCTIONS_PIPELINE:
            return cls.FUNCTIONS_PIPELINE[func](x, *args, **kwargs)
        
        else:
            raise TypeError(f"{func} not available")
    

    def __gt__(self, add_pipe,):
        """Add a pipe ("func_name", args, kwargs)/("func_name", kwargs) to the current pipeline"""
        if self.is_available(add_pipe[0]):
            # print(f"adding {add_pipe[0]!r} to pipeline")
            self.pipeline.append(add_pipe)
            return self.__class__(self.pipeline)
       
        else:
            raise NotImplementedError(f"{add_pipe[0]!r} not available in Pipeline")       


    def is_available(self, func_name,):
        """Return True if the function 'func_name' is available in Pipeline"""
        return True if func_name in self.FUNCTIONS_PIPELINE else False


    def asJSON(self, path_save=None,):
        path_save = Path(path_save) if path_save else Path("pipeline.json")

        with open(path_save, "w", encoding="utf8") as fp:
            json.dump(self.pipeline, fp, indent=4, ensure_ascii=False)
        # print(f"Pipeline configuration saved at {path_save!r}")


    def fromJSON(self, path_pipeline,):
        # Rear pipeline
        path_pipeline = Path(path_pipeline)

        with open(path_pipeline, "r", encoding="utf8") as fp: 
            pipeline = json.load(fp)
        
        # Corrobate that all functions are availables
        available_functions = {
            pipe[0]: self.is_available(pipe[0]) for pipe in pipeline
        }
        
        if not all(available_functions.values()): 
            print("Functions not availables:")
            functions_not_availables = dict(filter(lambda item: item[0], available_functions.items()))
        
            return [
                func_name for func_name, available in functions_not_availables.items() if available is False
            ]
        
        self.pipeline = pipeline
        # print("\n", f"Pipeline loaded from {path_pipeline!r}")