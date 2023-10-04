# TUGAS 2
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
<img src="/main//Untitled (2).png">

File urls.py berfungsi sebagai penghubung antara URL yang diminta oleh klien dengan fungsi view yang sesuai. Ini adalah bagian yang menentukan bagaimana URL akan dipetakan ke tindakan tertentu dalam aplikasi. Di sisi lain, views.py berperan sebagai pengendali utama dalam aplikasi Django. Fungsi-fungsi view dalam berkas ini memproses permintaan yang datang dari klien. Mereka juga berfungsi sebagai perantara antara model dan templat HTML. file models.py, yang terletak dalam direktori memiliki peran  dalam mendefinisikan struktur data yang akan disimpan dalam database. Model-model ini digunakan untuk merepresentasikan entitas seperti pengguna, produk, atau catatan lainnya, serta mendefinisikan bidang yang akan menyimpan data terkait. Model-model ini menjadi dasar untuk operasi database dalam Django, seperti migrasi schema dan pengambilan data.Terakhir, template HTML berfungsi sebagai kerangka dasar untuk menghasilkan halaman web yang akan diberikan kepada klien. Dalam template, akan digabungkan logika tampilan dengan data yang dikirimkan oleh view sehingga dapat menampilkan informasi dinamis kepada pengguna. Template dapat mengakses data dari model atau objek lain yang diteruskan oleh view sebagai konteks.

Dengan sinergi antara urls.py, views.py, models.py, dan templat HTML, aplikasi Django menjadi kuat dan fleksibel dalam mengelola permintaan klien dan menyajikan data dengan cara yang sesuai.

3-------------
Virtual environment adalah suatu platform atau wadah yang digunakan oleh Django untuk menjalankan aplikasi. Fungsi utama dari virtual environment adalah memungkinkan kita untuk menginstal serta mengelola berbagai paket Python yang diperlukan oleh aplikasi kita secara terpisah dari paket Python global yang terdapat di sistem operasi. Dengan cara ini, kita dapat menghindari potensi konflik versi atau masalah dependensi antara aplikasi yang berbeda.

Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, praktik ini tidak disarankan. Tanpa virtual environment, kita diharuskan menginstal semua paket Python yang dibutuhkan oleh aplikasi secara langsung ke sistem operasi kita. Hal ini dapat menimbulkan masalah kompatibilitas atau keamanan, terutama jika aplikasi lain juga membutuhkan paket Python yang sama. Oleh karena itu, penggunaan virtual environment sangat disarankan agar kita dapat mengisolasi dan mengelola dependensi aplikasi dengan lebih baik.


4-------------
MVC, MVT, serta MVVM adalah rangkaian arsitektur yang dipergunakan untuk mengisolasi logika bisnis, antarmuka, dan koneksi pengguna dalam proses pengembangan perangkat lunak. 

Model-View-Controller (MVC) adalah pola arsitektur yang membantu mengorganisir struktur aplikasi. Pola ini membagi tanggung jawabnya ke dalam tiga lapisan yaitu, Model, View, dan Controller. Model adalah lapisan data yang mengelola logika bisnis dan mendukung API jaringan atau database. Model bekerja dengan sumber data lokal dan remote untuk mengambil dan menyimpan data. Di sini logika bisnis diatur. View adalah lapisan antarmuka pengguna (UI) yang bertanggung jawab untuk visualisasi data dari Model ke pengguna. Ini mengatur tampilan data, termasuk antarmuka grafis. Controller adalah lapisan logis yang mengintegrasikan lapisan View dan Model. Tugas Controller adalah mengambil masukan pengguna dan menentukan tindakan apa yang harus dilakukan.

MVT (Model-View-Template) mirip dengan MVC, tetapi menggunakan template sebagai view. Template adalah file HTML yang dapat menyisipkan data dari model. MVT biasanya digunakan dalam framework web seperti Django. MVP membagi struktur aplikasi menjadi lapisan View, Model, dan Presenter. Model secara analogi sama dengan pola MVC. View merupakan lapisan antarmuka pengguna (UI), bertanggung jawab untuk menampilkan data kepada pengguna sesuai yang ditentukan oleh Presenter. Ini dapat diimplementasikan oleh Activities, Fragments, atau tampilan umum lainnya. Presenter adalah lapisan logika yang berperan sebagai perantara antara lapisan View dan Model. Presenter berhubungan dengan kedua lapisan View dan Model serta merespons tindakan yang dilakukan oleh pengguna.

