##### Español:
### Portal Blog
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20215641.png?raw=true" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Portal Blog</div>  
  #### Descripcion.
  
> Portal blog con alternativas para noticias, actualidad, creacion de cuenta de usuarios, apartado de ventas para exponer productos por categoria con precios donde los usuarios pueden escoger y guardar favoritos, apartado para postear servicios prestados por la empresa. 

#### Características
- Registro de suarios.
- Registro de productos.
- Registro de servicios.
- Blog.
- Noticias.
- Agregar productos a favoritos.
- BitMap del sitio para el posicionamiento SEO.
- Panel administrativo.
- Cuenta de administrador.

#### Instalación

##### Crear entorno virtual:
```
python -m venv blog
```

##### Entrar en el entorno
```
cd blog
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd blog/Script
```
```
activate
```
> en Lunix:
```
source blog/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/blog.git
```

> Navegar al directorio del proyecto:

```
cd blog
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Portal Blog
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20215641.png?raw=true" align="center" style="width: 100%" />
</div>  
<div align="center">Portal Blog/div>

 ### Description
 
 > Blog portal with options for news, current events, user account creation, a sales section to display products by category with prices where users can choose and save favorites, and a section to post services provided by the company.

#### Features

- User registration.
- Product registration.
- Service registration.
- Blog.
- News section.
- Add products to favorites.
- Site map for SEO positioning.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv blog
```

#### Enter the environment
```
cd blog
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd blog/Scripts
```
```
activate
```
> Linux:
```
source blog/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/blog.git
```

> Navigate to the project directory:

```
cd blog
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
