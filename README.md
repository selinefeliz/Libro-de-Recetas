1. Descripción del Programa
   
El programa será un libro de recetas personal que permitirá al usuario almacenar, consultar, editar y 
eliminar recetas. Cada receta incluirá información sobre su nombre, nivel de complejidad, número de 
pasos, detalles de cada paso y tiempo total de preparación (con la posibilidad de dividir el tiempo 
entre pasos). El programa contará con una interfaz gráfica amigable para facilitar la interacción del 
usuario, y los datos serán gestionados mediante una base de datos. 
3. Requerimientos Funcionales 
Funcionalidades Principales: 
1. Insertar Recetas - Permitir al usuario agregar una nueva receta con los siguientes datos: - Nombre de la receta. - Complejidad (baja, media, alta). - Número de pasos. - Detalles de cada paso (descripción de las acciones a realizar en cada paso). - Tiempo total de preparación (dividido entre los pasos). 
2. Mostrar Recetas en Orden de Complejidad - Mostrar una lista de todas las recetas ordenadas por su nivel de complejidad (baja, media, alta). - Mostrar la receta con su nombre y tiempo de preparación total. 
3. Mostrar Detalles de una Receta - Permitir al usuario seleccionar una receta y ver sus detalles completos: - Nombre de la receta. - Complejidad. - Número de pasos. - Descripción de los pasos (incluyendo el tiempo asignado a cada uno). - Tiempo total de preparación. 
4. Eliminar una Receta - Permitir al usuario seleccionar una receta de la lista y eliminarla del sistema. 
5. Salir del Programa 
   - Permitir al usuario cerrar la aplicación de manera controlada. 
 
 3. Especificaciones Técnicas 
 
 1. Lenguaje de Programación: Python 
   - Uso de Python para la lógica del programa, manejo de base de datos y conexión con la interfaz 
gráfica. 
 
 2. Base de Datos: SQLite 
   - Utilización de SQLite (o una alternativa simple) para almacenar los datos de las recetas: 
     - Tabla Recetas con los campos: 
       - id (clave primaria). 
       - nombre (texto). 
       - complejidad (entero/cadena). 
       - tiempo_total (número, minutos). 
       - num_pasos (número). 
 
     - Tabla Pasos: 
       - id (clave primaria). 
       - id_receta (clave foránea que relaciona la receta con sus pasos). 
       - detalle_paso (texto). 
       - tiempo_paso (número, minutos). 
 
 3. Interfaz Gráfica: CustomTkinter / Tkinter 
   - Uso de la librería CustomTkinter / Tkinter para crear la interfaz gráfica. Algunos elementos que 
incluirá son: 
     - Formulario de ingreso: Para añadir o editar recetas. 
     - Lista de recetas: Mostrar las recetas ordenadas por complejidad. 
     - Vista de detalles: Mostrar los pasos detallados de una receta. 
     - Botones de acción: Para agregar, eliminar, y salir del programa. 
 
4. Flujo General del Programa 
1. Pantalla Principal:  - Menú con opciones para: - Insertar nueva receta. - Mostrar todas las recetas (ordenadas por complejidad). - Eliminar una receta. - Salir del programa. 
2. Insertar Receta: - Formulario para ingresar el nombre de la receta, su complejidad, tiempo total de preparación y 
los pasos detallados. - Cada paso incluirá una descripción y su tiempo correspondiente. 
3. Mostrar Recetas: - Lista con todas las recetas, ordenadas por nivel de complejidad. Al hacer clic en una receta, se 
mostrará una vista detallada con todos los pasos y tiempos. 
4. Eliminar Receta: - Opción para seleccionar una receta y eliminarla de la base de datos. 
5. Salir del Programa: - El botón de "Salir" permitirá cerrar la aplicación de manera segura, guardando los cambios en la 
base de datos. 
5. Consideraciones Adicionales - Validación de Datos:  - Comprobar que el usuario introduzca valores válidos, como tiempos y número de pasos. - Sistema de Confirmaciones:  - Antes de eliminar una receta, se solicitará confirmación al usuario. - Persistencia de Datos:  
- Asegurar que las recetas agregadas, modificadas o eliminadas se mantengan guardadas en la base 
de datos. 
6. Tecnologías y Herramientas a Utilizar - Python 3.x: Lenguaje principal. - Tkinter: Para la interfaz gráfica. - CustomTkinter: Para la interfaz gráfica - SQLite: Para la gestión de la base de datos. - SQLAlchemy (opcional): Para gestionar la base de datos de forma más eficiente si se requiere. 