Model-View-ViewModel (MVVM) adalah pola berbasis event-based pattern. Berkat ini, user dapat bereaksi dengan cepat terhadap pola desain dan perubahan. Pola arsitektur ini memungkinkan user untuk lebih memisahkan antarmuka pengguna dari logika bisnis dan perilaku, bahkan lebih dari yang dilakukan oleh MVC atau MVP. Pola ini memiliki view-model dan view. ViewModel untuk menangani pengiriman data dari Model ke lapisan View dan mengelola tindakan pengguna. ViewModel menyediakan aliran data untuk View. View adalah lapisan antarmuka pengguna bertanggung jawab untuk menampilkan data, status sistem, dan operasi saat ini dalam antarmuka grafis. Selain itu, view menginisialisasi dan mengikat ViewModel dengan elemen-elemen View.

Maka dapat disimpulkan, MVC adalah Logika Model dipisahkan dari logika tampilan View, dan logika input diurus oleh Controller. MVP adalah Evolusi dari MVC. Presenter mengelola logika input dan logika tampilan. View lebih pasif dan hanya menangani Rendering dan pengelolaan Event. Terakhir, MVVM yang mirip dengan MVP tetapi menggunakan pengikatan (binding) antara View dan ViewModel. Pada dasarnya VC, MVP, dan MVVM sebenarnya adalah pola yang sama. Perbedaannya terletak pada bagaimana mereka diimplementasikan berdasarkan batasan dalam sistem yang dikerjakan. 

# TUGAS 3
1. Form POST digunakan untuk mengirimkan data atau nilai ke server untuk diproses. Data yang dikirimkan tidak ditampilkan secara terbuka pada URL browser. Sebagai contoh, ketika ingin menyimpan atau memperbarui data di server, ,maka menggunakan form POST. Misalnya, ketika mengirimkan informasi dari formulir pendaftaran pengguna, atau ketika Anda ingin memperbarui profil pengguna. contohnya :
if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
form.is_valid(): Ini adalah metode pada objek form Django yang memeriksa apakah data yang diterima dari permintaan (request) adalah valid sesuai dengan aturan validasi yang telah didefinisikan di form.
request.method == "POST": Ini memeriksa apakah metode permintaan adalah POST. Pengecekan ini memastikan bahwa tindakan ini hanya dijalankan jika permintaan adalah tipe POST.
form.save() akan menyimpan data yang sudah dikirim untuk disimpan untuk di form database. Setelah itu akan ada return yang akan mengarahkan ke urls tertentu

Form GET digunakan untuk mengambil data dari server dan menampilkannya di URL. Data yang dikirimkan melalui form GET akan terlihat pada URL dan itu akan berguna untuk permintaan yang hanya mengambil informasi dari server tanpa melakukan perubahan pada data yang ada. Misalnya, ketika ingin melakukan pencarian atau filtering berdasarkan kriteria tertentu.

2. 
- XML (eXtensible Markup Language) adalah bahasa markah yang diciptakan untuk menyediakan aturan yang memungkinkan pengguna untuk mendefinisikan struktur data secara bebas. XML menggunakan tanda markah, seperti <tag>, untuk membedakan antara elemen dan atribut data dalam dokumen. Data diorganisir dalam bentuk hirarki, yang terdiri dari elemen, atribut, dan nilai. XML memisahkan data dari presentasi dan sangat penting dalam pertukaran data antar platform. Keunggulan XML adalah fleksibilitasnya dalam mendefinisikan struktur data yang sesuai dengan kebutuhan aplikasi.

- JSON (JavaScript Object Notation) adalah format pertukaran data ringan yang mudah dibaca baik oleh manusia maupun mesin. JSON menggunakan pasangan kunci-nilai untuk merepresentasikan data, dan data diorganisir dalam bentuk objek dan array. Contoh representasi JSON adalah { "nama": "John Doe", "umur": 30 }. JSON banyak digunakan dalam komunikasi antar server dan klien, terutama dalam pengembangan web dan aplikasi. Keunggulan JSON adalah efisiensi dan kemudahan pengolahan data struktur sederhana hingga kompleks.

