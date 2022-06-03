<template>
  <div></div>
</template>

<script>
import {difference} from "lodash";

export default {
  name: "DataLoader",
  methods: {
    init_data() {
      this.$store.dispatch("fetchStudies");
      this.$store.dispatch("fetchTaxons");
      this.$store.dispatch("fetchPigeonData");
      this.$store.dispatch("fetchPigeonSpiderData");

    }
  },
  mounted() {
    this.init_data();
  },
  computed: {
    selected_studies: {
      get() {
        return this.$store.state.selected_studies;
      }
    },
  },
  watch: {
    selected_studies(newSelectedStudies, oldSelectedStudies) {
      difference([...newSelectedStudies], [...oldSelectedStudies]).forEach(new_study_set => {
          new_study_set.forEach(study_id => {
            this.$store.dispatch("fetchEvents", study_id);
          });
      })
    }
  }
}
</script>

<style scoped>

</style>