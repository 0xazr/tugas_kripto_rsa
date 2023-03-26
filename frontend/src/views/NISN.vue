<template>
    <div>
        <nav class="navbar static-top">
            <div class="container">
                <a class="navbar-brand" href="https://nisn.data.kemdikbud.go.id/">
                    <img src="https://nisn.data.kemdikbud.go.id/assets/images/icon_nisn.png" height="50px">
                </a>
                <span class="pull-right">
                    
                </span>
            </div>
        </nav>
        <header class="masthead text-white">
            <div class="overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-lg-5 col-md-5 col-sm-12 col-xs-12" style="padding-top: 2em">
                        <h2>Pencarian NISN</h2>
                        <div>
                            <input id="token_id" name="token_id" type="hidden" value="" data-validation="required">
                            <div class="form-group has-feedback">
                                <label for="nisn">Masukkan NISN</label>
                                <input id="nisn" name="nisn" type="text" v-model="appData.tx_data.nisn" minlength="10" maxlength="10" class="form-control form-control-lg" placeholder="NISN" data-validation="required">
                            </div>
                            <div class="form-group has-feedback">
                                <label for="nisn">Masukkan Nama Ibu Kandung</label>
                                <input id="nama_ibu_kandung" name="nama_ibu_kandung" type="text" v-model="appData.tx_data.nama_ibu" minlength="3" maxlength="100" class="form-control form-control-lg" placeholder="Nama Ibu Kandung" data-validation="required">
                            </div>
                            <div class="form-group has-feedback">
                                <div class="g-recaptcha" data-sitekey="6LeUUlAaAAAAALQuMSC4MZq0idzmaQYuJ24mRSVY"></div>
                            </div>
                            <div class="form-group has-feedback">
                                <button type="submit" @click="appData.getData" class="btn btn-block btn-lg btn-default" data-toggle="modal" data-target="#exampleModal">Cari Data</button>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-7 col-md-7 col-sm-12 col-xs-12" style="font-size: 17px;padding-top: 1em;padding-bottom: 4em">
                        <h4>Pengantar</h4>
                        <ol>
                            <li>Pengertian Nomor Induk Siswa Nasional adalah, kode pengenal identitas siswa yang bersifat unik, standar dan berlaku sepanjang masa yang dapat membedakan satu siswa dengan siswa lainnya di seluruh sekolah Indonesia dan Sekolah Indonesia di Luar Negeri; Nomor Induk Siswa Nasional (NISN) diberikan kepada setiap peserta didik yang bersekolah di satuan pendidikan yang memiliki NPSN dan terdaftar di Referensi Kemendikbud. Sistem pengelolaan NISN secara nasional oleh Pusat Data dan Statistik Pendidikan dan Kebudayaan (PDSPK) Kemendikbud yang merupakan bagian dari program Dapodik (Data Pokok Pendidikan) Kementerian Pendidikan dan Kebudayaan. Hasil dari proses pemberian kode identifikasi oleh PDSPK ditampilkan secara terbuka dalam batasan tertentu melalui situs NISN (<a style="color: white" href="https://nisn.data.kemdikbud.go.id/" target="_blank">http://nisn.data.kemdikbud.go.id./</a>).
                            </li>
                            <li>Tujuan dan Manfaat
                                <ul>
                                    <li>Mengidentifikasi setiap individu siswa (peserta didik) di seluruh sekolah se-Indonesia secara standar, konsisten dan berkesinambungan.</li>
                                    <li>Sebagai pusat layanan sistem pengelolaan nomor induk siswa secara online bagi Unit unit Kerja di Kemendikbud, Dinas Pendidikan Daerah hingga Sekolah yang bersifat standar, terpadu dan akuntabel berbasis Teknologi Informasi dan Komunikasi terkini.</li>
                                    <li>Sebagai sistem pendukung program Dapodik dalam pengembangan dan penerapan program-program perencanaan pendidikan, statistik pendidikan dan program pendidikan lainnya baik di tingkat pusat, propinsi, kota, kabupaten hingga sekolah, seperti: Bantuan Operasional Sekolah (BOS), Ujian Nasional, PIP, SNMPTN.</li>
                                </ul>
                            </li>
                        </ol>
                        <h4>Verval Lulusan</h4>
                        <ul>
                            <li>Untuk Verifikasi dan Validasi NISN Siswa yang sudah <b>lulus</b> silahkan klik <a style="color:white" href="http://pd.data.kemdikbud.go.id/index.php?r=pengajuan/PengajuanLulusan" target="_blank"><b>disini</b></a>.</li>
                        </ul>
                        <h4>Verval Lulusan Sekolah Luar Negeri (Non SILN)</h4>
                        <ul>
                            <li>Untuk Verifikasi dan Validasi NISN Siswa yang sudah <b>lulus dari sekolah luar negeri (Non SILN)</b> silahkan klik <a style="color:white" href="http://pd.data.kemdikbud.go.id/index.php?r=pengajuan/PengajuanLulusanLN" target="_blank"><b>disini</b></a>.
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </header>
    </div>		
</template>
<script>
import { useAppData } from '@/stores';

export default {
    setup() {
        const appData = useAppData();
        return {
            appData
        };
    },
};
</script>