- HTML (HyperText Markup Language) adalah bahasa markah yang digunakan untuk membuat halaman web. HTML mengandung elemen-elemen yang mendefinisikan struktur dan tampilan konten pada halaman web. Dalam HTML, elemen-elemen ini diatur dalam hierarki dan mewakili bagian-bagian seperti teks, gambar, tautan, dan elemen lainnya. HTML juga menggunakan tag untuk mengorganisir konten dan memberikan instruksi kepada browser web tentang cara menampilkan halaman. Browser web mengartikan tag HTML untuk membuat tampilan visual yang dapat diakses oleh pengguna.

Perbedaan utama antara XML, JSON, dan HTML terletak pada struktur data. XML menggunakan tag, atribut, dan nilai untuk mengorganisir data dengan fleksibilitas definisi struktur. Di sisi lain, JSON menggunakan pasangan kunci-nilai, objek, dan array, lebih fokus pada efisiensi pertukaran data di web. HTML, pada dasarnya, berfokus pada presentasi konten dan tampilan di browser web, mengatur konten menggunakan elemen dan tag. Tujuan penggunaannya juga berbeda: XML untuk pertukaran data antar platform dan penyimpanan konfigurasi, JSON untuk pertukaran data ringan antar aplikasi dan server, khususnya di web, sementara HTML digunakan untuk membuat halaman web dan menampilkan konten di browser. Pemahaman perbedaan ini memungkinkan pengembang memilih format yang sesuai dengan kebutuhan aplikasi mereka dalam hal pertukaran dan representasi data.

3.
- Pertukaran data yang cepat
JSON mempercepat proses pertukaran data dengan menyediakan struktur data yang lebih sederhana dan kompak. Hal ini bertujuan untuk meminimalkan waktu pemrosesan data sehingga server dapat segera menampilkan data kepada pengguna.
- Penerjemahan data yang mudah dimengerti manusia
JSON mempermudah penerjemahan data ke bahasa manusia. Meskipun komputer hanya dapat memproses data dalam kode biner, JSON membantu menerjemahkan data ini ke dalam teks yang dapat dimengerti oleh manusia, memudahkan perbaikan atau penambahan kode.
- Sederhana dan terstrukut
JSON membawa format yang lebih terstruktur, memudahkan pencarian dan modifikasi kode. Dengan ini, pengguna hanya perlu memasukkan teks dalam bahasa yang mereka pahami, memudahkan proses pengembangan.

4.
- Buat sebuah form Django yang terkait dengan model yang ingin  ditambahkan. Form ini akan digunakan sebagai wadah untuk mengambil input dari pengguna sesuai dengan struktur model yang sudah didefinisikan.contoh:
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
Lalu pada views.py di direktori main buat aplikasi untuk  menangkap data dari form, memvalidasi, dan menyimpannya ke basis data. 
if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
kode tersebut unyuk membuat form dan mevalidasi isi input dari form tersebut. form.save() akan menyimpan data pada form. lalu akan disimpan dan akan diredirect
Lalu pada urls.py pada main ditambahkan path baru untuk dipanggil ketika pengguna mengakses URL yang berakhir dengan path tertentu. Lalu function tersebut akan dipanggil ketika URL tersebut di akses. Lalu buat juga berkas HTML untuk menampilkan halaman saat menambahkan produk. 

Untuk mengembalikan data dalam bentuk html, json, xml, json by id, dan xml by id. Maka diperlukan untuk mengimport  HTTPResponse dan Serializer. HttpResponse adalah kelas yang digunakan untuk menghasilkan tanggapan HTTP yang akan dikirimkan kembali ke pengguna atau klien yang melakukan permintaan. Serializer adalah komponen yang digunakan dalam Django REST framework untuk mengubah objek Python menjadi bentuk data yang dapat di-serialize, seperti JSON, dan sebaliknya. Langkah akhir dari penanganan rute, kita akan melakukan routing seluruh fungsi yang telah dibuat sebelumnya. Kita dapat memasukkan import yang diperlukan ke dalam berkas views.py, dan kemudian menambahkan beberapa rute baru untuk memanggil fungsi melalui URL. Berikut adalah isi dari urls.py

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),   
]

Screenshot Postman
1. HTML
<img src="/ss_postman//html.jpg">
2. JSON
<img src="/ss_postman//json.jpg">
3. XML
<img src="/ss_postman//xml.jpg">
4. JSON by id
<img src="/ss_postman//json_id.jpg">
5. XML by id
<img src="/ss_postman//xml_id.jpg">

