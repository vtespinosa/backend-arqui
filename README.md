# Consideraciones Generales

* Se están utilizando dos repositorios, este para el backend y https://github.com/iic2173/iic2173-proyecto-semestral-grupo10-frontend para el frontend.
* Las credenciales de acceso a la instancia EC2 se encuentran en la entrega de canvas

#  Método de acceso al servidor con archivo *.pem* y *ssh*

Se debe ejecutar el siguiente comando con la terminal abierta en la misma carpeta donde se encuentra el archivo .pem:\
```ssh -i "entrega1.pem" ubuntu@backend.we-chat.ml```


# Logrado y no logrado

## Parte mínima

### Autenticación

* **RF1:** Logrado
* **RF2:** Logrado
* **RF3:** Logardo

### CI/CD

* **RF1:** Se implementó el sistema de integración y despliegue continuo, pero no funciona porque Travis lanza el siguiente error "Builds have been temporarily disabled for private repositories due to a negative credit balance". De todas maneras se documenta lo realizado:
1. Cada vez que se hace un pull request a master se hace un build, se corren los tests, se incluyen los archivos start.sh, stop.sh e install.sh para su uso futuro, y se comprime el proyecto en una carpeta comprimida llamada latest.zip
2. Solamente si pasaron los tests y no hubo un error en el paso anterior se sigue con los siguiente pasos. En primer lugar, se crea una imagen de docker y se sube a ECR.
3. Se sube la carpeta comprimida con el código a un bucket s3
4. Una vez que latest.zip es subida a s3, CodeDeploy se encarga de agregarla a la instancia EC2.
5. Una vez que latest.zip está en Ec2, se siguen los pasos de appspec.yml, que consisten en extraer el proyecto de la carpeta comprimida, parar la versión anterior, realizar el build y correr la nueva versión.
* **RF2:** Logrado, se utiliza Travis en conjunto con CodeDeploy
* **RF3:** Logrado, se hacen tests de request cada vez que se hace un pull request a master, y si fallan, se termina el proceso con status 1.
* **RF4:** Se manejan las variables de entorno en Travis.

### Documentación
* **RF1:** Logrado, se encuentra en la carpeta Documentación
* **RF2:** Logrado, se encuentra en la carpeta Documentación
* **RF3:** Logrado, se encuentra en la carpeta Documentación
* **RF4:** Logrado, se encuentra en la carpeta Documentación

## Parte Variable:

### CRUD Admin:

* **RF1:**
* **RF2:**
* **RF3:**

### CSS/Javascript Injection:

* **RF1:**
* **RF2:**
* **RF3:**

### Encriptación:

* **RF1:**
* **RF2:**
* **RF3:**
