Deploy King Tide

Este repositorio contiene los scripts y configuraciones necesarias para el despliegue de la aplicación King Tide.

Contenido

	•	Archivos docker-compose para entornos de desarrollo y producción.
	•	Scripts para la actualización programada de eventos deportivos.
	•	Configuración de CI/CD.

Requisitos

	•	Docker
	•	Docker Compose

Uso

Entorno de desarrollo

	1.	Inicia los contenedores con:
docker-compose -f docker-compose.dev.yml up –build
	2.	La aplicación estará disponible en:
	•	Frontend: http://localhost:5173
	•	Backend: http://localhost:8000
	•	API Clima: http://localhost:3000

Entorno de producción

	1.	Actualiza el archivo docker-compose.prod.yml con tus configuraciones.
	2.	Inicia los contenedores con:
docker-compose -f docker-compose.prod.yml up –build -d
	3.	La aplicación estará disponible en tu dominio configurado.

CI/CD

Flujo en GitHub Actions

	1.	Los workflows en .github/workflows automatizan la construcción y despliegue de imágenes Docker en cada commit a la rama main.
	2.	Las variables de entorno y secretos para el despliegue deben configurarse en la sección Secrets de GitHub.

Scheduler para actualización de eventos

El script update_events_scheduler.py ejecuta actualizaciones cada 2 horas.

Configuración del Scheduler

	1.	Construir la imagen Docker:
docker build -t usuario/update_events_scheduler:latest .
	2.	Ejecutar el contenedor:
docker run usuario/update_events_scheduler:latest

Licencia

Este proyecto está bajo la licencia MIT.
