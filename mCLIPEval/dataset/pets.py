from .base import TemplateDataSet
from torchvision.datasets import OxfordIIITPet

class Pets(TemplateDataSet):
    def __init__(self, **kwargs) -> None:
        if not hasattr(self, 'name'):
            self.name = 'pets' 
        super().__init__(name=self.name, **kwargs)
    
    def build(self, transform=None, verbose=False):
        ds = OxfordIIITPet(root=self.root_dir, split='test', target_types="category", transform=transform, download=False)
        self.classes = ds.classes
        if verbose:
            print(f'Creating Dataset: {self.name}')
            print(f"Dataset size: {len(ds)}")
            print(f"Dataset classes: {ds.classes}")
            print(f"Dataset number of classes: {len(ds.classes)}")
        return ds