Referensi
https://id.natapa.org/difference-between-xml-and-json-2447
https://midtrans.com/id/blog/json-format

# TUGAS 4
## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah sebuah form yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi sebuah web. Form ini memiliki tiga bidang, yaitu username, password ke-1, dan password ke-2 yang merupakan konfirmasi password ke-1 Untuk menggunakan UserCreationForm, maka diperlukan untuk mengimpornya dari django.contrib.auth.forms
# Kelebihan 
- Form ini sudah disediakan oleh Django, sehingga tidak perlu membuatnya dari awal.
- Form ini sudah memiliki validasi dan sanitasi data yang diperlukan, sehingga kita tidak perlu khawatir tentang keamanan dan integritas data.
- Form ini sudah terintegrasi dengan sistem autentikasi Django, sehingga kita dapat dengan mudah mengatur hak akses dan profil pengguna.
-  Form ini terkait erat dengan model User yang sudah ada di Django, sehingga memudahkan penyimpanan informasi pengguna ke dalam database.
- Formulir ini terhubung dengan model User bawaan Django sehingga  proses penyimpanan data pengguna ke dalam database menjadi lebih mudah

# Kekurangan
- Form tidak memiliki tampilan yang menarik atau sesuai dengan tema aplikasi, sehingga perlu mengubahnya dengan CSS atau template.
- UserCreationForm tidak memiliki bidang email bawaan. Akibatnya, user tidak dapat menggunakannya untuk mengirim verifikasi email kepada pengguna guna memverifikasi akun.

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi merupakan langkah untuk memvalidasi identitas pengguna yang hendak mengakses aplikasi web Django. Django telah menyediakan sistem autentikasi terintegrasi yang dapat mengurus berbagai hal, seperti registrasi pengguna, proses login, logout, pengaturan kata sandi, dan aspek lainnya.

Otorisasi adalah proses menentukan apa yang dapat dilakukan pengguna yang terotentikasi di aplikasi web Django. Django menyediakan sistem otorisasi bawaan yang dapat menangani hal-hal seperti pembatasan akses berdasarkan peran pengguna , izin objek, dan grup pengguna.

Kedua konsep, autentikasi dan otorisasi, memiliki peran penting dalam mempertinggi keamanan dan fungsionalitas aplikasi web Django. Autentikasi, misalnya, memiliki dampak positif pada keamanan aplikasi dengan membatasi akses ke platform hanya kepada pengguna yang telah terdaftar dan terotentikasi dengan benar. Hal ini membantu mencegah kemungkinan serangan dari pihak-pihak yang tidak sah atau berpotensi berbahaya.

Di sisi lain, otorisasi memungkinkan pengembang untuk mengontrol dan mengelola tingkat akses pengguna dengan lebih rinci. Pengguna yang berbeda bisa memiliki akses yang berbeda sesuai dengan peran dan tanggung jawab mereka dalam aplikasi web Django. Misalnya, seorang administrator dapat memiliki akses penuh untuk mengelola dan memodifikasi data, sementara pengguna biasa mungkin hanya memiliki akses untuk melihat atau memperbarui profil pribadi mereka.

## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah bagian penting dari penggunaan internet modern. Ketika mengunjungi sebuah situs web, cookies diciptakan dan disimpan di perangkat user melalui browser web. Tugas utamanya adalah menyimpan informasi tertentu tentang aktivitas user, preferensi, atau interaksi dengan situs web tersebut. Ini memungkinkan situs web untuk mengenal user secara lebih baik dan memberikan pengalaman yang dipersonalisasi. Misalnya, cookies dapat mengingat pilihan bahasa atau tema yang user pilih, menyimpan produk di keranjang belanja, atau bahkan memastikan user tetap masuk ke akun user saat user berpindah halaman. Namun, perlu diingat bahwa penggunaan cookies harus sejalan dengan kebijakan privasi dan keamanan yang berlaku, serta memberikan kontrol kepada pengguna untuk menerima atau menolak penggunaan cookies.

## 4.Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Pada dasarnya, cookies tidak dianggap sebagai ancaman serius terhadap privasi dan keamanan website karena tidak menyimpan data pribadi secara langsung (meskipun terkadang dapat menyimpan nomor kartu kredit dan alamat IP) dan tidak dapat digunakan untuk menyebarkan malware atau virus. Namun, terdapat risiko potensial yang perlu diwaspadai terkait penggunaan cookies.

