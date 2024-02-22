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


#### 2. Setup path untuk static dan media file

        modified:   README.md
        modified:   dreamblog/settings.py
        modified:   dreamblog/urls.py


#### 3. Menambahkan static assets pada folder static_in_env

        new file:   static_in_env/assets/css/custom.css
        new file:   static_in_env/assets/css/fontastic.css
        ...
        new file:   static_in_env/assets/vendor/popper.js/umd/popper.min.js
        new file:   static_in_env/assets/vendor/popper.js/umd/poppper.js.flow


#### 4. Loading static dan media files pada home page

        modified:   README.md
        modified:   apps/blog/templates/blog/index.html


#### 5. Membuat laman blog

        modified:   README.md
        new file:   apps/blog/templates/blog/blog.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


#### 6. Loading static dan media files pada blog page

        modified:   README.md
        modified:   apps/blog/templates/blog/blog.html


## 7. TEMPLATE INHERITANCE 


#### 1. Create base template

        modified:   README.md
        new file:   apps/blog/templates/blog/base.html


#### 2. Loading base template in home_view

        modified:   README.md
        modified:   apps/blog/views.py


#### 3. Memindahkan semua isi file index ke base.html

        modified:   README.md
        modified:   apps/blog/templates/blog/base.html
        modified:   apps/blog/templates/blog/index.html


#### 4. Extends base.html template ke index.html

        modified:   README.md
        modified:   apps/blog/templates/blog/index.html
        modified:   apps/blog/views.py


#### 5. Inherate content base.html template ke index.html

        modified:   README.md
        modified:   apps/blog/templates/blog/base.html
        modified:   apps/blog/templates/blog/index.html


## 8. TEMPLATE PARTIALS 


#### 1. Membuat files templates partials

        modified:   README.md
        new file:   apps/blog/templates/blog/partials/_footer.html
        new file:   apps/blog/templates/blog/partials/_head.html
        new file:   apps/blog/templates/blog/partials/_header.html
        new file:   apps/blog/templates/blog/partials/_scripts.html


#### 2. Memindahkan bagian head, header, footer, dan scripts dari base templates ke file partials

        modified:   README.md
        modified:   apps/blog/templates/blog/base.html
        modified:   apps/blog/templates/blog/partials/_footer.html
        modified:   apps/blog/templates/blog/partials/_head.html
        modified:   apps/blog/templates/blog/partials/_header.html
        modified:   apps/blog/templates/blog/partials/_scripts.html

        Note:

        Tampilan home page saat ini tidak sempurna 
        karena tanpa head, header, footer, dan scripts (21_template_partials/02).


#### 3. Include templat partials pada base.html

        modified:   README.md
        modified:   apps/blog/templates/blog/base.html


#### 4. Menggunakan teknik template inheritance dan include pada blog.html

        modified:   README.md
        modified:   apps/blog/templates/blog/blog.html


#### 5. Membuat laman post

        modified:   README.md
        new file:   apps/blog/templates/blog/post.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


## 9. MENTAUTKAN LAMAN WEB


#### 1. Mentautkan laman-laman web

        modified:   README.md
        modified:   apps/blog/templates/blog/contact.html
        modified:   apps/blog/templates/blog/partials/_footer.html
        modified:   apps/blog/templates/blog/partials/_header.html


## 10. POST APP


#### 1. Membuat aplikasi Post

        modified:   README.md
        new file:   apps/post/__init__.py
        new file:   apps/post/admin.py
        new file:   apps/post/apps.py
        new file:   apps/post/migrations/__init__.py
        new file:   apps/post/models.py
        new file:   apps/post/tests.py
        new file:   apps/post/views.py


#### 2. Register aplikasi Post pada dreamblog

        (dreamblog) λ python manage.py check
        System check identified no issues (0 silenced).
        
        modified:   README.md
        modified:   apps/post/apps.py
        modified:   dreamblog/settings.py


## 11. DATABASE


#### 1. Membuat Postgres Database

        modified:   README.md
        modified:   dreamblog/settings.py


#### 2. Menghubungkan database dengan proyek

        (dreamblog) λ pip install psycopg2-binary
        Collecting psycopg2-binary
          Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
        Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)
        Installing collected packages: psycopg2-binary
        Successfully installed psycopg2-binary-2.9.9

        modified:   README.md
        modified:   dreamblog/settings.py


