# 2024-dj5-dream-blog
Membangung Aplikasi Blog from Zero to Deployment menggunakan Django versi 5


## 1. SETUP


#### 1. Modifikasi file .gitignore dan README.md


        modified:   .gitignore
        modified:   README.md


## 2. PROYEK DJANGO


#### 1. Membuat proyek django

        modified:   README.md
        new file:   dreamblog/__init__.py
        new file:   dreamblog/asgi.py
        new file:   dreamblog/settings.py
        new file:   dreamblog/urls.py
        new file:   dreamblog/wsgi.py
        new file:   manage.py


#### 2. Menjalankan lokal server
        
        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ ls
        dreamblog/  manage.py*  README.md

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        February 21, 2024 - 10:13:56
        Django version 5.0.2, using settings 'dreamblog.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 3. Default page

        Django version 5.0.2, using settings 'dreamblog.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


## 3. APP DJANGO


#### 1. Membuat direktori apps untuk semua aplikasi django

        modified:   README.md
        (dreamblog) λ mkdir apps


#### 2. Membuat aplikasi django di dalam apps dengan nama blog

        (dreamblog) λ mkdir apps\blog

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ ls
        apps/  db.sqlite3  dreamblog/  manage.py*  README.md

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py startapp blog apps\blog

        modified:   README.md
        new file:   apps/blog/__init__.py
        new file:   apps/blog/admin.py
        new file:   apps/blog/apps.py
        new file:   apps/blog/migrations/__init__.py
        new file:   apps/blog/models.py
        new file:   apps/blog/tests.py
        new file:   apps/blog/views.py


#### 3. Register aplikasi blog pada dreamblog

        modified:   README.md
        modified:   apps/blog/apps.py
        modified:   dreamblog/settings.py

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ ls
        apps/  db.sqlite3  dreamblog/  manage.py*  README.md

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py check
        System check identified no issues (0 silenced).


## 4. HALLO WORLD


#### 1. HttpResponse dengan Hallo World!

        modified:   README.md
        new file:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   dreamblog/urls.py


## 5. TEMPLATES, VIEWS, DAN URLS


#### 1. Membuat home page

        modified:   README.md
        new file:   apps/blog/templates/blog/index.html
        modified:   apps/blog/views.py


#### 2. Membuat contact page

        modified:   README.md
        new file:   apps/blog/templates/blog/contact.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


## 6. NAVIGASI 

#### 1. Membuat navigasi dan mentautkan home dan contact pages

        modified:   README.md
        modified:   apps/blog/templates/blog/contact.html
        modified:   apps/blog/templates/blog/index.html


## 7. TEMPLATING, STATIC AND MEDIA FILE


#### 1. Menambahkan html template pada home page

        modified:   README.md
        modified:   apps/blog/templates/blog/index.html