Salah satu risiko utama adalah privasi, terutama jika cookies digunakan untuk melacak aktivitas online pengguna tanpa persetujuan mereka. Cookies pihak ketiga, yang dimiliki oleh domain yang berbeda dari yang dijelajahi oleh pengguna, sering digunakan untuk tujuan pelacakan, iklan, dan analitik. Praktik ini dapat mengancam privasi pengguna dan meningkatkan risiko serangan phishing atau spam234.

Keamanan cookies menjadi isu penting karena penyimpanannya dalam bentuk teks. Hal ini membawa potensi risiko keamanan, di mana sebagian orang dapat membuka dan mengubah pengaturan cookies. Dampaknya bisa mencakup pencurian identitas, akses tanpa izin ke akun pengguna, atau manipulasi data.

Perlu diingat bahwa cookies tidak akan dapat berfungsi jika tingkat keamanan browser diatur tinggi. Ini dapat mengganggu kinerja situs web yang bergantung pada cookies untuk menyimpan preferensi pengguna, data sesi, atau informasi lain yang memperkaya pengalaman pengguna. Sehingga, penyeimbangan antara keamanan dan fungsionalitas situs web perlu diperhatikan dengan bijak.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
Untuk pengimpletasian fungsi registrasi, maka akan menggunakan UserCreationForm untuk pembuatan formulir. Pada views.py dibuat dulu userCreationForm nya lalu divalidasi dan disimpan. Setelah itu ditambahkan register.html dan tambahkan path url tersebut. 

Untuk pengimpletasian fungsi login, pertama kita mengimport authenticate yang digunakan untuk melakukan autentikasi dan login jika autentikasi berhasil. Lalu kita tinggak merequest untuk usernama dan password untuk di autentikasi pada login. Lalu buat login.html dan tambahkan url path nya. 

Untuk Logout maka akan digunakan sebuah fungsi log_out yang akan menerima parameter request. Saat fungsi menerima request maka sesi pengguna akan dihapus. 

Untuk membuat akun kita pertama-pertama registrasi dahulu, setelah diarahkan ke halaman registrasi isi username dan password dua kali. Setelah berhasil, maka akan diarahkan ke halaman untama. Untuk menambahkan produk kita tinggal menekan button "Add New Product" dan tulis nama, harga, dan deskripsi produk. Setelah selesai menambahkan produk maka poduk tersebut akan muncul di halaman main. Untuk keluar halaman, tinggal memencet button logout dan akan kembali ke halaman login. Jika ingin membuat akun lagi, ulangi lagi langkah-langkah tersebut dari awal dan jika ingin login kembali akun yang tadi, maka tinggal login dengan username dan password yang sudah dibuat. 

Untuk menghubungkan antara model product dengan user, di models.py ditambahkan "from django.contrib.auth.models import User" untuk mengelola data user dalam sistem autentikasi dan otorisasi. Lalu kita tambahkan potongan ForeignKey yang digunakan untuk menghubungkan satu produk dengan satu user melalui sebuah relationship. Kemudian, dalam views.py pada fungsi create_product, diterapkan parameter commit=False. Fungsi ini berperan untuk menghindari Django dari menyimpan objek yang dibuat dari formulir langsung ke database. Pengguna akan mengisi bidang pengguna (user) dengan objek User yang berasal dari nilai pengembalian request.user yang saat ini diotorisasi. Hal ini bertujuan untuk menunjukkan bahwa objek tersebut dimiliki oleh pengguna yang sedang masuk. Lalu pada show_main menambahkan Product.objects.filter(user=request.user) untuk mengumpulkan objek Product yang sesuai dengan pengguna yang sedang masuk, dan hasil ini akan disimpan dalam variabel dan lalu ditampilkan. Setelah selelsai tinggal memlakukan migrasi model.

Untuk menambahkan detail infomasi pengguna yang sedang logged in kita bisa menggunakan inspect elemen pada browser. Setelah membuka browser ke bagian application, maka cookie akan terlihat. 

## BONUS
untuk membuat bonus pertama-tama di views, saya menambahkan fungsi untuk menambah, mengurangi, dan menghapus produk. Untuk menambahkan, product tinggal dibuat =+ 1, untuk mengurangi -= 1, dan untuk menghapus menggunakan product.delete. Lalu kita melakukan routing untuk fungsi yang ada di views. Terakhir, di main.html kita tambahkan button untuk tambah, kurang, dan hapus produk.