#### 3. Mengamankan database

        (dreamblog) λ touch .env .env-example

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ pip install django-environ
        Collecting django-environ
          Using cached django_environ-0.11.2-py2.py3-none-any.whl.metadata (11 kB)
        Using cached django_environ-0.11.2-py2.py3-none-any.whl (19 kB)
        Installing collected packages: django-environ
        Successfully installed django-environ-0.11.2

        STEPS:

        1. Install: pip install django-environ
        2. Create .env file
        3. Setup .env
                DEBUG=on
                SECRET_KEY=
                DATABASE_NAME=
                DATABASE_USER=
                DATABASE_PASSWORD=
        4. Setup settings.py in 6 steps:

                # step: 1 of 6 import environ
                import environ
                env = environ.Env( # new
                    # set casting, default value
                    DEBUG=(bool, False)
                )

                # step: 2 of 6:  Set the project base directory
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

                # step: 3 of 6: Take environment variables from .env file
                environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

                # step: 4 of 6: SECURITY WARNING: keep the secret key used in production secret!
                SECRET_KEY = env('SECRET_KEY')

                # step: 5 of 6: False if not in os.environ because of casting above
                DEBUG = env('DEBUG') # new

                # step: 6 of 6: Set the db connection
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': env('DATABASE_NAME'),
                        'USERNAME': env('DATABASE_USER'),
                        'PASSWORD': env('DATABASE_PASSWORD'),
                        'HOST': 'localhost',
                        'PORT': '5432'
                    }
                }

        5. Check: 
        (dreamblog) λ python manage.py check
        System check identified no issues (0 silenced).

        6. source: https://django-environ.readthedocs.io/en/latest/quickstart.html

        new file:   .env-example
        modified:   .gitignore
        modified:   README.md
        modified:   dreamblog/settings.py


## 12. MODELS


#### 1. Membuat analisa content

        """ ======================================
        ANALISA BERDASARKAN DEMO PROYEK (TEMPLATE)
        ==========================================

        Setiap post terdiri dari:

        .category
        .tag
        .title
        .overview
        .thumbnail
        .author:
                .author name
                .author profile_picture
        .timestamp atau tanggal terbit
        .jumlah komen
        .jumlah berapa kali dibuka/dilihat oleh user
        .jenis post:
                . featured
                . bukan featured

        JADI, berdasarkan analisa di atas kita harus membuat 4 model:

        1. Author
        2. Category
        3. Tag
        4. Post

        Hubungan / relationship antar model:

        1. Author dan Post memiliki hubungan OneToMany
        
           1.1 Di dalam tabel Author, dapat berisi 0, 1, atau banyak author.
           1.2 Setiap author, memiliki nama dan photonya.
           1.3 Setiap author dapat membuat 0, 1, atau banyak post.
               Dengan kata lain, setiap post dibuat oleh seorang author.
           1.4 Setiap post memiliki banyak atribut (lihat poin 4)

        2. Category dan Post memiliki hubungan ManyToMany

           2.1 Di dalam table Category, dapat berisi 0, 1, atau banyak category.
           2.2 Setiap category memiliki nama dan mungkin juga memiliki slug.
           2.3 Dalam hubungannya dengan post, setiap category dapat memiliki 0, 1, atau banyak post.
               Dengan kata lain, setiap post dapat menjadi bagian dari satu atau lebih dari satu category.
           1.4 Setiap post memiliki banyak atribut (lihat poin 4)

        3. Category dan Tag memiliki hubungan OneToMany

           3.1 Di dalam table Category, dapat berisi 0, 1, atau banyak category.
           3.2 Setiap category memiliki nama dan mungkin juga memiliki slug.
           3.3 Di dalam tabel Tag, dapat berisi 0, 1, atau banyak tag.
           4.3 Setiap tag, atau beberapa tag dapat menjadi bagian dari satu category.
               Dengan kata lain, sebuah category dapat memiliki 0, 1, atau banyak tag.

        4. Post dan Category memiliki hubungan ManyToMany

           4.1 Di dalam tabel post, dapat berisi 0, 1, atau banyak category yang didasarkan pada id dari category yang bersangkutan.
               Dengan kata lain, setiap post harus menjadi bagian dari sebuah category.
               Atau, setiap category dapat memiliki 0, 1, atau banyak post.

        5. Post dan Tag memiliki hubungan ManyToMany

           5.1 Di dalam tabel post, dapat berisi 0, 1, atau banyak tag yang didasarkan pada id dari tag yang bersangkutan.
               Dengan kata lain, setiap post harus menjadi bagian dari sebuah tag.
               Atau, setiap tag dapat memiliki 0, 1, atau banyak post.

        NOTE:

        Di dalam Django, dua model atau entitas yang memiliki hubungan ManyToMany, maka Django akan
        secara otomatis membuatkan entitas baru yang menghubungkan kedua model.

        """
        modified:   README.md
        modified:   apps/post/models.py


#### 2. Membuat model Author

        modified:   README.md
        modified:   apps/post/models.py


#### 3. Membuat model Category

        modified:   README.md
        modified:   apps/post/models.py


#### 4. Membuat model Tag

        modified:   README.md
        modified:   apps/post/models.py


#### 5. Membuat model Post

        modified:   README.md
        modified:   apps/post/models.py


#### 6. Menambahkan hubungan OneToMany antar model Category dan Tag
 
        modified:   README.md
        modified:   apps/post/models.py


#### 7. Menambahkan hubungan OneToMany antar model Author dan Post
 
        modified:   README.md
        modified:   apps/post/models.py