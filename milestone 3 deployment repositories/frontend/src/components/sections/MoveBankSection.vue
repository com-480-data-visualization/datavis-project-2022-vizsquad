<template>
  <div class="section" id="move_section">
    <div id="treeselector-div" style="height: 20%">
      <TreeFoamSelectorTaxons/>
    </div>
    <div id="globe-div" style="height: 80%">
      <GlobeView/>
    </div>
  </div>
</template>

<script>
import TreeFoamSelectorTaxons from "@/components/TreeFoamSelectorTaxons";
import GlobeView  from "@/components/GlobeView";

export default {
  components: {
    TreeFoamSelectorTaxons,
    GlobeView
  },
  name: "MoveBankSection.vue",

  mounted() {

  }
}
</script>

<style scoped>
#move_section {
  /*padding-top: 50px;*/
}
</style>