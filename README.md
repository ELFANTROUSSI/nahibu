# nahibu
### Installation
On commence par clonner le dépôt dans le dossier du wordpress:
```sh
$ cd wordpress
$ git clone https://github.com/ELFANTROUSSI/nahibu.git
```

On installe Django : 
```sh
$ pip install django
```
On ajoute le nom de domaine qu'on va utiliser dans le fichier settings.py
```sh
ALLOWED_HOSTS = []
```

On lance le serveur sur le port 8080 ou un autre port disponible :
```sh
$ cd nahibu
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8080
```









