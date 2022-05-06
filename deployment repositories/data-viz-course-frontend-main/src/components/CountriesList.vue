<template>
  <div>
    <h1>Select country:</h1>
    <multiselect
      mode="tags" 
      :searchable="true" 
      :multiple="true"
      :options="options">
    </multiselect>
  </div>
</template>  


<script>
  import Multiselect from '@vueform/multiselect'
  
  export default {
    name: 'CountriesList',
    components: { Multiselect },
    data () {
      return {
        selected: null,
        options: ['(all mock countries for now)', 'France', 'Ghana', 'Gabon', 'China', 'USA', 'Peru', 'Canada', 'Singapore']
      }
    }
  }
</script>

<style src="@vueform/multiselect/themes/default.css"></style>

<style scoped>

</style>