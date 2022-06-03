<template>
  <div class="section" id="studies_map_section">
    <div id="studiesMapContainer"></div>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import "leaflet-sidebar-v2/css/leaflet-sidebar.min.css";

export default {
  name: "StudiesMapSection",
  inject: ["L"],
  data() {
    return {
      map: null,
      sidebar: null,
    };
  },
  methods: {
    init_map() {
      this.map = this.L.map("studiesMapContainer", {
        doubleClickZoom: true,
      }).setView([6.519962, 5], 3);
      this.L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution: "",
      }).addTo(this.map);
      this.sidebar = this.L.control
        .sidebar({
          autopan: false, // whether to maintain the centered map point when opening the sidebar
          closeButton: true, // whether t add a close button to the panes
          container: "sidebar", // the DOM container or #ID of a predefined sidebar container that should be used
          position: "left", // left or right
        })
        .addTo(this.map);
    },
    update_map() {
      if (this.studies.length === 0) return;

      var panelContent = {
        id: "userinfo", // UID, used to access the panel
        tab: '<i class="fa fa-gear"></i>', // content can be passed as HTML string,
        title: "Map of Studies' Origin", // an optional pane header
        position: "bottom", // optional vertical alignment, defaults to 'top'
        pane: "<p>This map shows where each of the studies started, and some basic information about them. </br> For instance, the name, start and end time of the studies as well as some information about how many individual were tracked and with what type of equipment is presented. Let's explore!</p>",
      };
      this.sidebar.addPanel(panelContent);
      this.sidebar.on('content', "hello")

      for (let i = 0; i < this.studies.length; i++) {
        var study = this.studies[i];

        var lat = study.main_location_lat;
        var long = study.main_location_long;
        var taxon_id = study.taxon_id;
        var img_url = "assets/img/taxon_pics_small/" + taxon_id + ".png";
        var imgIcon = this.L.icon({
          iconUrl: img_url,
          iconSize: [30, 30], // size of the icon
          iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
          popupAnchor: [0, 0], // point from which the popup should open relative to the iconAnchor
        });

        // make custom styled popup
        var popupContent = this.createHTMLTemplate(study);

        // add marker to the map
        this.L.marker([lat, long], { icon: imgIcon })
          .addTo(this.map)
          .bindPopup(popupContent, {
            //maxWidth: "auto",
          });
        this.map.invalidateSize();
      }
    },
    createHTMLTemplate(study) {
      return `<!DOCTYPE html>
        <html>
        <head>
        <title>${study.name}</title>
        </head>
        <body style="overflow:auto; max-height:100px">
        <div >
        <h1> <b>${study.name} <b></h1>
        <p>The study ranged from ${study.timestamp_first_deployed_location} to ${study.timestamp_last_deployed_location}. This is a ${study.study_type} study. ${study.study_objective}</p>
        <p>There were ${study.number_of_deployments} (${study.sensor_type_ids}) deployments over ${study.number_of_individuals} individuals ranging from ${study.timestamp_first_deployed_location} to ${study.timestamp_last_deployed_location}.</p>
        </div>
        </body>
        </html>
        `;
    },
  },
  mounted() {
    this.init_map();
  },
  beforeUnmount() {
    if (this.map) {
      this.map.remove();
    }
  },
  computed: {
    studies: {
      get() {
        return this.$store.state.studies;
      },
    },
  },
  watch: {
    studies() {
      this.update_map();
    },
  },
};
</script>

<style scoped>
#studiesMapContainer {
  height: 80%;
  width: 80%;
  margin-left: 10%;
}
</style>
