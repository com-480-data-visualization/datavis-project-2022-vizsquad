<template>
  <div class="list-studies">
    <h1>Select studies:</h1>
    <Multiselect v-model="selected_studies" mode="tags" :searchable="true" :multiple="true" :options="study_options">
    </Multiselect>
  </div>
</template>

<script>
import Multiselect from '@vueform/multiselect'
// register globally

export default {
  components:{
    Multiselect
  },
  name: "StudiesList",
  data() {
    return {
      value: [],
    }
  },
  methods: {
    init_studies() {
    }
  },
  mounted() {
    this.init_studies();
  },
  computed: {
    study_options: {
      get() {
        if(this.$store.state.studies === undefined) {
          return [];
        }
        return this.$store.state.studies.map(study => {
          return {
            value: study.study_id,
            label: study.name
          };
        });
      }
    },
    selected_studies: {
      get() {
        if(this.$store.state.studies === undefined) {
          return [];
        }
        return this.$store.state.selected_studies;
      },
      set(value) {
        console.log("New selected studies", value)
        this.$store.dispatch("setSelectedStudies", value);
      }
    }
  }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>

<style scoped>

</style>