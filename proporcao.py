from src import (
    Folder,
    GetModel,
    SegmentedList,
    segmentation_fails
    )

from os.path import join
DATA = "Dados"
MODEL = "Models"


#adquindo as imagens e seus respectivos rotulos
dataBasePath = join(DATA,"dados")
images, labels = Folder(dataBasePath)

segmentation_model = GetModel(join("models","best.pt"))

items = [(640,640), (512,512), (256,256), (128,128), (64,64)]

results = []

for item in items:
    process_images = SegmentedList(images,segmentation_model,is_resized=False, new_size=item) # Por padrão redimensionar garante menor taxa de falha
    fails = segmentation_fails(process_images,labels)

    results.append((item,fails))
    

for item, fails in results:

    print(f"Proporção:{item}\nFalhas:",len(fails))