import telebot
import os
from os import environ
from telebot import types


BOT_TOKEN = environ['BOT-TOKEN'] #'1737660531:AAG0dmz1zcmaz0kBBGMKessuqzAh1iaz3sU' #
bot = telebot.TeleBot(BOT_TOKEN)

# menu command 
@bot.message_handler(commands=['start', 'help', 'MENU_UTAMA'])
def send_welcome(message):
    nama_user = message.from_user.first_name + " " + message.from_user.last_name

    bot.reply_to(message, "Halo {} ,Selamat datang di chatbot informasi SMKN 1 Mas Ubud, Informasi apa yang kamu butuhkan? 😊".format(nama_user))
    markup_awal = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Visi dan Misi')
    itembtn2 = types.KeyboardButton('Jurusan')
    itembtn3 = types.KeyboardButton('Pencapaian Sekolah')
    itembtn5 = types.KeyboardButton('SPP')
    itembtn6 = types.KeyboardButton('Tata Tertib Sekolah')
    itembtn7 = types.KeyboardButton('Kontak Sekolah')
    markup_awal.add(itembtn1, itembtn2, itembtn3, itembtn5, itembtn6, itembtn7)
    bot.send_message(message.chat.id, "Pilih salah satu : ", reply_markup=markup_awal)

# kembali ke menu utama
def ke_menu_utama(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Kembali ke menu utama? --> /MENU_UTAMA', reply_markup=markup)

#list command informasi
@bot.message_handler(content_types=['text'])
def menu_utama(message):
    #list jurusan
    if(message.text == 'Jurusan'):
        nama_user = message.from_user.first_name + " " + message.from_user.last_name
        bot.reply_to(message, '''
            Halo {} , Berikut adalah seluruh jurusan yang ada di Sekolah kami, 
            1. Rekayasa Perangkat Lunak (RPL)
            2. Teknik Komputer Jaringan (TKJ)
            3. Multimedia (MM)
            4. Akuntansi (AK)
            5. Akomodasi Perhotelan (AP)
            6. Tata Kecantikan Rambut (TKR) '''
        .format(nama_user))

        markup_list_jurusan = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('RPL')
        itembtn2 = types.KeyboardButton('TKJ')
        itembtn3 = types.KeyboardButton('MM')
        itembtn4 = types.KeyboardButton('AK')
        itembtn5 = types.KeyboardButton('AP')
        itembtn6 = types.KeyboardButton('TKR')
        markup_list_jurusan.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

        bot.send_message(message.chat.id, "Pilih salah satu : ", reply_markup=markup_list_jurusan)
    #RPL
    elif(message.text == 'RPL'):
        bot.reply_to(message, 
        '''
            RPL adalah sebuah jurusan yang mempelajari dan mendalami semua cara-cara pengembangan perangkat lunak termasuk pembuatan, 
            pemeliharaan, manajemen organisasi pengembangan perangkat lunak dan manajemen kualitas. Bukan hanya itu, RPL juga berkaitan 
            dengan software komputer mulai dari pembuatan website, aplikasi, game dan semua yang berkaitan dengan pemrograman dengan 
            menguasai bahasa pemrograman tersebut. Intinya RPL tidak akan jauh-jauh dari tiga hal yaitu Coding, Desain dan Algoritma 
            yang akan menjadi kunci keberhasilan rekayasa perangkat lunak tersebut.

            Yang Dipelajari Di Jurusan RPL:
            1)	Coding
            -	Pemograman Bahasa Pascal
            -	Pemograman Bahasa C
            -	Pemograman Bahasa C++
            -	Pemograman Bahasa Java
            -	Pemograman Bahasa Python (*)
            -	Pemograman Bahasa Delphi (*)
            -	Pemograman PHP & Mysql
            -	Pemograman JavaScript
            -	Pemograman AJAX (*)
            -	Pemograman Web Server
            -	Pemograman HTML
            -	Pemograman CSS
            -	Dan masih banyak lagi

            2)	Desain
            -	Photoshop
            -	Corel Draw
            -	Video Editing
            -	Web Design
            -	Dan masih banyak lagi

            3)	Algoritma
            -	Algoritma Dasar
            -	Algoritma tingkat Lanjut
            -	Microsoft Access
            -	Gerbang Logika
            -	Basis Data
            -	DFD (Data Flow Diagram)
            -	Dan masih banyak lagi


            Peluang Dalam Bekerja:
            - Konfersi PSD ke WordPress
            - Developer IT
            - Programmer
            - IT Consultant
            - System Analyst dan System Integrator
            - Database Engineer/ Database Administrator
            - Web Engineer

    
        '''
        )
        ke_menu_utama(message)
    #TKJ
    elif(message.text == 'TKJ'):
        bot.reply_to(message, 
        '''
        TKJ adalah singkatan dari Teknik Komputer Jaringan. TKJ merupakan sebuah kejurusan yang mempelajari tentang cara-cara merakit komputer dan menginstalasi program komputer. Jurusan TKJ sangatlah mudah untuk dipelajari hanya modal kemauan untuk belajar. Banyak siswa yang awalnya tidak tahu apa itu TKJ, tapi setelah sekolah di jurusan ini siswa jadi banyak tahu mengenai bagaimana memperbaiki PC, menginstalasi Jaringan LAN maupun yang lainnya.

        Yang Akan Dipelajari Dalam Jurusan Ini :
            1)	Komputer Dan Jaringan Dasar
            Sesuai dengan nama jurusannya, maka Kamu pun akan diajari tentang perihal komputer dan jaringan dasarnya. Mulai dari materi hardware, perkembangan jaringan, hingga bagian-bagian lainnya.
            2)	Pemrograman Dasar
            Bagi Kamu yang mengenyam pendidikan di TKJ, maka Kamu juga harus memahami apa itu pemrograman. Ilmu yang berisi coding untuk sebuah operasi komputer ini memungkinkanmu mempelajari banyak hal.
            3)	Teknologi Jaringan Berbasis Luas
            Salah satu mata pelajaran TKJ yang wajib Kamu ketahui dan wajib Kamu kuasai adalah Teknologi Jaringan Berbasis Luas. Mata pelajaran ini bisa dibilang cukup sulit bahkan untuk mereka yang menguasainya. Pasalnya di Teknologi Jaringan Berbasis Luas, Kamu akan belajar soal diagnosa kerusakan komputer, perbaikannya, hingga pembuatan jaringan seperti LAN, WAN, atau internet.
            4)	Administrasi Infrastruktur Jaringan
            Di mata pelajaran ini, Kamu juga akan digembleng dengan banyak macam konfigurasi jaringan, sebut saja Cisco, Mikrotik, dan jaringan-jaringan lainnya. Selain itu, Kamu juga akan belajar tentang konfigurasi server dimana Kamu dipersiapkan menjadi seorang administrator jaringan entah itu di perusahaan besar atau kecil.
            5)	Simulasi Dan Komunikasi Digital
            Proses meniru bentuk visual yang dideskripsi dalam model gambar, grafis, atau kata ini juga akan Kamu pelajari di TKJ. Oleh sebab itu, Kamu harus benar-benar mahir dalam bidang analitik agar Kamu dapat memahami perilaku dari suatu sistem itu sendiri.
            6)	Desain Grafis
            Di mata pelajaran ini, Kamu akan belajar cara mendesain dalam bentuk grafis. Ilmu ini sangat penting dan berguna bahkan ketika Kamu lulus nanti.
            7)	Administrasi Sistem Jaringan
            Disini, Kamu akan belajar soal Sistem Operasi beserta proses instalasinya. Biasanya, OS ini memungkinkan untuk melayani banyak service, mulai dari pinter, HTTP, hingga DNS Service.
            8)	Teknologi Layanan Jaringan
            Tentunya, mengambil jurusan TKJ membuatmu harus juga belajar Teknologi Layanan Jaringan. Disini, Kamu akan belajar mengenai apa saja layanan yang dirancang dan dibangun dengan tujuan untuk melayani pengguna meski dari banyak perangkat yang berbeda.
            9)	Produk Kreatif Dan Kewirausahaan
            Belajar di jurusan TKJ bukan berarti Kamu tidak bisa berwirausaha. Pasalnya di mata pelajaran ini, Kamu akan diajari soal kreativitas dan wirausaha sehingga bisa Kamu jadikan modal untuk kedepannya.
            10)	Pengetahuan Dasar
        Terakhir, Kamu pun akan belajar mengenai berbagai mata pelajaran dasar layaknya di SMA. Contohnya saja Matematika, Bahasa Indonesia, hingga Bahasa Inggris dan Agama.

        Peluang Dalam Bekerja:
        Dari segi peluang kerja setelah lulus sangat banyak peluangnya. Mulai dari menjadi teknisi komputer, teknisi jaringan, membuka toko komputer, atau bisa juga membuka warnet sendiri
        '''
        )
        ke_menu_utama(message)
    #MM
    elif(message.text == 'MM'):
        bot.reply_to(message, 
        '''
            Jurusan Kecantikan adalah jurusan bidang studi pariwisata. Dimana kopetensi yang dimiiki oleh peserta didik meliputi perawatan, seni menghias dan merubah. adapun unsur perawatan yaitu perawatan wajah, perawatan tangan dan kaki, perawatan badan dan perawatan rambut. seni menghias yaitu tata rias wajah khusus dan kreatif, nail art, henna art, up styling dan hair colouring. Serta seni merubah seperti Pemangkasan rambut, pelurusan dan pengeritingan rambut. 

            Peluang profesi yang dapat dimiliki oleh lulusan Tata Kecantikan :
            -	MakeUp Artist
            -	Hair Dresser
            -	Beautycian
            -	Beauty Consultant
            -	Beauty Advisor.

    
        '''
        )
        ke_menu_utama(message)
    #AK
    elif(message.text == 'AK'):
        bot.reply_to(message,
        '''
        Jurusan akuntansi ialah belajar cara memelihara keuangan. Ini mempersiapkan siswa untuk menjadi akuntan dengan mengajar mereka tentang prinsip-prinsip akuntansi seperti audit, pelaporan, penganggaran dan peraturan pajak. Akuntansi adalah sarana yang digunakan perusahaan atau organisasi untuk menyampaikan informasi keuangannya. Mempelajari akuntansi mencakup pembelajaran tentang keuangan, pelaporan informasi keuangan organisasi, dan akuntansi manajerial. Penggunaan data itu untuk mengukur kinerja entitas dan menginformasikan keputusan tentang masa depan dan kontrolnya. Jurusan akuntansi mempelajari bagaimana catatan keuangan perusahaan disiapkan dan dipelihara. Ia mempelajari perpajakan, audit, dan pelaporan keuangan.
 
        '''
        )
        ke_menu_utama(message)
    #AP
    elif(message.text == 'AP'):
        bot.reply_to(message, 
        '''
            Jurusan ini mempelajari tentang tata cara menjalankan dan menyediakan layanan di dunia pariwisata. Lulusannya akan menjadi sumber daya manusia di berbagai perusahaan bidang pariwisata dan layanan. Baik itu hotel, restoran, tempat wisata, pemandu wisata, dan lain sebagainya.
        '''
        )
        ke_menu_utama(message)
    #TKR
    elif(message.text == 'TKR'):
        bot.reply_to(message, 
        '''
            Jurusan Kecantikan adalah jurusan bidang studi pariwisata. Dimana kopetensi yang dimiiki oleh peserta didik meliputi perawatan, seni menghias dan merubah. adapun unsur perawatan yaitu perawatan wajah, perawatan tangan dan kaki, perawatan badan dan perawatan rambut. seni menghias yaitu tata rias wajah khusus dan kreatif, nail art, henna art, up styling dan hair colouring. Serta seni merubah seperti Pemangkasan rambut, pelurusan dan pengeritingan rambut. 

            Peluang profesi yang dapat dimiliki oleh lulusan Tata Kecantikan :
            -	MakeUp Artist
            -	Hair Dresser
            -	Beautycian
            -	Beauty Consultant
            -	Beauty Advisor.

    
        '''
        )
        ke_menu_utama(message)

    #Visi dan Misi Sekolah
    elif(message.text == 'Visi dan Misi'):
        bot.reply_to(message,
        '''
        VISI: Terwujudnya sekolah yang dapat menciptakan SDM yang Trampil, Mandiri, Produktif dan Profesional.

        MISI:
        1. Menyelenggarakan diklat kejuruan yang berwawasan mutu dan keunggulan sesuai kebutuhan pasar.
        2. Melaksanakan diklat Normatif, Adaftif, dan Produktif untuk meningkatkan pengetahuan, sikap dan keterampilan bagi peserta didik.
        3. Menumbuhkan bakat kreatifitas semangat keunggulan kompetitif guna menghadapi tantangan kehidupan di Era Globalisasi.
        4. Mengolah potensi daerah menjadi aset potensial
        '''
        )
        ke_menu_utama(message)
    #Pencapaian Sekolah
    elif(message.text == 'Pencapaian Sekolah'):
        bot.reply_to(message, 
        '''
            Prestasi dan Pencapaian Sekolah

        '''
        )
        ke_menu_utama(message)
    #SPP
    elif(message.text == 'SPP'):
        bot.reply_to(message, 
        '''
            Informasi SPP Sekolah

        '''
        )
        ke_menu_utama(message)
    #Tata Tertib Sekolah
    elif(message.text == 'Tata Tertib Sekolah'):
        bot.reply_to(message, 
        '''
            Tata Tertib Sekolah

        '''
        )
        ke_menu_utama(message)
    #Kontak Sekolah
    elif(message.text == 'Kontak Sekolah'):
        bot.reply_to(message, 
        '''
            Alamat		: Jl. Ambarwati No.1 No.320, MAS, Kecamatan Ubud, Kabupaten Gianyar, Bali 80571
            Phone		: 0361971518
            Email		: info@smkn1mas.sch.id
        '''
        )
        ke_menu_utama(message)
    #jika tidak ada pada list command
    else:
        bot.reply_to(message,
        '''
            Maaf, pesan yang anda kirimkan tidak ada dalam list command bot, mohon kirim pesan sesuai pilihan command yang tersedia
            Kembali ke menu utama untuk melihat list command
        '''
        )
        ke_menu_utama(message)

print("--- bot sedang berjalan ---")
bot.polling()


