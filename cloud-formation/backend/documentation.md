## Servicios que se levantan

- Load Balancer
- Target Group
- Load Balancer Listeners
- Auto Scaling Group

## Servicios que deben estar levantados en AWS

- Certificate Manager
- Launch Template

## Cómo funciona?

- Se crea un Application Load Balancer, con security group default, y todas las subnets de us-east-1.
- Se crea un target group, con las mismas properties de health checks, puertos, protocolos y VPC que el target group deployado actualmente en AWS.
- Se crean dos listeners para el Load Balancer, uno http y el otro https. Ambos están asociados al Load Balancer creado anteriormente. 
- El listener http escucha en el puerto 80 y su default action redirige al puerto 443. 
- El listener https escucha en el mismo puerto 443 y su default action reenvía la solicitud al target group creado anteriormente. 
- El listener https tiene asociado el certificado SSL creado con Certificate Manager que se usa actualmente en el deploy en AWS. También cuenta con la misma configuración de SslPolicy que el listener deployado actualmente.
- Por último, se crea el Auto Scaling Group. Cuenta con las mismas configuraciones de de zonas, VPC y cantidad de instancias que el que está deployado actualmente.
- El Auto Scaling Group está asociado al Target Group creado anteriormente.
- El Auto Scaling Group utiliza el Launch Template que se encuentra deployado en AWS.

## Espacio de Mejora

- Se podría implementar el Launch Template (junto con la creación de la imagen de la instancia EC2) directamente en el template de CloudFormation.
- Se podría aprovechar el template para crear ambientes de Staging y Producción, cambiando solamente los nombres asociados a los servicios. También sería necesario tener un Launch Template distinto, con la imagen de Staging.
- Falta integrar Route 53 en el template.