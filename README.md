Nama : Arief Ridzki Darmawan

NPM : 2306210115

Kelas : PBP F

---

## Jawaban Pertanyaan Tugas 3

### > Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian platform karena memungkinkan komunikasi antar komponen, memastikan interaksi pengguna secara real-time, dan menjaga konsistensi data di seluruh sistem. Hal ini mendukung skalabilitas dan kinerja dengan menangani traffic yang besar secara efisien sambil mengurangi latensi. Tanpa data delivery yang efektif, platform akan sulit beroperasi dengan lancar dan memenuhi kebutuhan pengguna atau bisnis.

### > Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer daripada XML karena lebih sederhana, strukturnya ringan, dan kemudahan penggunaannya. JSON memiliki sintaks yang sederhana dengan overhead yang lebih sedikit, membuatnya efisien untuk transmisi data, terutama di web. JSON didukung secara native oleh JavaScript, menjadikannya ideal untuk pengembangan web, dan JSON menangani tipe data seperti angka dan array lebih efektif dibandingkan XML yang memperlakukan semua data sebagai teks. Selain itu, JSON banyak digunakan dalam API karena ukurannya yang lebih kecil dan parsing yang lebih cepat, sementara XML lebih cocok untuk struktur data yang kompleks, namun umumnya lebih verbose dan sulit digunakan.

### > Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Metode is_valid() di Django sangat penting untuk memastikan bahwa data dari form atau serializer memenuhi aturan validasi, sehingga mencegah data yang tidak valid atau berbahaya diproses. Metode ini memeriksa data berdasarkan kriteria yang telah ditentukan, menangani kesalahan dengan memberikan feedback. Jika valid, data yang sudah bersih dapat diakses untuk digunakan dengan aman. 

### > Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token di Django mencegah serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat menipu pengguna agar tanpa sadar mengirim permintaan yang tidak diizinkan ke sebuah situs web. Tanpa token ini, penyerang bisa mengeksploitasi sesi yang telah diautentikasi dan membuat perubahan atau tindakan yang tidak diizinkan atas nama pengguna. Token ini memastikan bahwa pengiriman form berasal dari sumber tepercaya dengan memverifikasikan keaslian permintaan sehingga mencegah tindakan berbahaya dari situs web eksternal.

### > Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Mengubah primary key menjadi UUID untuk mencegah celah keamanan dan melakukan migrasi
* Membuat forms.py berisi struktur form (fields untuk model)
* Import class form dan model ke views.py dan buat fungsi create_product yang menerima parameter request
* Import fungsi create_product pada views.py dan menambahkan path url ke url_patterns
* Buat file create_product.html pada templates
* Tambahkan kode untuk menampilkan data produk dalam bentuk tabel serta tombol "Add Product" yang akan redirect ke halaman form
* Menjalankan server Django pada localhost untuk memastikan bahwa fitur berfungsi
* Import HttpResponse dan serializers pada views.py dan buat fungsi show_xml yang me-return HttpResponse
* Import fungsi show_xml pada views.py dan menambahkan path url ke url_patterns
* Membuat fungsi show_json yang me-return HttpResponse
* Import fungsi show_json pada views.py dan menambahkan path url ke url_patterns
* Buat request baru pada postman dengan method GET dengan url http://localhost:8000/xml/ dan http://localhost:8000/json/ untuk mengetes apakah data terkirim
* Membuat direktori .github pada proyek dengan subdirektori workflows
* Membuat file deploy.yml pada direktori workflows
* Buat secret pada repositori, dengan nama PWS_URL dan mengisinya dengan format https://(username.sso):(password proyek PWS)@pbp.cs.ui.ac.id/(username.sso)/(nama proyekmu)
* Menambahkan CSRF_TRUSTED_ORIGINS pada settings.py di direktori proyek
* Melakukan add, commit, dan push ke repository GitHub dan mengecek apakah proyek di PWS sudah ter-deploy secara otomatis

### > Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![Screenshot 2024-09-17 221822](https://github.com/user-attachments/assets/c2f88511-87ba-4cd3-822a-c93408f27278)
![Screenshot 2024-09-17 222002](https://github.com/user-attachments/assets/2256087d-befb-43af-a9dc-32f23617c064)
![Screenshot 2024-09-17 221932](https://github.com/user-attachments/assets/3341fecb-4d9f-4a47-9bba-36e3e37ffd0f)
![Screenshot 2024-09-17 222018](https://github.com/user-attachments/assets/3d55c02f-4c24-4d5f-b54f-63c730850822)

---

## Jawaban Pertanyaan Tugas 2

### > Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

### > Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Frame 1](https://github.com/user-attachments/assets/bdbde251-4b8b-4e8b-9ec0-6605d80cc51c)

### > Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem pengontrol versi, yaitu untuk mencatat setiap perubahan file proyek yang dikerjakan oleh seorang atau banyak orang. Hal ini meningkatkan efisiensi dalam pembuatan program karena setiap perubahan dapat dilacak secara detail, memudahkan rollback ke versi sebelumnya jika terjadi kesalahan, serta memungkinkan kolaborasi antar pengembang dengan sinkronisasi yang baik. Git juga memungkinkan penggabungan (merge) dari berbagai cabang (branch) proyek sehingga tim bisa bekerja secara paralel tanpa mengganggu alur kerja satu sama lain.

### > Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django adalah framework yang ideal untuk memulai pengembangan perangkat lunak karena mempunyai fitur bawaan yang berguna seperti autentikasi, ORM, dan keamanan yang cukup kuat. Arsitekturnya yang terstruktur membuat Django mendukung skalabilitas seiring pertumbuhan aplikasi. Fitur keamanannya juga kuat, seperti perlindungan terhadap SQL injection dan CSRF. Selain itu, komunitas dan dokumentasi Django luas, ditambah dengan keserbagunaannya untuk berbagai proyek mulai dari situs web kecil hingga aplikasi berskala besar.

### > Mengapa model pada Django disebut sebagai ORM?
Dalam Django, model disebut ORM (Object-Relational Mapping) karena memetakan objek Python ke tabel database relasional, yang memungkinkan developer berinteraksi dengan database menggunakan kode Python tanpa harus menulis SQL secara langsung. Setiap class atribut model mewakili sebuah tabel kolom atau fields, sedangkan instance-nya mewakili sebuah baris. ORM menangani konversi antara kedua format ini, memudahkan operasi database seperti membuat, mengambil, memperbarui, atau menghapus data.
