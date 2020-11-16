## GET /rooms/
Obtener todas las salas de chat de la base de datos.

### Headers
``` json
{
  HTTP_AUTHORIZATION: "Token"
}
```

### Response
Success 200
``` json
[
  {
    id: 1,
    name: "Primera sala"
  },
  {
    id: 2,
    name: "Segunda sala"
  },
  ...
]
```

## GET /messages/
Obtener todos los mensajes de la base de datos.

### Headers
``` json
{
  HTTP_AUTHORIZATION: "Token"
}
```

### Response
Success 200
``` json
[
  {
    id: 1,
    text: "Primer mensaje de la primera sala",
    date: "2020-11-09",
    nickname: "someuser",
    room_id: 1
  },
  {
    id: 2,
    text: "Segundo mensaje de la primera sala",
    date: "2020-11-09",
    nickname: "anotheruser",
    room_id: 1
  },
  {
    id: 3,
    text: "Primer mensaje de la segunda sala",
    date: "2020-11-09",
    nickname: "anotheruser",
    room_id: 2
  },
  {
    id: 4,
    text: "Segundo mensaje de la segunda sala",
    date: "2020-11-09",
    nickname: "someuser",
    room_id: 2
  },
  ...
]
```

## POST /create_user/
Crear un nuevo usuario. Recibe nickname y email. El nickname se usa como atributo para el modelo de usuario, y el email para enviar un correo al usuario.

### Headers
``` json
{
  HTTP_AUTHORIZATION: "Token"
}
```

### Body
``` json
{
  nickname: "myusernickname",
  email: "some@mail.com"
}
```

### Response
```json
{
  success: True
}
```

## POST /create_room/
Crear una sala nueva. Recibe name, con el nombre de la sala que se quiere crear.

### Headers
``` json
{
  HTTP_AUTHORIZATION: "Token"
}
```

### Body
``` json
{
  name: "Some room name"
}
```

### Response
```json
{
  success: True
}
```

## GET /
Health check, para revisar si el servidor está corriendo y recibiendo requests de manera correcta. No recibe ningún parámetro ni es necesario agregar ningún header.

### Response
```json
{
  success: True
}
```