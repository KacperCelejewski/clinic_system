<template>
  <div id="app">
    <head>
      <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
        crossorigin="anonymous"
      />
      <title>Medicin</title>
    </head>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/"> Medicin </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item" :class="homeClass">
            <router-link class="nav-link" to="/"> Home </router-link>
          </li>
          <li class="nav-item" :class="addPatientClass">
            <router-link class="nav-link" to="/add-patient">
              Add patient
            </router-link>
          </li>
        </ul>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPath: this.$route?.path || "/",
    };
  },
  computed: {
    homeClass() {
      return this.currentPath === "/" ? "active" : "";
    },
    addPatientClass() {
      return this.currentPath === "/add-patient" ? "active" : "";
    },
  },
  watch: {
    $route(newRoute) {
      this.currentPath = newRoute.path;
    },
  },
};
</script>

<style>
#app {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
