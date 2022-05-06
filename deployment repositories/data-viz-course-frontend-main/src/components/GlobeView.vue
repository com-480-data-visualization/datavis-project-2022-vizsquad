<template>
  <div ref="canvasContainer"></div>
</template>
{{selected_studies_events}}
<script>

// import * as THREE from 'three';
// import ThreeGlobe from 'three-globe';
import Globe from 'globe.gl'
// import {OrbitControls} from "three/examples/jsm/controls/OrbitControls";

export default {
  name: "GlobeView",

  data() {
    return {
    }
  },

  methods: {

    init_globe() {
      this.globe = new Globe();
      this.globe(this.$refs.canvasContainer)
      .globeImageUrl('/world.jpg')
      .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
      .height(0.8 * window.innerHeight)
      .width(0.8 * window.innerwidth)

      // setTimeout(() => {
      //   this.globe.resumeAnimation();
      //
      // }, 2000);
    },
    update_globe_paths(events) {
      //
      // this.globe.pathsData(paths)
      //     .pathColor(() => ['rgba(0,0,255,0.6)', 'rgba(255,0,0,0.6)']);

      let group_by_tag_id = events.reduce(function (r, a) {
        r[a.tag_id] = r[a.tag_id] || [];
        r[a.tag_id].push(a);
        return r;
      }, Object.create(null));

      let paths = [];
      for (let tag_id in group_by_tag_id) {
        let tag_events = group_by_tag_id[tag_id];
        paths.push(tag_events);
      }
      console.log(paths)

      this.globe.pathsData(paths)
          .pathPointLat((d) => d["location_lat"])
          .pathPointLng((d) => d["location_long"])
          .pathPointAlt(0.0).pathResolution(2)
          .pathColor(() => ['rgba(0,0,255,1.0)', 'rgba(255,0,0,1.0)'])
          .pathStroke(4).pathDashGap(1).pathDashAnimateTime(10000)
      if (paths.length > 0){
        if (paths[0].length > 0) {
          this.globe.pointOfView({"lng": paths[0][0]["location_long"], "lat": paths[0][0]["location_lat"], "altitude": 1.5}, 2000);
        }
      }

      // this.globe.controls().autoRotate = true;
      // this.globe.controls().autoRotateSpeed = 1.8;

    }
  },
  mounted() {
    this.init_globe();
  },
  computed: {
    events: {
      get(){
        return this.$store.state.events;
      }
    },
    selected_studies: {
      get(){
        return this.$store.state.selected_studies;
      }
    },
    selected_studies_events: {
      get(){
        const selectedStudies = this.$store.state.selected_studies;
        const events = this.$store.state.events;

        return events.filter(event => selectedStudies.includes(event["study_id"]));
      }
    },
  },
  watch: {
    selected_studies(newSelectedStudies, oldSelectedStudies) {
      newSelectedStudies.forEach(study => {
        if(!oldSelectedStudies.includes(study)){
          this.$store.dispatch('fetchEvents', study);
        }
      });
    },
    selected_studies_events(newStudiesEvents){
      console.log(newStudiesEvents)
      this.update_globe_paths(newStudiesEvents);
    }
  }
}


</script>

<style scoped>
#canvasContainer {
  padding: 20px;
  max-width: 80%;
}

</style>