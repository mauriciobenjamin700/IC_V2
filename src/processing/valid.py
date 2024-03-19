from typing import List,Tuple
from numpy import ndarray
def segmentation_fails(process_images: ndarray, labels: List[str])->List[str]:
    """
    Devolve o rotulo de todas as imagens que falharam na detecção
    """
    fails = []

    # Iterando de trás para frente
    for i in reversed(range(len(process_images))):
        if process_images[i] is None:
            fails.append(labels[i])

    return fails


def images_labels(fails:List[str],process_images: ndarray, labels: List[str])->Tuple[List[ndarray],List[str]]:
    """
    Devolve as imagens e rotulos validos com base nos nomes das imagens que falharam
    """
    valid_images = []
    valid_labels = []

    for i in range(0,len(process_images),1):
        if labels[i] not in fails:
            valid_images.append(process_images[i])
            valid_labels.append(labels[i])
            
    
    return valid_images, valid_labels