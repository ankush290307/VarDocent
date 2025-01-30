class PipelineOrchestrator:
    """Detects available resources and optimizes workflow"""
    
    def __init__(self):
        self.executor = ('nextflow' if shutil.which('nextflow') 
                        else 'conda' if os.path.exists('envs/') 
                        else 'bare-metal')
