<template>
  <div ref="canvasContainer" id="canvasContainer" class="globe-view"></div>

</template>

<script>

import Globe from 'globe.gl'
import {groupBy} from "lodash";


export default {
  name: "GlobeView",

  data() {
    return {
      globe_texture_selector: "monthly",
      globe_maximum_zoom_out: 1.6
    }
  },

  methods: {

    init_globe() {
      console.log("init_globe");
      this.globe = new Globe();
      this.globe(this.$refs.canvasContainer).height(document.getElementById('canvasContainer').clientHeight * 0.75)
      this.globe.onZoom((coords) => {
        coords.altitude = Math.min(coords.altitude, this.globe_maximum_zoom_out);
        this.globe.pointOfView(coords);
      });
      this.update_globe_texture()
    },
    update_globe_texture() {
      if (this.globe_texture_selector === "monthly") {
        this.globe.globeImageUrl(`./assets/img/globe/${this.globe_texture_selector}/${this.selected_month}.jpg`)
            .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
            .polygonsData([])

      } else if (this.globe_texture_selector === "countries") {

        fetch('/assets/img/globe/countries/countries.geojson').then(res => res.json()).then(countries => {
          this.globe.globeImageUrl('//unpkg.com/three-globe/example/img/earth-dark.jpg')
              .polygonsData(countries.features.filter(d => d.properties.ISO_A2 !== 'AQ'))
              .polygonStrokeColor(() => '#000000')
        });
      }
    },

    update_texture_selector(texture_selector) {
      this.globe_texture_selector = texture_selector;
      document.getElementById('countries-btn').classList.remove("active");
      document.getElementById('monthly-btn').classList.remove("active");
      document.getElementById(`${texture_selector}-btn`).classList.add("active");
      this.update_globe_texture();
    },

    update_globe_paths(selected_studies_events) {

      let flattened_events = []
      selected_studies_events.forEach(selected_studies => {
        if (selected_studies.events && selected_studies.events.length > 0 && selected_studies.events[0]) {
          flattened_events.push(...(selected_studies.events))
        }
      })
      const flattened_filtered = flattened_events.filter(element => {
        return element && element.length > 0;
      }).flat();
      if(flattened_filtered.length <= 0) {
        return;
      }
      console.log(flattened_filtered, "flattened_filtered");
      this.globe.pathsData(flattened_filtered)
          .pathPointLat((d) => {return d["location_lat_extrapolated"]})
          .pathPointLng((d) => {return d["location_long_extrapolated"]})
          .pathStroke(3).pathDashLength(0.01).pathDashGap(1-0.01).pathDashAnimateTime(1000000)

      // if (flattened_events.length > 0){
      //   if (flattened_events[0].length > 0) {
      //     this.globe.pointOfView({"lng": flattened_events[0][0]["location_long_extrapolated"], "lat": flattened_events[0][0]["location_lat_extrapolated"], "altitude": 1.2}, 2000);
      //   }
      // }
    }

    //   let group_by_individual_id = events.reduce(function (r, a) {
    //     r[a.individual_id] = r[a.individual_id] || [];
    //     r[a.individual_id].push(a);
    //     return r;
    //   }, Object.create(null));
    //
    //   let paths = [];
    //   for (let individual_id in group_by_individual_id) {
    //     let tag_events = group_by_individual_id[individual_id];
    //     paths.push(tag_events);
    //   }
    //   this.globe.pathsData(paths)
    //       .pathPointLat((d) => d["location_lat_extrapolated"])
    //       .pathPointLng((d) => d["location_long_extrapolated"])
    //       .pathPointAlt(0)
    //       .pathColor(() => ['rgba(0,0,255,1.0)', 'rgba(255,0,0,1.0)'])
    //       .pathStroke(3).pathDashLength(0.01).pathDashGap(1-0.01).pathDashAnimateTime(10000)
    //   if (paths.length > 0){
    //     if (paths[0].length > 0) {
    //       this.globe.pointOfView({"lng": paths[0][0]["location_long_extrapolated"], "lat": paths[0][0]["location_lat_extrapolated"], "altitude": 1.5}, 2000);
    //     }
    //   }
    // }
  },
  mounted() {
    this.init_globe();
  },
  computed: {
    events: {
      get() {
        return this.$store.state.events;
      }
    },
    selected_studies: {
      get() {
        return this.$store.state.selected_studies;
      }
    },
    selected_month: {
      get() {
        let date = this.$store.state.selected_date;
        return date.getMonth();
      }
    },
    selected_events_per_study: {
      get() {
        let events = this.$store.state.events;
        let selected_studies = this.$store.state.selected_studies;
        let result = [];
        selected_studies.forEach(selected_study_group => {
          let cookie = {}
          cookie["events"] = [...[...selected_study_group].map(selected_study => {
            return Object.values(groupBy(events[selected_study], event => event.individual_id));
          })]
          cookie["study_group"] = selected_study_group;
          result.push(cookie);
        })
        return result
      }
    }
  },
  watch: {
    selected_events_per_study(new_value) {
      this.update_globe_paths(new_value);
    },
    selected_month(newMonth, oldMonth) {
      if (newMonth !== oldMonth) {
        this.update_globe_texture();
      }
    }
  }
}


</script>

<style scoped>
#canvasContainer {
  width: 100%;
}

</style>