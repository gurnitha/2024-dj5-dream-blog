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


#### 8. Menambahkan hubungan ManyToMany antar model Category dan Post
 
        modified:   README.md
        modified:   apps/post/models.py


#### 9. Menambahkan hubungan ManyToMany antar model Tag dan Post
 
        modified:   README.md
        modified:   apps/post/models.py


#### 10. Menginstal Pillow


        (dreamblog) λ python manage.py check
        SystemCheckError: System check identified some issues:

        ERRORS:
        post.Author.profile_picture: (fields.E210) Cannot use ImageField because Pillow is not installed.
                HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
        post.Post.thumbnail: (fields.E210) Cannot use ImageField because Pillow is not installed.
                HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".

        System check identified 2 issues (0 silenced).

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ pip install pillow
        Collecting pillow
          Using cached pillow-10.2.0-cp312-cp312-win_amd64.whl.metadata (9.9 kB)
        Using cached pillow-10.2.0-cp312-cp312-win_amd64.whl (2.6 MB)
        Installing collected packages: pillow
        Successfully installed pillow-10.2.0

        NOTE:

        Karena di dalam tabel Author ada kolom profile_picture (tempat image),
        maka Django akan minta kita untuk menginstal Pillow.


## 13. DJANGO ADMIN DAN MIGRASI


#### 1. Fixing issues

        modified:   README.md
        modified:   dreamblog/settings.py


#### 2. Menjalankan perintah makemigrations

        NOTE: Tentang peringah makemigrations

        Saat Anda membuat perubahan pada model Anda, seperti menambahkan bidang baru, mengubah jenis bidang, atau bahkan membuat model baru, menjalankannya akan makemigrationsmenganalisis perubahan tersebut dan menghasilkan file migrasi yang menangkap perubahan dalam format yang dapat dibaca manusia. File migrasi ini disimpan di migrationsdirektori aplikasi Anda.

        Makemigrations di Django pada dasarnya menghasilkan perintah SQL untuk aplikasi yang sudah diinstal sebelumnya (yang dapat dilihat di aplikasi yang diinstal di settings.py) dan model aplikasi yang baru Anda buat yang Anda tambahkan di aplikasi yang diinstal. Itu tidak menjalankan perintah-perintah itu di file database Anda. Jadi tabel tidak dibuat setelah melakukan migrasi. Setelah menerapkan makemigrations Anda dapat melihat perintah SQL tersebut dengan sqlmigrate yang menampilkan semua perintah SQL yang telah dihasilkan oleh makemigrations. Untuk mengetahui lebih lanjut tentang makemigrations, kunjungi

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py check
        System check identified no issues (0 silenced).

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py makemigrations
        Migrations for 'post':
          apps\post\migrations\0001_initial.py
            - Create model Category
            - Create model Author
            - Create model Tag
            - Create model Post

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-dream-blog\root(main -> origin)
        (dreamblog) λ python manage.py sqlmigrate post 0001
        BEGIN;
        --
        -- Create model Category
        --
        CREATE TABLE "post_category" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "title" varchar(25) NOT NULL
        );
        
        --
        -- Create model Author
        --
        CREATE TABLE "post_author" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "profile_picture" varchar(100) NOT NULL, "user_id" integer NOT NULL UNIQUE
        );
        
        --
        -- Create model Tag
        --
        CREATE TABLE "post_tag" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "title" varchar(30) NOT NULL, "category_id" bigint NOT NULL
        );
        
        --
        -- Create model Post
        --
        CREATE TABLE "post_post" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "title" varchar(100) NOT NULL, 
                "overview" text NOT NULL, 
                "timestamp" timestamp with time zone NOT NULL, 
                "comment_count" integer NOT NULL, 
                "view_count" integer NOT NULL, 
                "thumbnail" varchar(100) NOT NULL, 
                "featured" boolean NOT NULL, 
                "author_id" bigint NOT NULL
        );

        CREATE TABLE "post_post_categories" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "post_id" bigint NOT NULL, 
                "category_id" bigint NOT NULL
        );

        CREATE TABLE "post_post_tags" (
                "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, 
                "post_id" bigint NOT NULL, 
                "tag_id" bigint NOT NULL
        );

        ALTER TABLE "post_author" 
        ADD CONSTRAINT 
                "post_author_user_id_8583799e_fk_auth_user_id" 
                FOREIGN KEY ("user_id") 
                REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
        
        ALTER TABLE "post_tag" 
        ADD CONSTRAINT 
                "post_tag_category_id_885a6954_fk_post_category_id" 
                FOREIGN KEY ("category_id") 
                REFERENCES "post_category" ("id") DEFERRABLE INITIALLY DEFERRED;
        
        CREATE INDEX "post_tag_category_id_885a6954" ON "post_tag" ("category_id");

        ALTER TABLE "post_post" 
        ADD CONSTRAINT 
                "post_post_author_id_99d134d5_fk_post_author_id" 
                FOREIGN KEY ("author_id") 
                REFERENCES "post_author" ("id") DEFERRABLE INITIALLY DEFERRED;

        CREATE INDEX "post_post_author_id_99d134d5" ON "post_post" ("author_id");

        ALTER TABLE "post_post_categories" 
        ADD CONSTRAINT 
                "post_post_categories_post_id_category_id_a3046e59_uniq" 
                UNIQUE ("post_id", "category_id");

        ALTER TABLE "post_post_categories" 
                ADD CONSTRAINT "post_post_categories_post_id_4e6b60a6_fk_post_post_id" 
                FOREIGN KEY ("post_id") 
                REFERENCES "post_post" ("id") DEFERRABLE INITIALLY DEFERRED;

        ALTER TABLE "post_post_categories" 
                ADD CONSTRAINT "post_post_categories_category_id_c3484c55_fk_post_category_id" 
                FOREIGN KEY ("category_id") 
                REFERENCES "post_category" ("id") DEFERRABLE INITIALLY DEFERRED;

        CREATE INDEX "post_post_categories_post_id_4e6b60a6" ON "post_post_categories" ("post_id");
        CREATE INDEX "post_post_categories_category_id_c3484c55" ON "post_post_categories" ("category_id");

        ALTER TABLE "post_post_tags" 
        ADD CONSTRAINT 
                "post_post_tags_post_id_tag_id_15c628ee_uniq" 
                UNIQUE ("post_id", "tag_id");
        
        ALTER TABLE "post_post_tags" 
        ADD CONSTRAINT 
                "post_post_tags_post_id_6adf1c1b_fk_post_post_id" 
                FOREIGN KEY ("post_id") 
                REFERENCES "post_post" ("id") DEFERRABLE INITIALLY DEFERRED;

        ALTER TABLE "post_post_tags" 
        ADD CONSTRAINT 
                "post_post_tags_tag_id_cb551e85_fk_post_tag_id" 
                FOREIGN KEY ("tag_id") 
                REFERENCES "post_tag" ("id") DEFERRABLE INITIALLY DEFERRED;
        
        CREATE INDEX "post_post_tags_post_id_6adf1c1b" ON "post_post_tags" ("post_id");
        CREATE INDEX "post_post_tags_tag_id_cb551e85" ON "post_post_tags" ("tag_id");
        COMMIT;

        modified:   README.md
        new file:   apps/post/migrations/0001_initial.py