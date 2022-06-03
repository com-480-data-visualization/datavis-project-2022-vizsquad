<template>
  <div class="list-animals">
    <h1>Select animals:</h1>
    <Multiselect v-model="animals_selected" mode="tags" :searchable="true" :multiple="true" :options="animal_options">
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
  name: "AnimalsList",
  data() {
    return {
    }
  },
  methods: {
    init_animals() {
      this.$store.dispatch("fetchAnimals");
    }
  },
  mounted() {
    this.init_animals();
  },
  computed: {
    animal_options: {
      get() {
        if(this.$store.state.animals === undefined) {
          return [];
        }
        return this.$store.state.animals.map(animal => {
          return {
            value: animal.id,
            label: animal.name
          };
        });
      }
    },
    animals_selected: {
      get() {
        return this.$store.state.animals_selected;
      },
      set(value) {
        this.$store.commit("setSelectedAnimals", value);
      }
    }
  }
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>

<style scoped>

</style>