import { defineStore } from "pinia";
import axios from "axios";

const url = "http://127.0.0.1:5000";

export const useLogicUI = defineStore({
  id: "logicUI",
  state: () => ({
    isSideMenuOpen: false,
    isNotificationsMenuOpen: false,
    isProfileMenuOpen: false,
    isPagesMenuOpen: false,
    dark: false,
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
  },
});

export const useAppData = defineStore({
  id: "logicAPP",
  state: () => ({
    tx_data: {
      name: "",
      age: 0,
      email: "",
    },
    loading: false,
  }),
  getters: {},
  actions: {
    async insertData() {
      console.log("Inserting data...");
      let that = this;
      this.loading = true;
      try {
        await axios
          .post(url + "/add", {
            name: that.tx_data.name,
            age: that.tx_data.age.toString(),
            email: that.tx_data.email,
          })
          .then((res) => {
            console.log(res.data);
          });
        this.tx_data.name = "";
        this.tx_data.age = "";
        this.tx_data.email = "";
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
    async getData() {
      console.log("Getting data...");
      let that = this;
      this.loading = true;
      try {
        await axios.get(url + "/get").then((res) => {
          console.log(res.data.data);
        });
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  },
});
