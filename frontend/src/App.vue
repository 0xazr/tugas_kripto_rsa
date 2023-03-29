<template>
  <div class="h-screen md:flex">
    <div
      class="relative overflow-hidden md:flex w-1/2 bg-gradient-to-tr from-purple-700 to-blue-500 i justify-around items-center hidden"
    >
      <div class="mx-16 text-white">
        <h1 class="font-bold text-4xl font-sans mb-2">Check NISN</h1>
        <p class="mt-1">
          Nomor Induk Siswa Nasional adalah, kode pengenal identitas siswa yang
          bersifat unik, standar dan berlaku sepanjang masa yang dapat
          membedakan satu siswa dengan siswa lainnya di seluruh sekolah
          Indonesia dan Sekolah Indonesia di Luar Negeri; Nomor Induk Siswa
          Nasional (NISN) diberikan kepada setiap peserta didik yang bersekolah
          di satuan pendidikan yang memiliki NPSN dan terdaftar di Referensi
          Kemendikbud.
        </p>
        <div class="mt-1 duration-2" v-show="AppData.expand">
          Sistem pengelolaan NISN secara nasional oleh Pusat Data dan Statistik
          Pendidikan dan Kebudayaan (PDSPK) Kemendikbud yang merupakan bagian
          dari program Dapodik (Data Pokok Pendidikan) Kementerian Pendidikan
          dan Kebudayaan. Hasil dari proses pemberian kode identifikasi oleh
          PDSPK ditampilkan secara terbuka dalam batasan tertentu melalui situs
          NISN (http://nisn.data.kemdikbud.go.id./).

          <h1 class="font-bold text-xl mt-2">Tujuan dan Manfaat</h1>
          <ul class="ml-3 list-disc">
            <li>
              Untuk mengidentifikasi setiap individu siswa (peserta didik) di
              seluruh sekolah se-Indonesia secara standar, konsisten dan
              berkesinambungan.
            </li>
            <li>
              Sebagai pusat layanan sistem pengelolaan nomor induk siswa secara
              online bagi Unit unit Kerja di Kemendikbud, Dinas Pendidikan
              Daerah hingga Sekolah yang bersifat standar, terpadu dan akuntabel
              berbasis Teknologi Informasi dan Komunikasi terkini.
            </li>
            <li>
              Sebagai sistem pendukung program Dapodik dalam pengembangan dan
              penerapan program-program perencanaan pendidikan, statistik
              pendidikan dan program pendidikan lainnya baik di tingkat pusat,
              propinsi, kota, kabupaten hingga sekolah, seperti: Bantuan
              Operasional Sekolah (BOS), Ujian Nasional, PIP, SNMPTN.
            </li>
          </ul>
        </div>
        <button
          class="z-50 absolute w-28 bg-white text-indigo-800 mt-4 py-2 rounded-2xl font-bold mb-2"
          @click="AppData.toggleExpand()"
        >
          {{ AppData.expand ? "Hide" : "Read More" }}
        </button>
      </div>
      <div
        class="absolute -bottom-32 -left-40 w-80 h-80 border-4 rounded-full border-opacity-30 border-t-8"
      ></div>
      <div
        class="absolute -bottom-40 -left-20 w-80 h-80 border-4 rounded-full border-opacity-30 border-t-8"
      ></div>
      <div
        class="absolute -top-40 -right-0 w-80 h-80 border-4 rounded-full border-opacity-30 border-t-8"
      ></div>
      <div
        class="absolute -top-20 -right-20 w-80 h-80 border-4 rounded-full border-opacity-30 border-t-8"
      ></div>
    </div>
    <div class="flex md:w-1/2 justify-center py-10 items-center bg-white">
      <form class="bg-white w-4/6">
        <img
          class="h-20 w-20 object-cover rounded-full"
          src="./assets/nisn.png"
          alt="nisn"
        />
        <h1 class="text-gray-800 font-bold text-2xl mb-1">NISN</h1>
        <p class="text-sm font-normal text-gray-600 mb-7">
          Nomor Induk Siswa Nasional
        </p>
        <p class="text-m font-normal text-gray-600 mb-1">Masukkan NISN</p>
        <div class="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 22 22"
            stroke-width="1.5"
            stroke="currentColor"
            class="h-5 w-5 text-gray-400"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"
            />
          </svg>

          <input
            class="pl-2 outline-none border-none w-full border-transparent focus:border-transparent focus:ring-0"
            type="text"
            name=""
            id=""
            placeholder="NISN"
          />
        </div>
        <p class="text-m font-normal text-gray-600 mb-1">
          Masukkan Nama Ibu Kandung
        </p>
        <div class="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 text-gray-400"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
              clip-rule="evenodd"
            />
          </svg>
          <input
            class="pl-2 outline-none border-none w-full border-transparent focus:border-transparent focus:ring-0"
            type="text"
            name=""
            id=""
            placeholder="Nama Ibu Kandung"
          />
        </div>
        <button
          type="submit"
          class="block w-full bg-blue-600 mt-4 py-2 rounded-2xl text-white font-semibold mb-2"
        >
          Cari Data
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { useLogicUI, useAppData } from "./stores/index.js";

export default {
  setup() {
    const LogicUI = useLogicUI();
    const AppData = useAppData();
    return {
      LogicUI,
      AppData,
    };
  },
};
</script>
