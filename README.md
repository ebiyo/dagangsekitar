Nama : Arief Ridzki Darmawan

NPM : 2306210115

Kelas : PBP F

Jawaban Pertanyaan Tugas 2

### * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Membuat direktori dagangsekitar lokal
* Membuat repository dagangsekitar pada GitHub
* Menghubungkan direktori lokal dengan repository GitHub dengan command git remote add origin
* Mengaktifkan virtual environment
* Membuat requirements.txt pada direktori lokal dan melakukan pip install -r requirements.txt
* Membuat proyek Django baru bernama dagangsekitar
* Menambahkan "127.0.0.1" pada ALLOWED_HOSTS
* Menjalankan server Django pada localhost untuk memastikan bahwa Django berhasil diinstal
* Menambahkan file .gitignore
* Membuat proyek baru pada website PWS dan menambahkan url deployment pada ALLOWED_HOSTS
* Membuat aplikasi main baru pada direktori lokal dengan command py manage.py startapp main
* Menambahkan 'main' pada INSTALLED_APPS
* Membuat folder templates berisi main.html pada aplikasi main
* Mengisi main.html dengan apa yang ingin ditampilkan (nama toko, npm, nama, kelas)
* Mengisi models.py pada aplikasi main dengan class Product dengan atribut name, price, dan description
* Melakukan migrasi model
* Menambahkan fungsi show_main pada views.py pada aplikasi main
* Membuat urls.py pada aplikasi main dan mengisinya dengan routing untuk memetakan fungsi pada views.py
* Menambahkan path('', include('main.urls')) pada url_patterns pada proyek dagangsekitar (bukan di main)
* Membuat tests.py pada aplikasi main dan mengisinya dengan test case
* Melakukan add, commit, dan push ke repository GitHub
* Melakukan push ke PWS

### * Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
[Link Bagan](https://drive.google.com/file/d/1cXv8iSAX9yDLXXuejRB-dl_tzLU7R90H/view?usp=sharing)

### * Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem pengontrol versi, yaitu untuk mencatat setiap perubahan file proyek yang dikerjakan oleh seorang atau banyak orang. Hal ini meningkatkan efisiensi dalam pembuatan program karena setiap perubahan dapat dilacak secara detail, memudahkan rollback ke versi sebelumnya jika terjadi kesalahan, serta memungkinkan kolaborasi antar pengembang dengan sinkronisasi yang baik. Git juga memungkinkan penggabungan (merge) dari berbagai cabang (branch) proyek sehingga tim bisa bekerja secara paralel tanpa mengganggu alur kerja satu sama lain.

### * Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django adalah framework yang ideal untuk memulai pengembangan perangkat lunak karena mempunyai fitur bawaan yang berguna seperti autentikasi, ORM, dan keamanan yang cukup kuat. Arsitekturnya yang terstruktur membuat Django mendukung skalabilitas seiring pertumbuhan aplikasi. Fitur keamanannya juga kuat, seperti perlindungan terhadap SQL injection dan CSRF. Selain itu, komunitas dan dokumentasi Django luas, ditambah dengan keserbagunaannya untuk berbagai proyek mulai dari situs web kecil hingga aplikasi berskala besar.

### * Mengapa model pada Django disebut sebagai ORM?
Dalam Django, model disebut ORM (Object-Relational Mapping) karena memetakan objek Python ke tabel database relasional, yang memungkinkan developer berinteraksi dengan database menggunakan kode Python tanpa harus menulis SQL secara langsung. Setiap class atribut model mewakili sebuah tabel kolom atau fields, sedangkan instance-nya mewakili sebuah baris. ORM menangani konversi antara kedua format ini, memudahkan operasi database seperti membuat, mengambil, memperbarui, atau menghapus data.
