<template>
  <div>
    <h1>Select date range:</h1>
    <Datepicker v-model="date" range />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

const date = ref();
</script>