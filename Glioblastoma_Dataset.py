import os
from PIL import Image
from torch.utils.data import Dataset

class Glioblastoma(Dataset):
    def __init__(self, path, transform=None):
        self.path = path
        self.transform = transform
        self.data = []
        sortedFiles = sorted(os.listdir(path))
        for fileName in sortedFiles:
            sections = fileName.split("_")
            weekSections = sections[1].split("-")
            week = int(weekSections[1])
            year = week//52
            mode = sections[2].lower()
            pathology = f"year {year} {mode}"
            self.data.append((fileName, year, pathology))
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        fileName, year, pathology = self.data[idx]
        img_path = os.path.join(self.path, fileName)
        img = Image.open(img_path).convert("RGB")
        
        if self.transform is not None:
            img = self.transform(img)
        metadata = {'img_path': img_path, "pathologies": pathology}
        return img, year, metadata
            
