import torch
#model = torch.hub.load('.', 'custom', pth='model_test/weights/best.pt', source='local')
model = torch.hub.load(repo_or_dir='model_test/weights/',model='best.pt', source='local')  
print(model)
"""
# Image
img = '1.jpg'
# Inference
results = model(img)
# Results, change the flowing to: results.show()
results.show()  # or .show(), .save(), .crop(), .pandas(), etcimport torch


torch.hub.load()
"""