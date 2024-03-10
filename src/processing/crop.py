from cv2 import resize,fillPoly,bitwise_and
from typing import Tuple,List
from numpy import ndarray,uint8,int32,zeros,array
from ultralytics import YOLO

def imageList(images:List[ndarray], size:Tuple[int,int] = (640,640))-> List[ndarray]:
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

def predict_image(image:str,modelsPath:str="best.pt",conf:float=0.5):
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
            results = model.predict(image,conf=conf,boxes=False,max_det=2)

            result = results[0]
            boxes = result.boxes.cpu().numpy()
        
            dic['xyxys'] = boxes.xyxy
            dic['confidences'] = boxes.conf
            #dic['masks'] = (result.masks.xy,result.masks.data)
            dic['masks'] = result.masks.xy
            
        except:
            dic = None
        
        return dic


def segment(image:ndarray,model: YOLO):
    """
    Recebe uma imagem famacha, a segmenta e retorna a zona de interesse coletada após a segmentação.
    
    Parâmetros:
        image::ndarray: Imagem que será segmentada
        
    Retorno:
        segmentacao::ndarray: Imagem segmentada a ser retornada ou Nada caso não haja oq segementar na imagem
    """
    
    
    
    try:
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
        
    except:
        segmentacao = None
    
    return segmentacao

def segmentedList(images:List[ndarray])->List[ndarray]:
    """
    Recebe uma lista de imagens processadas e realizada a segmentação em cada uma das imagens.
    Caso a imagem seja uma imagem válida, retorna a zona de interesse obtida pela segmentação.
    Caso não seja, retorna um valor Nulo para aquela imagem
    
    Args:
        images::List[ndarray]: Lista de imagens a serem segmentadas
        
    Return:
        segmented::List[ndarray | None]: Lista com as imagens ou None caso a imagem não tenha a zona de interesse
         
    """
    segmented = []
    
    for image in images:
        segmented.append(segment(image))
        
    return segmented

if __name__ == "__main__":
    from cv2 import imread, imwrite
    
    image = imread(r"Dados\dados\img3_1.jpg")
    model = YOLO("best.pt")

    result = segment(image,model)
    print(result)
    imwrite(r"test\segmentado.jpg",result)