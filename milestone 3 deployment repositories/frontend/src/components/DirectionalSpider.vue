<!--<template>-->
<!--  <Radar :chart-data="chartData" />-->
<!--</template>-->


<!--<script>-->

<!--import {Radar} from 'vue-chartjs';-->
<!--import {Chart as ChartJS, Title, Tooltip, Legend, PointElement, RadialLinearScale, LineElement} from 'chart.js';-->
<!--ChartJS.register(Title, Tooltip, Legend, PointElement, RadialLinearScale, LineElement);-->

<!--export default {-->
<!--  name: "DirectionalSpider",-->

<!--  data() {-->
<!--    return {-->
<!--      chartData: {-->
<!--        labels: ["N", "NE", "E", "SE", "S", "SW", "W", "NW"],-->
<!--        datasets: [{-->
<!--          label: 'My First dataset',-->
<!--          backgroundColor: 'rgba(179,181,198,0.2)',-->
<!--          borderColor: 'rgba(179,181,198,1)',-->
<!--          pointBackgroundColor: 'rgba(179,181,198,1)',-->
<!--          pointBorderColor: '#fff',-->
<!--          pointHoverBackgroundColor: '#fff',-->
<!--          pointHoverBorderColor: 'rgba(179,181,198,1)',-->
<!--          data: [65, 59, 90, 81, 56, 55, 40, 45]-->
<!--        }, {-->
<!--          label: 'My Second dataset',-->
<!--          backgroundColor: 'rgba(255,99,132,0.2)',-->
<!--          borderColor: 'rgba(255,99,132,1)',-->
<!--          pointBackgroundColor: 'rgba(255,99,132,1)',-->
<!--          pointBorderColor: '#fff',-->
<!--          pointHoverBackgroundColor: '#fff',-->
<!--          pointHoverBorderColor: 'rgba(255,99,132,1)',-->
<!--          data: [28, 48, 0, 19, 96, 27, 100, 0]-->
<!--        }]-->
<!--      }-->
<!--    };-->
<!--  },-->
<!--  components : {-->
<!--    Radar-->
<!--  },-->

<!--  mounted() {-->
<!--    this.init_radar();-->
<!--  },-->
<!--  methods: {-->
<!--    init_radar() {-->
<!--     this.selected_studies_events-->
<!--    },-->

<!--    // Converts from degrees to radians.-->
<!--    toRadians(degrees) {-->
<!--      return (degrees * Math.PI) / 180;-->
<!--    },-->

<!--    // Converts from radians to degrees.-->
<!--    toDegrees(radians) {-->
<!--      return (radians * 180) / Math.PI;-->
<!--    },-->

<!--    bearing(startLat, startLng, destLat, destLng) {-->
<!--      startLat = this.toRadians(startLat);-->
<!--      startLng = this.toRadians(startLng);-->
<!--      destLat = this.toRadians(destLat);-->
<!--      destLng = this.toRadians(destLng);-->

<!--      var y = Math.sin(destLng - startLng) * Math.cos(destLat);-->
<!--      var x =-->
<!--        Math.cos(startLat) * Math.sin(destLat) - -->
<!--        Math.sin(startLat) * Math.cos(destLat) * Math.cos(destLng - startLng);-->
<!--      var brng = Math.atan2(y, x);-->
<!--      var brng = this.toDegrees(brng);-->
<!--      return (brng + 360) % 360;-->
<!--    },-->

<!--    //compute final angles-->
<!--    compute_angles_for_array_of_studies(studies_to_compute) {-->
<!--       for (let i = 1; i < studies_to_compute.length; i++) {-->
<!--         if (i == 0) {-->
<!--           //  block of code to be executed if the condition is true-->
<!--           var current_angle = 0;-->
<!--         } else {-->
<!--           var previous_lat = studies_to_compute[i - 1].location_lat;-->
<!--           var previous_long = studies_to_compute[i - 1].location_long;-->
<!--           var current_lat = studies_to_compute[i].location_lat;-->
<!--           var current_long = studies_to_compute[i].location_long;-->
<!--           var current_angle = this.bearing(-->
<!--             previous_lat,-->
<!--             previous_long,-->
<!--             current_lat,-->
<!--             current_long-->
<!--           );-->
<!--           //get direction-->
<!--           if (current_angle >= 22.5 && current_angle < 67.5) {-->
<!--             var current_direction = "NE";-->
<!--           } else if (current_angle >= 67.5 && current_angle < 112.5) {-->
<!--             var current_direction = "E";-->
<!--           } else if (current_angle >= 112.5 && current_angle < 157.5) {-->
<!--             var current_direction = "SE";-->
<!--           } else if (current_angle >= 157.5 && current_angle < 202.5) {-->
<!--             var current_direction = "S";-->
<!--           } else if (current_angle >= 202.5 && current_angle < 247.5) {-->
<!--             var current_direction = "SW";-->
<!--           } else if (current_angle >= 247.5 && current_angle < 292.5) {-->
<!--             var current_direction = "W";-->
<!--           } else if (current_angle >= 292.5 && current_angle < 337.5) {-->
<!--             var current_direction = "NW";-->
<!--           } else {-->
<!--             var current_direction = "N";-->
<!--           }-->
<!--           studies_to_compute[i].direction = current_direction;-->
<!--           studies_to_compute[i].angle = current_angle;-->
<!--         }-->
<!--       }-->
<!--       return studies_to_compute;-->
<!--    },-->
<!--    groupByKey(array, key) {-->
<!--      return array.reduce((hash, obj) => {-->
<!--        if (obj[key] === undefined) return hash;-->
<!--        return Object.assign(hash, {-->
<!--          [obj[key]]: (hash[obj[key]] || []).concat(obj),-->
<!--        });-->
<!--      }, {});-->
<!--    },-->

<!--    generate_groups(event_w_angles_and_direction) {-->
<!--      var events_grouped_by_id = this.groupByKey(-->
<!--        event_w_angles_and_direction,-->
<!--        "study_id"-->
<!--      );-->

<!--      console.log(events_grouped_by_id);-->
<!--      var study_ids_selected = Object.keys(events_grouped_by_id);-->
<!--      console.log("length " + study_ids_selected.length);-->
<!--      for (var i = 0; i < study_ids_selected.length; i++) {-->
<!--        console.log(i);-->
<!--        var study_id = study_ids_selected[i];-->
<!--        console.log("Computing directection for study " + study_id);-->
<!--        var study_events = events_grouped_by_id[study_id];-->

<!--        var direction_counts = {};-->
<!--        for (var i = 0; i < study_events.length; i++) {-->
<!--          var current_dir = study_events[i].direction;-->
<!--          if (Object.keys(direction_counts).includes(current_dir)) {-->
<!--            direction_counts[current_dir] += 1;-->
<!--          } else if (current_dir != undefined) {-->
<!--            direction_counts[current_dir] = 1;-->
<!--          }-->
<!--        }-->
<!--        console.log(direction_counts);-->
<!--      }-->
<!--      -->
<!--      -->
<!--      -->
<!--    },-->
<!--    check_if_data_downloaded_already(study_to_get, events) {-->
<!--      var items = events;-->

<!--      for (var item, i = 0; item = items[i++];) {-->
<!--        if (study_to_get == item.study_id) {-->
<!--          return true-->
<!--        } else {-->
<!--          return false-->
<!--        }-->
<!--}-->
<!--    },-->
<!--  },-->
<!--  computed: {-->
<!--    events: {-->
<!--      get() {-->
<!--        return this.$store.state.events;-->
<!--      },-->
<!--    },-->
<!--    selected_studies: {-->
<!--      get() {-->
<!--        return this.$store.state.selected_studies;-->
<!--      },-->
<!--    },-->
<!--    selected_studies_events: {-->
<!--      get() {-->
<!--        const selectedStudies = this.$store.state.selected_studies;-->
<!--        const events = this.$store.state.events;-->
<!--        const filtered_events = events.filter((event) =>-->
<!--          selectedStudies.includes(event["study_id"] == selectedStudies[0] || selectedStudies[1])-->
<!--        );-->
<!--        //console.log("filtered_events", filtered_events)-->

<!--        // group by individual_id and thus by study_id too)-->
<!--        const grouped_events = this.groupByKey(filtered_events, "individual_id");-->
<!--        console.log("grouped_events", grouped_events)-->

<!--        // compute distances and angles per group of individuals in grouped_events-->


<!--        // flatten the array-->
<!--        // merge values in the format required by the chart-->
<!--        // plot in the chart-->

<!--        // group by study_id and individual_id-->
<!--        Object.keys(grouped_events).forEach(function (key) {-->
<!--          function groupByKey(array, key) {-->
<!--            return array.reduce((hash, obj) => {-->
<!--              if (obj[key] === undefined) return hash;-->
<!--              return Object.assign(hash, {-->
<!--                [obj[key]]: (hash[obj[key]] || []).concat(obj),-->
<!--              });-->
<!--            }, {});-->
<!--          }-->
<!--          //console.log(grouped_events[key]);-->
<!--          grouped_events[key] = groupByKey(-->
<!--            grouped_events[key],-->
<!--            "individual_id"-->
<!--          );-->
<!--        });-->
<!--        //grouped_events here the events grouped by study_id and individual_id-->
<!--        //console.log("grouped_events", grouped_events);-->
<!--        return grouped_events;-->
<!--        //const event_with_angles_and_direction =-->
<!--        //  this.compute_angles(filtered_events);-->
<!--        //return this.generate_groups(event_with_angles_and_direction);-->
<!--      },-->
<!--    },-->
<!--  },-->
<!--  watch: {-->
<!--    selected_studies(newSelectedStudies, oldSelectedStudies) {-->
<!--      newSelectedStudies.forEach((study) => {-->
<!--        if (!oldSelectedStudies.includes(study)) {-->
<!--          //this.$store.dispatch("fetchEvents", study);-->
<!--          this.init_radar()-->
<!--        }-->
<!--      });-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->



<!--<style scoped>-->
<!--</style>-->