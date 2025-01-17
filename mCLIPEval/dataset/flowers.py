from .base import TemplateDataSet
from torchvision.datasets import Flowers102

class Flowers(TemplateDataSet):
    def __init__(self, **kwargs) -> None:
        if not hasattr(self, 'name'):
            self.name = 'flowers' 
        super().__init__(name=self.name, **kwargs)
    
    def build(self, transform=None, verbose=False):
        ds = Flowers102(root=self.root_dir, split='test', transform=transform, download=False)
        ds.classes = self.classes
        if verbose:
            print(f'Creating Dataset: {self.name}')
            print(f"Dataset size: {len(ds)}")
            print(f"Dataset classes: {ds.classes}")
            print(f"Dataset number of classes: {len(ds.classes)}")
        return ds