# Yolov11-Classifier
Este repositorio implementa un modelo de clasificación de imágenes basado en YOLO-11n, la versión más pequeña del modelo. Aunque YOLO es tradicionalmente utilizado para detección de objetos, aquí se adapta para tareas de clasificación pura.

## Descripción del modelo

El modelo parte de la arquitectura YOLO-11 como extractor de características, reemplazando la parte final de detección por una cabeza clasificadora totalmente conectada. De esta forma, aprovechamos la potencia de YOLO como backbone para tareas de clasificación de imágenes multiclase.

## Estructura del Dataset

El dataset debe estar organizado en tres carpetas principales: `train`, `val` y `test`. Cada una de estas carpetas contiene subcarpetas que representan las clases del modelo. Las clases son las siguientes:

- Bean  
- Bitter_Gourd  
- Bottle_Gourd  
- Brinjal  
- Broccoli  
- Cabbage  
- Capsicum  
- Carrot  
- Cauliflower  
- Cucumber  
- Papaya  
- Potato  
- Pumpkin  
- Radish  
- Tomato  


## Resultados

![confusion_matrix](https://github.com/user-attachments/assets/83c47a70-cf36-4562-aec8-035ce7e4484f)
![results](https://github.com/user-attachments/assets/d862db41-8baa-423e-bd07-de0162171967)


## Requisitos

- Python 3.8+
- PyTorch
- scikit-learn
- matplotlib
- numpy
- OpenCV
- ultralytics (si se usa la versión oficial de YOLO-11)

Instalación recomendada:

```bash
pip install -r requirements.txt
