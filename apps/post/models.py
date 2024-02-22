# apps/post/models.py

# Django and third parties modules
from django.db import models
from django.contrib.auth import get_user_model

# Define User
User = get_user_model()

# Locals

# Create your models here.


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


# Author model
class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField()

	def __str__(self):
		return self.user.username