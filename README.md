1.--------------
- Untuk membuat projek django baru yang pertama dilakukan adalah membuka terminal dan menulis perintah "django-admin startproject nama_proyek". Dengan dijalankan perintah tersebut, Django akan membuat struktur awal "main" di direktori.
- lalu lanjut di terminal yang sama dan menjalan "python manage.py startapp main" setelah itu akan terbentuk direktori baru bernama main
- Untuk melakukan routing proyek, kita membuka urls.py di direktori main. lalu menuliskan kode "
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
] "
kode tersebut mengkonfigurasi URL pattern untuk aplikasi "main" dalam proyek Django. Ketika mengunjungi URL utama dari aplikasi "main," fungsi show_main akan dipanggil, dan URL pattern ini memiliki nama "show_main" yang dapat digunakan dalam kode lain untuk mengacu pada URL.
- Pertama-tama buka models.py dalam direktori main, lalu tulis kode "from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    promo = models.CharField(max_length=255)
    price = models.IntegerField()

Kode tersebut berupa model django berupa product. name berupa charfield dimana menyimpan text. amount menyimpan bilangan bulat. description menyimpan text panjang yang tidak terbatas. Lalu kita jalankan perintah migrasi untuk membuat tabel database.
- pertama-tama buka views.py pada direktori main dan tulis kode "
def show_main(request):
    context = {
        'item_inventory' : [
            {
                'name': 'Piring The Flop',
                'description': 'Piring yang lansung dibuat dari Norwegia pembawa kekuatan',
                'amount': '5',
                'promo' : 'FLASH SALE 50%',
                'price': '1000000'  
            },
        ],
    }
    return render(request, "main.html", context)"
"from django.shortcuts import render" berfungsi untuk mengimpor fungsi render. contexr akan menyimpan dictionary yang nantinya akan dikirimkan ke tampilan. Lalu "return render(request, "main.html", context)" akan merender tampilan tersebut pada main.html. Untuk isi item_inventory disesuaikan dengan isi tabel, dimana kita mengisi tiap variabel dengan apa yang ingin dikeluarkan di tabel.
- Buka urls.py dalam direktori proyek di shoptheflop dan menambahkan fungsi include dan rute url untuk mengarahkan ke tampilan main.
- Untuk mendeploy pertama menekan new app lalu mengubungkan dengan respitory github, lalu memilih template python dan basis data postgreSQL dan lalu mendeploy. Setelah berhasil aplikasi sudah dapat dibuka.

2-------------
<img src="/bagan.jpg"

File urls.py berfungsi sebagai penghubung antara URL yang diminta oleh klien dengan fungsi view yang sesuai. Ini adalah bagian yang menentukan bagaimana URL akan dipetakan ke tindakan tertentu dalam aplikasi. Di sisi lain, views.py berperan sebagai pengendali utama dalam aplikasi Django. Fungsi-fungsi view dalam berkas ini memproses permintaan yang datang dari klien. Mereka juga berfungsi sebagai perantara antara model dan templat HTML. file models.py, yang terletak dalam direktori memiliki peran  dalam mendefinisikan struktur data yang akan disimpan dalam database. Model-model ini digunakan untuk merepresentasikan entitas seperti pengguna, produk, atau catatan lainnya, serta mendefinisikan bidang yang akan menyimpan data terkait. Model-model ini menjadi dasar untuk operasi database dalam Django, seperti migrasi schema dan pengambilan data.Terakhir, template HTML berfungsi sebagai kerangka dasar untuk menghasilkan halaman web yang akan diberikan kepada klien. Dalam template, akan digabungkan logika tampilan dengan data yang dikirimkan oleh view sehingga dapat menampilkan informasi dinamis kepada pengguna. Template dapat mengakses data dari model atau objek lain yang diteruskan oleh view sebagai konteks.

Dengan sinergi antara urls.py, views.py, models.py, dan templat HTML, aplikasi Django menjadi kuat dan fleksibel dalam mengelola permintaan klien dan menyajikan data dengan cara yang sesuai.