## REFERENSI
https://dev.to/balt1794/registration-page-using-usercreationform-django-part-1-21j7
https://www.niagahoster.co.id/blog/cookies-adalah/

# TUGAS 5
## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Berikut adalah manfaat-manfaat dari element-elemen selector dan kapan untuk menggunakannya
- Element Selector
    Penggunaan Element Selector berdasarkan pada nama elemen HTML tersebut. Pemilih elemen ditulis dengan hanya menggunakan nama elemen HTML tanpa ada tambahan tanda seperti titik (.) atau pagar (#). Element selector memungkinkan untuk dapat menerapkan gaya secara global pada semua elemen dengan tipe tertentu. Element selector juga sangat sederhana dan intuitif, hanya perlu menentukan nama elemen dan mendefinisikan properti serta nilainya. Element selector membantu mengurangi pengulangan kode gaya di CSS, khususnya untuk elemen yang umum di situs web, seperti paragraf atau heading. Elemen Selector berguna ketika  ingin menerapkan gaya umum pada sekelompok elemen dengan tipe yang sama. Misalnya, saat ingin menerapkan gaya tertentu pada semua paragraf dalam halaman web atau pada semua elemen heading. 
- Class Selector
    Class Selector digunakan untuk memilih elemen HTML berdasarkan kelas yang diberikan pada elemen tersebut. Kelas dinyatakan dengan menggunakan tanda titik (.) sebelum nama kelas. Manfaat dari menggunakan class selector antara lain bisa untuk mengelompokkan elemen berdasarkan fungsionalitas atau gaya tertentu, menerapkan gaya yang sama pada banyak elemen di halaman web Anda hanya dengan memberikan kelas yang sama kepada elemen tersebut, dan memudahkan user untuk merencanakan dan menerapkan berbagai gaya dan tema secara konsisten pada elemen-elemen yang memiliki fungsionalitas atau penampilan yang mirip.
    Class Selector biasa digunakan ketika ingin menerapkan gaya yang sama pada beberapa elemen di halaman web dan ketika Anda ingin mengelompokkan elemen dengan tampilan yang sama. 
- ID Selector
    ID selector dalam CSS digunakan untuk memilih dan menerapkan gaya pada elemen HTML yang memiliki atribut ID tertentu. Beberapa manfaat dalam menggunakan adalah untuk  secara spesifik memilih satu elemen HTML dengan ID unik. Lalu juga untuk membuat ancor (bookmark) dalam halaman web dan membuat link ke bagian tertentu dalam satu halaman, dengan menggunakan atribut href yang berisi tanda “#” diikuti oleh nama id. ID selector sebaiknya digunakan ketika ingin memberikan gaya khusus pada elemen HTML yang hanya ada satu pada halaman atau ketika Anda membuat link ke bagian tertentu dalam satu halaman.

## 2. Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 tag adalah komponen fundamental dalam penulisan dokumen HTML versi 5, standar terbaru untuk web. Beberapa fitur-fitur utama HTML5 tag meliputi:

1. HTML5 tag seperti <audio>, <video>, dan <canvas> memungkinkan integrasi multimedia seperti suara, video, dan grafik tanpa memerlukan plugin tambahan.
2. HTML5 memperkenalkan tag-tag semantik baru seperti <article>, <section>, <header>, <footer>, <nav>, dan <aside>, yang membantu dalam mengorganisir struktur dan konten halaman web dengan lebih baik.
3. Tag seperti <br>, <img>, atau <input> tidak memerlukan penutup (/) dan dapat digunakan tanpa masalah, namun penutupan tetap opsional.
4. HTML5 tidak memerlukan atribut type untuk tag <script> dan <style>, karena secara default dianggap sebagai JavaScript dan CSS.
5. HTML5 mempermudah pendeklarasian DOCTYPE dengan menggunakan <!DOCTYPE html> di awal dokumen, menggantikan pendeklarasian DOCTYPE yang panjang.
Dengan HTML5, pengembang dapat menggunakan tag-tag yang lebih kaya fitur, lebih ekspresif, dan lebih mudah dimengerti, memungkinkan pengembangan web yang lebih dinamis dan modern.

## 3. Jelaskan perbedaan antara margin dan padding.
Perbedaan antara margin dan padding adalah sebagai berikut:
- Margin adalah ruang kosong di sekeliling elemen HTML, sementara padding adalah ruang kosong di dalam elemen HTML.
- Penggunaan margin adalah untuk mengatur jarak antara elemen dengan elemen lain atau tepi browser, sementara padding digunakan untuk mengatur jarak antara tepi elemen dan kontennya.
- Margin tidak mempengaruhi dimensi dari elemen itu sendiri, sedangkan padding dapat memperbesar atau memperkecil elemen tergantung pada nilainya.
- Pengaturan margin dapat berdampak pada tata letak keseluruhan situs web, karena dapat mengubah posisi elemen relatif terhadap elemen lain, sedangkan padding hanya mempengaruhi elemen yang memiliki padding.

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Bootstrap menawarkan set class CSS dan komponen yang telah dirancang sebelumnya dengan tampilan yang cukup terstruktur dan konsisten. Ini cocok untuk proyek dengan desain tradisional yang membutuhkan kerangka kerja yang stabil dan mudah digunakan. Tailwind menganut pendekatan yang lebih “utility-first”, di mana kita membangun antarmuka dengan menggabungkan class utilitas yang lebih kecil. Ini memberikan kebebasan kreatif yang lebih besar dan memungkinkan penggunaan class yang sangat spesifik.

Dalam hal fleksibilitas desain, Tailwind memberikan fleksibilitas yang lebih besar dengan pendekatan “utility-first” yang memungkinkan kita membangun desain yang sangat kustom sesuai kebutuhan. kita memiliki kendali penuh atas gaya dan tata letak dengan kombinasi class utilitas yang spesifik. Bootstrap menawarkan kerangka kerja yang relatif terstruktur dengan banyak komponen yang telah dirancang sebelumnya. Ini memberikan stabilitas dan kemudahan penggunaan, tetapi mungkin memiliki batasan dalam hal fleksibilitas desain yang unik.

Untuk pemilihan penggunaannya, jika Anda ingin membangun antarmuka dengan cepat menggunakan komponen siap pakai, Bootstrap mungkin menjadi pilihan terbaik. Namun, jika Anda ingin membangun antarmuka dengan desain khusus atau ingin mengoptimalkan performa halaman web Anda, Tailwind mungkin menjadi pilihan terbaik.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
# LOGIN
Untuk bagian login, saya menggunakan class selector dan element selector. Berikut penjelasannya untuk penggunaan class selector:
.login -> untuk gaya untuk elemen dengan kelas "login", termasuk warna latar belakang, padding, border-radius, dan bayangan kotak.
.login h1 -> untuk gaya untuk elemen <h1> yang berada di dalam elemen dengan kelas "login", termasuk ukuran font, margin bawah, dan pemusatannya.
.login table dan .login table td -> unutk gaya untuk tabel dan sel dalam tabel yang digunakan dalam formulir login, termasuk lebar tabel dan padding untuk sel.
.login input -> untuk gaya untuk elemen input dalam formulir, seperti lebar, padding, border, dan border-radius.
.login .login_btn -> untuk gaya untuk tombol login, termasuk warna latar belakang, warna teks, ukuran font.
.login .login_btn:hover -> untuk gaya untuk tombol login saat digerakkan (hover), seperti perubahan warna latar belakang.
.login .register_link -> untuk gaya untuk tautan yang mengarah ke halaman registrasi, termasuk penataan teks dan warna.

# REGISTER
Pada bagian register saya menggunakan external register dengan membuat file register.css. Di css tersebut saya menggunakan universal selector dan class selector. Untuk universal selectornya saya menggunakan di "*" dimana mempengaruhi semua elemen pada halaman. Pada kode tersebut, digunakan untuk mengatur properti box-sizing, margin, dan padding untuk semua elemen.
Lalu sisanya saya menggunakan class selector diantara lain :
.login -> Class ini mempengaruhi elemen dengan class "login". Properti-properti di dalamnya akan mempengaruhi tampilan kotak login.
.login h1 -> Class gabungan ini  mempengaruhi elemen <h1> yang berada di dalam elemen dengan class "login". Properti-properti di dalamnya akan mempengaruhi tampilan judul pada kotak login.
.login table -> Class yang mempengaruhi elemen tabel yang berada di dalam elemen dengan class "login". Properti width diatur menjadi 100% untuk tabel tersebut.
.login table td:first-child -> Class yang mempengaruhi sel pertama (<td>) dalam setiap baris tabel di dalam elemen dengan class "login". Properti text-align dan padding-right diatur untuk penataan teks dan jarak kanan pada sel pertama.
.login table input -> Selector gabungan yang mempengaruhi elemen input yang berada di dalam tabel di dalam elemen dengan class "login". Properti width diatur menjadi 80% untuk input tersebut.
.login table input[type="submit"] -> Selector gabungan yang mempengaruhi tombol submit yang berada di dalam tabel di dalam elemen dengan class "login". Properti-properti di dalamnya akan mempengaruhi tampilan tombol submit.
.login ul -> Selector class yang mempengaruhi elemen <ul> (daftar tak bernomor) yang berada di dalam elemen dengan class "login". Properti list-style-type diatur menjadi none untuk menghilangkan penomoran pada daftar tersebut.

# TAMBAH INVENTORI
Pada create_product.html saya menggunakan element selector dan class selector. Di element selector saya menggunakannya pada "body" Selector untuk elemen <body> pada halaman HTML. Properti-properti di dalamnya akan mempengaruhi tampilan seluruh halaman. Untuk Class selector saya menggunakannya pada:
.container -> class ini mempengaruhi elemen dengan class "container". Properti-properti di dalamnya akan mempengaruhi tampilan kontainer.
.container h1 -> class ini mempengaruhi elemen <h1> yang berada di dalam elemen dengan class "container". Properti-properti di dalamnya akan mempengaruhi tampilan judul dalam kontainer.
.form-table -> class yang mempengaruhi elemen dengan class "form-table". Properti-properti di dalamnya akan mempengaruhi tampilan tabel form.
.form-table td -> Class yang mempengaruhi sel (<td>) dalam tabel form. Isi dari class ini mempengaruhi padding untuk memberikan jarak antar sel. 
.form-table input[type="text"] dan .form-table input[type="number"] -> Class yang mempengaruhi input dengan tipe "text" dan "number" yang berada dalam tabel form. Isi di dalamnya akan mempengaruhi tampilan input tersebut.
.form-table input[type="submit"] -> Selector yang mempengaruhi tombol submit yang berada dalam tabel form. Properti-properti di dalamnya akan mempengaruhi tampilan tombol submit.
.form-table input[type="submit"]:hover -> Selector yang mempengaruhi tombol submit saat mouse diarahkan ke atasnya (hover). Properti-properti di dalamnya akan mempengaruhi tampilan tombol submit saat dihover.

# HAlAMAN INVENTORY
Pada halaman inventory atau main.html. Saya mengubah tampilan tabel menjadi lebih berwarna. Untuk selector yang saya gunakan adalah sebagai berikut :
- body -> Elemen <body> ini akan mempengaruhi tampilan seluruh halaman, termasuk properti seperti font-family, margin, padding, dan background-color.
- header -> Selector untuk elemen <header> yang mempengaruhi tampilan bagian header. Properti seperti background-color, color, text-align, padding, max-width, margin, dan border-radius digunakan untuk mengatur tampilan header.
- .container -> class yang mempengaruhi elemen dengan class "container". Properti padding dan text-align digunakan untuk mengatur tampilan konten dalam kontainer.
- table -> Selector untuk elemen <table> yang mempengaruhi tampilan tabel. Properti width, border-collapse, dan table-layout digunakan untuk mengatur tampilan tabel.
- th dan td -> Selector untuk elemen <th> (header kolom) dan <td> (sel) dalam tabel. Properti-properti seperti border, padding, text-align, background-color, dan color digunakan untuk mengatur tampilan header kolom dan sel dalam tabel.
- tr -> Selector untuk elemen <tr> (baris) dalam tabel. Properti padding dan background-color digunakan untuk mengatur tampilan baris dalam tabel.

Lalu saya juga menggunakan menambahkan bootstrap pada main.html. Saya menggunakannya di bagian navbar dan dropdown edit product. Untuk di navbar saya menambahkan fungsi untuk menampilkan nama user, edit product, dan log out. Untuk di drop-down saya menggunakannya pada bagian edit yang memunculkan fungsi tambah, kurang, hapus, dan edit produk.  


## REFERENSI
https://www.petanikode.com/css-selektor/
https://www.malasngoding.com/belajar-css-margin-dan-padding-pada-css/

    

