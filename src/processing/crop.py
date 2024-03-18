from cv2 import resize,fillPoly,bitwise_and
from typing import Tuple,List
from numpy import ndarray,uint8,int32,zeros,array
from ultralytics import YOLO

import numpy as np
import torch
import torchvision
from numpy import ndarray
from typing import Union

def GetModel(filePath:str = r"models\best.pt") -> YOLO | None:
    """
    Recebe o caminho de um modelo YOLO e o retorna
    Caso falhe ao encontrar o modelo retorna None
    
    Args:
        filepath::str: Caminho para o arquivo .pt
        
    Return:
        Model:: Yolo | None: Retorna o modelo carrega ou None em caso de falha
        
    """
    
    try:
        model = YOLO(filePath)
    except:
        model = None
        
    return model

def ResizeList(images:List[ndarray], size:Tuple[int,int] = (640,640))-> List[ndarray]:
    """
    Redimensiona uma lista de imagens para a proporção desejada
    
    Args:
        images::List[ndarray]: Lista de imagens no formato ndarray a serem redimensionadas
        size::Tuple[int,int]: Tupla contendo 2 valores usadaos para definir as novas dimensões, sendo eles respectivamente largura e altura
        
    Return:
        resized::List[ndarray]: Lista contendo as imagens redimensionadas
    """
    
    resized = []
    
    for imagem in images:
        resized.append(resize(imagem, size))
        
    return resized

def Predict_image(image:str,modelsPath:str="best.pt",conf:float=0.5):
        """
        Processa uma imagem e retorna um dicionário com os dados obtidos.
        O dicionário possui as seguintes chaves -> xyxys,confidences,class_id,masks,probs
        
        Args:
            image::str: Nome de uma imagem processada para o recorte
            modelsPath::str: Caminho para o modelo YOLO salvado no formato .pt para segmentação
            confiance::float: Grau de confiança que a rede usará para decidir as zonas de recorte,
            o valor de confiança pode varia entre 0 e 1.
            
        Retorno:
            dic::dict: Dicionário Contendos os dados obtidos no processamento
        """
        
        dic = dict()
        
        try:
            model = YOLO(modelsPath)
            results = model.predict(image,conf=conf,boxes=False,max_det=1)

            result = results[0]
            boxes = result.boxes.cpu().numpy()
        
            dic['xyxys'] = boxes.xyxy
            dic['confidences'] = boxes.conf
            #dic['masks'] = (result.masks.xy,result.masks.data)
            dic['masks'] = result.masks.xy
            
        except:
            dic = None
        
        return dic


def Segment(image: ndarray, model: YOLO, conf: float = 0.5) -> Union[ndarray, None]:
    """
    Recebe uma imagem famacha, a segmenta e retorna a zona de interesse coletada após a segmentação.
    
    Args:
        image::ndarray: Imagem que será segmentada
        model::YOLO: Modelo YOLO treinado para realizar a segmentação
        conf::float: Confiança da box durante a detecção
 
    Return:
        segmentacao::ndarray: Imagem segmentada a ser retornada ou Nada caso não haja o que segmentar na imagem
    """
    # Realiza a predição do modelo na imagem
    results = model.predict(source=image, boxes=False, conf=conf, max_det=1)
    
    segmentacao = None
    
    # Verifica se houve detecções
    if results is not None and len(results) > 0:
        # Obtém o primeiro resultado
        result = results[0]
        
        # Verifica se há máscaras
        if result.masks is not None and len(result.masks) > 0:
            
            # Obtém as coordenadas das máscaras
            xy = result.masks.xy
            
            # Converter as coordenadas das máscaras para um único numpy.ndarray
            xy_np = np.array(xy, dtype=np.float32)

            # Calcular as caixas delimitadoras a partir das coordenadas das máscaras
            xmin = np.min(xy_np[:, :, 0], axis=1)
            ymin = np.min(xy_np[:, :, 1], axis=1)
            xmax = np.max(xy_np[:, :, 0], axis=1)
            ymax = np.max(xy_np[:, :, 1], axis=1)

            # Criar as caixas delimitadoras no formato [xmin, ymin, xmax, ymax]
            boxes = torch.tensor(np.stack([xmin, ymin, xmax, ymax], axis=1), dtype=torch.float32)

            # Ajustar o tamanho do tensor de pontuações (scores) para corresponder ao número de caixas detectadas
            scores = torch.zeros(boxes.shape[0], dtype=torch.float32)

            # Aplicar a supressão não máxima (NMS)
            indices = torchvision.ops.nms(boxes, scores, iou_threshold=conf)

            # Verificar se os índices estão dentro do alcance válido de xy antes de acessá-los
            filtered_xy = [xy[i] for i in indices if i < len(xy)]

            mask = np.zeros(image.shape[:2], dtype=np.uint8)

            # Converter a lista de tuplas em um array numpy
            pts = np.array([tuple(map(int, ponto)) for array in filtered_xy for ponto in array], dtype=np.int32)

            # Desenhar a região de interesse na máscara (casso erro trocar 1 por 255)
            fillPoly(mask, [pts], (255))  # Preenche a região da máscara com branco

            # Aplicar a máscara na imagem original
            segmentacao = bitwise_and(image, image, mask=mask)
            
        
    # Retorna None caso não haja detecções ou máscaras presentes na imagem
    return segmentacao
    """
def Segment(image:ndarray,model: YOLO):
    """
    """
    Recebe uma imagem famacha, a segmenta e retorna a zona de interesse coletada após a segmentação.
    
    Args:
        image::ndarray: Imagem que será segmentada
        model::YOLO: Modelo YOLO treinado para realiazar a segmentação
 
    Return:
        segmentacao::ndarray: Imagem segmentada a ser retornada ou Nada caso não haja oq segementar na imagem
    """
    """
    #try:
    results = model.predict(source=image,boxes=False,conf=0.3,max_det=1)

    result = results[0]
    xy = result.masks.xy

    mask = zeros(image.shape[:2], dtype=uint8)

    # Converter a lista de tuplas em um array numpy
    pts = array([tuple(map(int, ponto)) for array in xy for ponto in array], dtype=int32)

    # Desenhar a região de interesse na máscara
    fillPoly(mask, [pts], (255))  # Preenche a região da máscara com branco

    # Aplicar a máscara na imagem original
    segmentacao = bitwise_and(image, image, mask=mask)
        
    #except:
        #segmentacao = None
    
    return segmentacao

    """

def SegmentedList(images:List[ndarray], model:YOLO, is_resized: bool = False, conf: float = 0.5)->List[ndarray]:
    """
    Recebe uma lista de imagens e realizada a segmentação em cada uma das imagens.
    Caso a imagem seja uma imagem válida, retorna a zona de interesse obtida pela segmentação.
    Caso não seja, retorna um valor Nulo para aquela imagem
    
    Args:
        images::List[ndarray]: Lista de imagens a serem segmentadas
        model::YOLO: Modelo YOLO treinado para realizar a segmentação
        is_resized::bool: Caso as imagens já estejam redimensionadas para a proporção ideal passe True
        
    Return:
        segmented::List[ndarray | None]: Lista com as imagens ou None caso a imagem não tenha a zona de interesse
         
    """
    if is_resized == False:
        images = ResizeList(images)
    
    segmented = []
    
    for image in images:
        segmented.append(Segment(image,model,conf))
        
    return segmented

if __name__ == "__main__":
    from cv2 import imread, imwrite
    
    image = imread(r"Dados\dados\img3_1.jpg")
    model = YOLO("best.pt")

    result = Segment(image,model)
    print(result)
    imwrite(r"test\segmentado.jpg",result)