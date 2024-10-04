# topicos-ia-2024-1er-parcial


## instrucciones

### Completar implementacion del detector

#### match gun bbox

Esta función servirá para realizar el match entre un segmento y un arma cercana. El objetivo de esta función es de encontrar el arma más cercana a un segmento dado en base a un umbral de distancia máxima.

La función deberá retornar el bounding box del arma más cercana a un segmento siempre y cuando la distancia entre el segmento correspondiente a una persona y el bounding box del arma sea menor a una distancia máxima de acercamiento. Si el bounding box más cercano es mayor a la distancia máxima, la función deberá retornar None.

#### segment people

Usted deberá implementar el método GunDetector.segment_people() el cual tiene la tarea de segmentar personas en la imagen siguiendo las siguientes reglas:

 1. El método deberá retornar un objeto de tipo Segmentation
 2. Los segmentos a retornar deberán corresponder solamente con segmentos de personas.
 3. Existen 2 etiquetas posibles para los segmentos de personas: 'safe' y 'danger'.
 4. La etiqueta 'safe' o 'danger' deberá ser asignada de acuerdo a la proximidad del segmento con un arma previamente detectada.
 5. Todos aquellos segmentos que estén cerca a un arma (pistola o rifle) serán etiquetados como 'danger', aquellos segmentos que estén alejados, 'safe'.


 
#### annotate segmentation
La funci'on annotate_segmentation deberá realizar anotaciones sobre la imagen origen en base a las predicciones de segmentación siguiendo las siguientes reglas:

 1. Todos los segmentos de personas en la categoria 'danger' deberán ser anotados con un tinte rojo.
 2. Todos los segmentos de personas en la categoria 'safe' deberán ser anotados con un tinte verde.
 3. Existe un parámetro opcional llamado draw_boxes, si el valor del parámetro es True, deberá dibujar además los bounding boxes y etiquetas del sgmento correspondiente.

Ejemplos:

![alt text](sample_out1.jpg)

![alt text](sample_out2.jpg)

![alt text](sample_out3.jpg)

### Implementar endpoints

Una vez completadas las anteriores tareas, usted deberá implementar los siguientes endpoints en la aplicación de FastAPI:

#### POST: /detect_people
Este endpoint deberá devolver un objeto de tipo Segmentation correspondiente a la predicción de la segmentación de personas en las categorias 'safe' y 'danger'.

#### POST: /annotate_people
Este endpoint deberá retornar una imagen con la anotación de la segmentacion, agregue un parámetro opcional para decidir si se debe anotar también los bounding boxes.

#### POST: /detect
Este endpoint deberá combinar ambos tipos de predicciones Detection y Segmentation en un solo response. Es decir, para una imagen deberá retornar ambos, la detección de las armas y la segmentación de las personas.

#### POST: /annotate
Este endpoint, deberá combinar las anotaciones tanto de la detección de armas como la de la segmentación en una sola imagen resultado.

#### POST: /guns
Este endpoint deberá devolver una lista de objetos de tipo Gun con la información del tipo de arma y ubicación de la misma en la imagen (en pixeles). La ubicación deberá corresponder con el centro del bounding box de detección. Este objeto está declarado como Gun en el archivo src.models


### POST: /people
Este endpoint deberá devolver una lista de objetos de tipo Person con la información de la categoría de la persona, ubicación y área en pixeles ocupada por el segmento. La ubicación corresponde con el centro del segmento. El objeto está declarado como Person en el archivo src.models