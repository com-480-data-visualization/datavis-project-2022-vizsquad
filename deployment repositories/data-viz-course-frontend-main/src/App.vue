<template>
  <div id="drop-down-container">
    <StudiesList/>
    <AnimalsList/>
    <CountriesList/>
    <DateRangePickerComponent/>
  </div>
  <div id="globe-container">
    <GlobeView/>
  </div>
</template>

<script>
import GlobeView  from "@/components/GlobeView";
import StudiesList from "@/components/StudiesList";
import AnimalsList from "@/components/AnimalsList";
import CountriesList from "@/components/CountriesList";
import DateRangePickerComponent from "@/components/DateRangePicker";

export default {
  name: 'App',
  components: {
    GlobeView,
    StudiesList,
    AnimalsList,
    CountriesList,
    DateRangePickerComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin: 20px;
  max-width: 90%;
}
#drop-down-container {
  padding: 20px;
}
#globe-container {
  padding: 20px;
  max-width: 80%;
}
</style>