3-------------
Untitled (1) <img src="Untitled (2).png">
Virtual environment adalah suatu platform atau wadah yang digunakan oleh Django untuk menjalankan aplikasi. Fungsi utama dari virtual environment adalah memungkinkan kita untuk menginstal serta mengelola berbagai paket Python yang diperlukan oleh aplikasi kita secara terpisah dari paket Python global yang terdapat di sistem operasi. Dengan cara ini, kita dapat menghindari potensi konflik versi atau masalah dependensi antara aplikasi yang berbeda.

Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, praktik ini tidak disarankan. Tanpa virtual environment, kita diharuskan menginstal semua paket Python yang dibutuhkan oleh aplikasi secara langsung ke sistem operasi kita. Hal ini dapat menimbulkan masalah kompatibilitas atau keamanan, terutama jika aplikasi lain juga membutuhkan paket Python yang sama. Oleh karena itu, penggunaan virtual environment sangat disarankan agar kita dapat mengisolasi dan mengelola dependensi aplikasi dengan lebih baik.


4-------------
MVC, MVT, serta MVVM adalah rangkaian arsitektur yang dipergunakan untuk mengisolasi logika bisnis, antarmuka, dan koneksi pengguna dalam proses pengembangan perangkat lunak. 

Model-View-Controller (MVC) adalah pola arsitektur yang membantu mengorganisir struktur aplikasi. Pola ini membagi tanggung jawabnya ke dalam tiga lapisan yaitu, Model, View, dan Controller. Model adalah lapisan data yang mengelola logika bisnis dan mendukung API jaringan atau database. Model bekerja dengan sumber data lokal dan remote untuk mengambil dan menyimpan data. Di sini logika bisnis diatur. View adalah lapisan antarmuka pengguna (UI) yang bertanggung jawab untuk visualisasi data dari Model ke pengguna. Ini mengatur tampilan data, termasuk antarmuka grafis. Controller adalah lapisan logis yang mengintegrasikan lapisan View dan Model. Tugas Controller adalah mengambil masukan pengguna dan menentukan tindakan apa yang harus dilakukan.

MVT (Model-View-Template) mirip dengan MVC, tetapi menggunakan template sebagai view. Template adalah file HTML yang dapat menyisipkan data dari model. MVT biasanya digunakan dalam framework web seperti Django. MVP membagi struktur aplikasi menjadi lapisan View, Model, dan Presenter. Model secara analogi sama dengan pola MVC. View merupakan lapisan antarmuka pengguna (UI), bertanggung jawab untuk menampilkan data kepada pengguna sesuai yang ditentukan oleh Presenter. Ini dapat diimplementasikan oleh Activities, Fragments, atau tampilan umum lainnya. Presenter adalah lapisan logika yang berperan sebagai perantara antara lapisan View dan Model. Presenter berhubungan dengan kedua lapisan View dan Model serta merespons tindakan yang dilakukan oleh pengguna.

Model-View-ViewModel (MVVM) adalah pola berbasis event-based pattern. Berkat ini, user dapat bereaksi dengan cepat terhadap pola desain dan perubahan. Pola arsitektur ini memungkinkan user untuk lebih memisahkan antarmuka pengguna dari logika bisnis dan perilaku, bahkan lebih dari yang dilakukan oleh MVC atau MVP. Pola ini memiliki view-model dan view. ViewModel untuk menangani pengiriman data dari Model ke lapisan View dan mengelola tindakan pengguna. ViewModel menyediakan aliran data untuk View. View adalah lapisan antarmuka pengguna bertanggung jawab untuk menampilkan data, status sistem, dan operasi saat ini dalam antarmuka grafis. Selain itu, view menginisialisasi dan mengikat ViewModel dengan elemen-elemen View.

Maka dapat disimpulkan, MVC adalah Logika Model dipisahkan dari logika tampilan View, dan logika input diurus oleh Controller. MVP adalah Evolusi dari MVC. Presenter mengelola logika input dan logika tampilan. View lebih pasif dan hanya menangani Rendering dan pengelolaan Event. Terakhir, MVVM yang mirip dengan MVP tetapi menggunakan pengikatan (binding) antara View dan ViewModel. Pada dasarnya VC, MVP, dan MVVM sebenarnya adalah pola yang sama. Perbedaannya terletak pada bagaimana mereka diimplementasikan berdasarkan batasan dalam sistem yang dikerjakan. 
