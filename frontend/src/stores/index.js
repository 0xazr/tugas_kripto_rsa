import { defineStore } from "pinia";
import axios from "axios";
import Swal from "sweetalert2";

const url = "http://127.0.0.1:5000";

export const useLogicUI = defineStore({
  id: "logicUI",
  state: () => ({
    isSideMenuOpen: false,
    isNotificationsMenuOpen: false,
    isProfileMenuOpen: false,
    isPagesMenuOpen: false,
    dark: false,
    expand: false,
  }),
  getters: {},
  actions: {
    toggleSideMenu() {
      this.isSideMenuOpen = !this.isSideMenuOpen;
    },
    togglePagesMenu() {
      this.isPagesMenuOpen = !this.isPagesMenuOpen;
    },
    closeSideMenu() {
      this.isSideMenuOpen = false;
    },
    toggleNotificationsMenu() {
      this.isNotificationsMenuOpen = !this.isNotificationsMenuOpen;
    },
    closeNotificationsMenu() {
      this.isNotificationsMenuOpen = false;
    },
    toggleProfileMenu() {
      this.isProfileMenuOpen = !this.isProfileMenuOpen;
    },
    closeProfileMenu() {
      this.isProfileMenuOpen = false;
    },
    toggleExpand() {
      this.expand = !this.expand;
      console.log(this.expand);
    },
  },
});

export const useAppData = defineStore({
  id: "logicAPP",
  state: () => ({
    tx_data: {
      nisn: "",
      nama_ibu: "",
    },
    loading: false,
  }),
  getters: {},
  actions: {
    async getData() {
      console.log("Getting data...");
      let that = this;
      this.loading = true;
      console.log(that.tx_data.nisn);
      console.log(that.tx_data.nama_ibu);
      try {
        fetch(url + "/api/nisn/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            nisn: that.tx_data.nisn,
            nama_ibu: that.tx_data.nama_ibu,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            Swal.fire({
              title: "Data Siswa",
              html: `
              <table class="table table-striped">
                <tr>
                  <td>NISN</td>
                  <td>${data.data[0].nisn}</td>
                </tr>
                <tr>
                  <td>Nama</td>
                  <td>${data.data[0].nama_siswa}</td>
                </tr>
                <tr>
                  <td>Tempat Lahir</td>
                  <td>${data.data[0].tempat_lahir}</td>
                </tr>
                <tr>
                  <td>Tanggal Lahir</td>
                  <td>${data.data[0].tanggal_lahir}</td>
                </tr>
                <tr>
                  <td>Jenis Kelamin</td>
                  <td>${data.data[0].jenis_kelamin}</td>
                </tr>
                <tr>
                  <td>Agama</td>
                  <td>${data.data[0].agama}</td>
                </tr>
                <tr>
                  <td>Alamat</td>
                  <td>${data.data[0].alamat}</td>
                </tr>
                `,
            });
          });
      } catch (error) {
        console.error("Error:", error);
      }
      this.loading = false;
    },
  },
});
