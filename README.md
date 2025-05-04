# 🕹️ Gamershop - Proyecto Web

**Aplicación web creada para la asignatura _Programación Web (PGY3221)_**

---

### 📌 Descripción del Proyecto

**Gamershop** es una aplicación web tipo foro centrado en videojuegos. Los usuarios pueden registrarse, iniciar sesión y navegar por diferentes categorías de juegos, donde encontrarán información como el título del juego, una breve descripción y su precio en pesos chilenos.

Los usuarios registrados tienen la posibilidad de valorar los juegos con una puntuación del 1 al 5 y dejar comentarios u opiniones sobre ellos.

---

### 🛠️ Tecnologías Utilizadas

- **Frontend:**
  - HTML
  - CSS
  - Bootstrap
  - JavaScript

- **Backend:**
  - Django (Python)
  - Django REST Framework

- **Base de datos:**
  - Oracle

- **Herramientas:**
  - Git y GitHub para trabajo colaborativo
  - Consumo de servicios web externos

---

### 🔒 Funcionalidades del Sistema

- Registro de usuarios y autenticación segura con validaciones de contraseña (longitud mínima, uso de caracteres especiales, números y letras).
- Recuperación de contraseña y modificación de perfil.
- Visualización de juegos por categorías temáticas.
- Valoración de juegos (1 a 5 estrellas).
- Publicación de comentarios por parte de los usuarios.
- Restricción de acceso a páginas internas mediante inicio de sesión.
- Administración de usuarios, juegos, comentarios y secciones del foro.
- Diseño responsive que se adapta a diferentes tamaños de pantalla utilizando un sistema de grilla de 12 columnas.

---

### 🔗 API REST

#### Endpoints Propios

- **API Juegos:** Devuelve un listado JSON con todos los juegos registrados.
- **API Comentarios:** Muestra las opiniones y valoraciones realizadas por los usuarios.

#### Ejemplo de consumo:

```js
fetch("https://tudominio/api/juegos/")
  .then(res => res.json())
  .then(data => console.log(data));
```

> Puedes hacer peticiones GET desde herramientas como Postman o frameworks frontend como React o Vue.

---

### 📁 Estructura del Proyecto

- `gamershop_app/`: Lógica principal de la aplicación (modelos, vistas, APIs, etc.)
- `oracle_wallet/`: Configuración de conexión con Oracle
- `ui/`: Archivos visuales (fondos, estilos)
- `db.sqlite3`: Base de datos de prueba local
- `manage.py`: Ejecutable principal de Django
- `.gitignore`: Archivos y carpetas excluidos del control de versiones

---

### 👥 Roles de Usuario

- **Usuario común:** Puede explorar juegos, valorarlos y dejar comentarios.
- **Administrador:** Acceso completo al sistema, incluyendo gestión de usuarios, juegos y comentarios.

---

### 👨‍💻 Desarrolladores

- Fabrizio Bugedo
- Benjamín Araneda 
- Nicolas Soto
