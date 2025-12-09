# Sistema de Detección de Botellas Usando YOLOv5
1. Instalar Python  
Descargar desde https://www.python.org/downloads/  
Durante la instalación marcar la opción “Add Python to PATH”.  
  
2. Descargar YOLOv5  
Puedes clonar el repositorio con: "git clone https://github.com/ultralytics/yolov5"  
Luego entrar a la carpeta: "cd yolov5"  
  
3. Instalar las dependencias  
Ejecutar: "pip install -r requirements.txt"  
Es importante asegurar que OpenCV tenga soporte para ventanas.
Ejecutar: "pip uninstall opencv-python-headless -y"  
"pip install opencv-python==4.7.0.72"  
  
4. Copiar el modelo entrenado  
Colocar el archivo best.pt dentro de la carpeta principal de YOLOv5, donde está detect.py.  
La estructura debe quedar así:  
yolov5/  
detect.py  
best.pt  
data/  
models/  
utils/  
  
5. Ejecutar detección  
  
A) Para usar la cámara:  
python detect.py --weights best.pt --source 0  
  
Si la cámara principal no se abre, probar con:  
--source 1  
--source 2  
  
B) Para detectar en una imagen:  
python detect.py --weights best.pt --source ruta/de/imagen.jpg  
  
C) Para detectar en una carpeta:  
python detect.py --weights best.pt --source images/  
  
Ver resultados  
Los resultados se guardan automáticamente en:  
runs/detect/exp/  
Cada nueva ejecución crea exp2, exp3, etc.  
