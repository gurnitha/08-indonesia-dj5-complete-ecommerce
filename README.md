# 08-indonesia-dj5-complete-ecommerce
Membuat aplikasi ecommerce lengkap menggunakan Django versi 5
Github:https://github.com/gurnitha/08-indonesia-dj5-complete-ecommerce


## 1. SETUP

#### 1. Complete setup menampilkan halo dunia

        new file:   .env.example
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/urls.py
        new file:   app/main/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   requirements.txt

        Aktivitas:

        1. Membuat remote repositori.
        2. Mengklon remote repositori.
        3. Mengklon snipet complete basics setup
        4. Setup environ variable.


## 2. PROYEK DAN APLIKSI DJANGO

#### 1. Menghapus aplikasi main

        modified:   README.md
        deleted:    app/main/__init__.py
        deleted:    app/main/admin.py
        deleted:    app/main/apps.py
        deleted:    app/main/migrations/__init__.py
        deleted:    app/main/models.py
        deleted:    app/main/tests.py
        deleted:    app/main/urls.py
        deleted:    app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py

#### 2. Membuat aplikasi shop

        modified:   README.md
        new file:   app/shop/__init__.py
        new file:   app/shop/admin.py
        new file:   app/shop/apps.py
        new file:   app/shop/migrations/__init__.py
        new file:   app/shop/models.py
        new file:   app/shop/tests.py
        new file:   app/shop/views.py

#### 3. Mengintegrasikan Aplikasi shop dengan Proyek

        modified:   app/shop/apps.py
        modified:   config/settings.py

#### 4. Menampilkan Selamat Datang di INGShop

        modified:   README.md
        new file:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   config/urls.py