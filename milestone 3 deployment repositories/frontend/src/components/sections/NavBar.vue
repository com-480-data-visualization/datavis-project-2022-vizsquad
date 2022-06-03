<template>
  <nav class="navbar navbar-light bg-dark navbar-expand-lg fixed-top navbar-custom" id="mainNav" ref="navbar">
    <div class="container"><a class="navbar-brand" href="#page1" style="color: var(--bs-gray-100);">
      <img src="assets/img/epfl-logo-new.svg" style="padding-left: 16px;padding-right: 16px;height: auto;max-height: 20px; text-align: center;">
      VizSquad - CS-480 Data Visualization 2022</a>
      <button data-bs-toggle="collapse" data-bs-target="#navbarResponsive" class="navbar-toggler navbar-toggler-right" type="button" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fa fa-align-justify"></i></button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"></li>
          <li class="nav-item"><a class="nav-link" href="#page2" style="color: var(--bs-gray-100);">MOVEBANK</a></li>
          <li class="nav-item"><a class="nav-link" href="#portfolio" style="color: var(--bs-gray-100);">PIGEON STORY</a></li>
          <li class="nav-item"><a class="nav-link" href="#contact" style="color: var(--bs-gray-100);">OUR TEAM</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  mounted() {

  },
  methods: {

  }
}
</script>

<style scoped>
.navbar-other-pages {
  background-color: #42b983;
}
.navbar {
  text-align: center;
}
</style>

