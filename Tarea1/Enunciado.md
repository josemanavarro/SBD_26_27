# Tarea evaluable 1

En esta primera tarea, quiero que despleguemos una pila MING en Docker (Mosquitto, Node-RED, InfluxDB, y Grafana) para captar el clima de Almería desde alguna API pública, por ejemplo [open-meteo.com](https://open-meteo.com). Un mínimo es tener valores de temperatura, presión y humedad, aunque podéis emplear los datos que os resulten más útiles. Con esos datos vamos a construir un cuadro de mando en Grafana que tenga, al menos, los siguientes elementos:

* Temperatura, humedad y presión actual (panel tipo Gauge o similar para cada uno).  
* Gráfica de la última hora de los 3 valores (serie temporal).  
* Texto / métrica con la tendencia de las últimas 24 h (subida/bajada y %).

**Los objetivos de aprendizaje son:**

* Comprender el funcionamiento de una arquitectura Lambda.  
* Desplegar un stack de observabilidad/IoT ligero (MING) con Docker.  
* Diseñar un flujo de ingesta con Node-RED consumiendo de una API REST.  
* Modelar y persistir datos de series temporales en InfluxDB (mediciones, campos, tags).  
* Construir un dashboard en Grafana con paneles KPI y series temporales.  
* Aplicar buenas prácticas (parametrización, manejo de errores, documentación).

**Requisitos funcionales**

1. Despliegue en Docker Compose con red interna y volúmenes persistentes para MQTT, InfluxDB y Grafana.  
2. Ingesta cada 5 minutos desde un script (Script → API → MQTT → Node-RED → Influx → Grafana).  
3. Esquema en InfluxDB:  
   1. measurement: almeria\_clima  
   2. tags: symbol="Tª", “P”, “H”, source="open-meteo"  
   3. fields: valor (float), cambio\_24h (float, opcional), ts\_api (timestamp opcional)  
   4. InfluxDB v2: org, bucket y token gestionados por variables de entorno/secrets.  
4. Cálculo de tendencia 24 h, con una de estas opciones (a elegir):  
   1. Calcular en Grafana: panel Stat que compare el valor actual con el valor de hace 24 h y muestre Δ% (override/transform).  
   2. Calcular en Node-RED y almacenar el %\_cambio\_24h como field adicional (si usáis el endpoint que ya devuelve cambio 24 h, basta con mapearlo).  
5. Dashboard en Grafana con, al menos:  
   1. Panel Valores actuales.  
   2. Panel Gráfica última hora (intervalo fijo 1h, auto-refresh razonable).  
   3. Panel Tendencia 24 h: texto/indicador con flecha ↑/↓ y porcentaje.

**Robustez mínima:**

* Reintento en caso de fallo (HTTP ≠ 200\) y log del error en Node-RED.  
* Respeto por la cadencia (5 minutos) sin ráfagas innecesarias.  
* Script con tratamiento de errores.

**Documentación:**

* README.md con cómo levantar el stack, variables usadas, endpoints y usuario/contraseña por defecto (si los hay), y capturas del dashboard.  
* Documento con:   
  * Explicación general de la implementación.  
  * Capturas que muestren el funcionamiento de la pila.  
  * Diagrama del flujo Node-RED.  
  * Justificación del esquema Influx.  
  * Justificación de decisiones tomadas para el dashboard y capturas del mismo.

**Entrega:**

* Repositorio (o carpeta) con:   
  * docker-compose.yml  
  * Flows de Node-RED (flows.json)  
  * Ficheros .env/secrets (sin credenciales sensibles reales)  
  * README.md  
* PDF con el documento.

**Valoración (10 puntos)**

* Infraestructura Docker (Compose, redes, volúmenes, parametrización) – 2 pts  
* Script de captación – 1pto  
* Flujo Node-RED – 2 pts  
* Modelo de datos en InfluxDB y consultas – 2 pts  
* Dashboard Grafana – 2 pts  
* Documentación y entregables – 1 pto  
* Extra (hasta \+1 pto):  
  * Alertas en Grafana por umbral de variación (\>±10 % en 1 h).  
  * Variables de entorno y .env bien estructurado \+ secrets Docker.