<template>
  <div
    class="flex h-screen bg-gray-50 dark:bg-gray-900"
    :class="{ 'overflow-hidden': LogicUI.isSideMenuOpen }"
  >
    <Sidebar />
    <div class="flex flex-col flex-1 w-full">
      <Header />
      <dashboard />
    </div>
  </div>
</template>

<script>
import { useLogicUI } from "../stores/index.js";
import Header from "../components/Header.vue";
import Sidebar from "../components/Sidebar.vue";
import dashboard from "./content/dashboard.vue";

export default {
  setup() {
    const LogicUI = useLogicUI();
    return {
      LogicUI,
    };
  },
  components: {
    Header,
    Sidebar,
    dashboard,
  },
};
</script>
