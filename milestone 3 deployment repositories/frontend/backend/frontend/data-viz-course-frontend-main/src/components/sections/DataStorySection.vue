<template>
  <div class="section" style="min-height: 100vh;background: url('assets/img/pigeons.jpg') right / contain no-repeat, #f7f6f2;text-align: left;">
    <div class="container my-auto" style="/*margin-top: 50%;*/text-align: left;">
      <div class="row align-items-end" style="color: #c03418;">
        <div class="col-lg-4 col-xl-3 col-xxl-4 mx-auto">
          <h1 class="text-uppercase"><strong>Datastory</strong></h1>
          <p>Visualizing trajectories of homing pigeons</p>
          <hr>
          <p><br><strong><span style="color: rgb(0, 0, 0); background-color: transparent;">With the present website we wanted to build a set of visualization tools to help gaininig new insights into data regarding the migration and displacement of animals.The aim of such tools is twofold: help researchers to quickly visualize their data to build intuition, and get the average user closer to the study of such topics. Below, we present a study case, visualizing a dataset that was collected and studied in&nbsp;</span></strong><a href="https://www.sciencedirect.com/science/article/pii/S0003347216303141">this paper&nbsp;</a><strong><span style="color: rgb(0, 0, 0); background-color: transparent;">&nbsp;published on the journal "Animal Behaviour" by Pollonara, Guilford, Rossi, Bingman and Gagliardo.&nbsp;The complete dataset can be found&nbsp;</span></strong><a href=" https://www.datarepository.movebank.org/handle/10255/move.596">here</a><strong>&nbsp;.</strong><br><br></p>
        </div>
        <div class="col" style="background: url('assets/img/pigeons.jpg'), rgba(255,255,255,0);"></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="container-fluid full-height">
      <div class="row full-height">
        <div class="col-4 bg-info full-height">
          <div class="row justify-content-end full-height">
            <div class="col-9 vertical-center">
              <div style="padding-right: 5%">
                <h2 class="title">Inside a pigeon’s brain:</h2>
                <p>
                  A pigeon's homing process is fascinating and complex. They can
                  be displaced far away from their home, and still find its way
                  back to the loft . How do they do that? Pigeons are known to
                  employ different strategies to achieve this. They have an
                  internal geomagnetic compass, that can be used to find the
                  direction of home, they can use a “sun” compass, by looking at
                  the position of the sun, and a so-called navigational map,
                  that can be exploited when the pigeon is in unfamiliar places.
                  Some of these navigation are enabled by the left part of the
                  brain, while some others (usually the more complicated),
                  involve processing in both hemispheres. In the paper this was
                  studied in depth, by forcing some pigeons to use “only the
                  left hemisphere” and some others to use only the “only the
                  right hemisphere”. How did they do that? Simple, using an eye
                  cap! (like a pirate bird! \todo add pirate bird emoji). The
                  strongly lateralized visual inputs were thus inducing the
                  birds to use one of the two hemispheres.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-8 full-height" style="background: url('assets/img/pigeon.jpg') center / contain no-repeat, #f7f6f2;">
          <div class="row justify-content-start full-height">
            <div class="col-9 vertical-center">
              <div id="ds-graph1"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container-fluid full-height">
      <div class="row full-height">
        <div class="col-8 full-height" style="background-color: #f7f6f2">
          <div class="row justify-content-end full-height">
            <div class="col-9 vertical-center">
              <div>
                <div id="ds-graph2"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-4 bg-danger full-height">
          <div class="row justify-content-start full-height">
            <div class="col-9 vertical-center">
              <div style="padding-left: 5%">
                <h2 class="title">Are pigeons slowed down when using a cap?</h2>
                <p>
                  The first question they asked themselves is the following: are
                  pigeons slowed down by the cap? The hypothesis was that the
                  physical impairment induced by the experimental conditions was
                  causing them to fly slower, to better estimate their position.
                  The pigeons were displaced from their home to two different
                  cities: La Sterpia and Livorno. Some of them were forced to
                  use only their right hemisphere, some of them only the left
                  one, and some were free to use both. Surprisingly, the
                  distribution of the speeds for the birds with an eye-cap is
                  very similar to the ones without the cap. And this happens for
                  both cities! But if their speed was not affected, what changed
                  ?
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  #2980b9
  <div class="section">
    <div class="container-fluid full-height">
      <div class="row full-height">
        <div class="col-4 bg-info full-height">
          <div class="row justify-content-end full-height">
            <div class="col-9 vertical-center">
              <div style="padding-right: 5%">
                <h2 class="title">
                  Everyone likes the sea (pigeons included)!
                </h2>
                <p>
                  Pigeons with a left or right hemisphere bias showed strikingly
                  different trajectories while homing. A simple explanation of
                  this is that pigeons can use visual cues of familiar places to
                  orient themselves in space. Thus pigeons who had the coastline
                  in their sight, exploited it to return home following a
                  shorter path. Pigeons who did not (because of the impairment
                  caused by the experimental conditions) tended to deviate more
                  from the home trajectory. On the (left?) a picture homing to
                  Livorno under different experimental conditions.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-8 full-height" style="background-color: #f7f6f2">
          <div class="row justify-content-start full-height">
            <div class="col-9 vertical-center">
              <div id="ds-graph3"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container-fluid full-height">
      <div class="row full-height">
        <div class="col-8 full-height" style="background-color: #f7f6f2">
          <div class="row justify-content-end full-height">
            <div class="col-9 vertical-center">
              <div style="padding-left: 5%">
                <div id="ds-graph4"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-4 bg-danger full-height">
          <div class="row justify-content-start full-height">
            <div class="col-9 vertical-center">
              <div>
                <h2 class="title">Everyone likes the sea #2</h2>
                <p>
                  This behavior is particularly true if pigeons undergo a clock
                  shift treatment, which is a procedure to “mess up” the bird’s
                  internal clock, in order to prevent them from using it in
                  their navigation tasks. This behavior was consistent in many
                  pigeons’ trajectories. On the (right?) pigeons homing to La
                  Sterpia. It is interesting to note that the behavior of the
                  pigeons in the two groups is the opposite in this case,
                  compared with the previous one. In this case, pigeons with a
                  left/right impairment follow straighter paths, because when
                  homing from La Sterpia the coastline is in the opposite
                  direction
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container-fluid full-height">
      <div class="row full-height">
        <div class="col-4 bg-info full-height">
          <div class="row justify-content-end full-height">
            <div class="col-9 vertical-center">
              <div style="padding-right: 5%">
                <h2 class="title">What’s your favorite direction?</h2>
                <p>
                  Finally, we can compare the most frequent directions of the
                  pigeons, in this radar we show the direction frequency of the
                  velocities in 3 different trajectories (maybe add selector for
                  a subset of trajetories) . As you can see, when compared with
                  the pigeon in the control group , pigeons using only one
                  hemisphere tend to have a “broader” distribution of
                  directions.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-8 full-height" style="background-color: #f7f6f2">
          <div class="row justify-content-start full-height">
            <div class="col-9 vertical-center">
              <div id="ds-graph5"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import { groupBy, orderBy } from "lodash";

export default {
  name: "DataStorySection",
  inject: ["L"],
  data() {
    return {
      map: null,
      map4: null,
    };
  },
  methods: {
    init_graph2() {},
    update_graph2() {
      if (this.pigeon_data.length == 0) return;

      const grouped = groupBy(
        this.pigeon_data,
        (item) => `"${item.town}+${item.treatment}"`
      );

      var color_counter = 0;

      var data = Object.keys(grouped).map((key) => {
        const data = grouped[key].map((item) => item["ground-speed"]);
        return {
          x: data,
          type: "histogram",
          // marker: {
          // },
          opacity: 0.5,
          name:
            (key.substring(1, 3) === "LI" ? "Livorno" : "La Sterpaia") +
            " - " +
            (key.substring(4, 5) === "L"
              ? "Left"
              : key.substring(4, 5) === "R"
              ? "Right"
              : "Control"),
        };
      });

      const layout = {
        title: `Speed distribution in the three trajectories`,
        xaxis: {
          title: "Speed [km/h]",
          titlefont: {
            family: "Courier New, monospace",
            size: 18,
            color: "#7f7f7f",
          },
        },
        yaxis: {
          title: "Frequency",
          titlefont: {
            family: "Courier New, monospace",
            size: 18,
            color: "#7f7f7f",
          },
        },
        barmode: "overlay",
      };
      Plotly.newPlot("ds-graph2", data, layout);
    },
    init_graph3() {
      //instantiate the chart
      this.map = this.L.map("ds-graph3", {
        doubleClickZoom: true,
      }).setView([43.7, 10.33], 12);
      this.L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution: "",
      }).addTo(this.map);
    },
    init_graph4() {
      //instantiate the chart
      this.map4 = this.L.map("ds-graph4", {
        doubleClickZoom: true,
      }).setView([43.63, 10.36], 11);
      this.L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution: "",
      }).addTo(this.map4);
    },

    update_graph3() {
      //get data
      var pigeon_data3 = this.pigeon_data.filter(function (el) {
        return el.town == "ST";
      });

      const grouped_data = groupBy(
        pigeon_data3,
        (item) => `"${item.individual}+${item.release}"`
      );

      // Requiring the lodash library
      const _ = require("lodash");

      //loop through all group partitions
      Object.keys(grouped_data).forEach((key) => {
        var partition = grouped_data[key];
        _.orderBy(partition, ["timestamp"], ["asc"]);

        var polylinePoints = [];
        //loop through all the events of a partition
        for (let i = 0; i < partition.length; i++) {
          var current_event = partition[i];

          //add the point to the polyline
          //add new point to polyline
          polylinePoints.push([
            current_event["location-lat"],
            current_event["location-long"],
          ]);

          //get treatment of the pigeon (to color the line)
          var treatment = current_event.treatment;
          if (treatment == "R") {
            var colour = "red";
          } else if (treatment == "L") {
            var colour = "blue";
          } else {
            var colour = "green";
          }

          if (i == partition.length - 1) {
            var polyline = this.L.polyline(polylinePoints, {
              color: colour,
              weight: 3,
              opacity: 0.7,
              smoothFactor: 1,
            }).addTo(this.map);
          }
        }
      });

      //recompute the map with the correct size
      this.map.invalidateSize();
    },
    update_graph4() {
      //get data
      var pigeon_data4 = this.pigeon_data.filter(function (el) {
        return el.town == "LI";
      });

      const grouped_data = groupBy(
        pigeon_data4,
        (item) => `"${item.individual}+${item.release}"`
      );

      // Requiring the lodash library
      const _ = require("lodash");

      //loop through all group partitions
      Object.keys(grouped_data).forEach((key) => {
        var partition = grouped_data[key];
        _.orderBy(partition, ["timestamp"], ["asc"]);

        var polylinePoints = [];
        //loop through all the events of a partition
        for (let i = 0; i < partition.length; i++) {
          var current_event = partition[i];

          //add the point to the polyline
          //add new point to polyline
          polylinePoints.push([
            current_event["location-lat"],
            current_event["location-long"],
          ]);

          //get treatment of the pigeon (to color the line)
          var treatment = current_event.treatment;
          if (treatment == "R") {
            var colour = "red";
          } else if (treatment == "L") {
            var colour = "blue";
          } else {
            var colour = "green";
          }

          if (i == partition.length - 1) {
            var polyline = this.L.polyline(polylinePoints, {
              color: colour,
              weight: 3,
              opacity: 0.7,
              smoothFactor: 1,
            }).addTo(this.map4);
          }
        }
      });

      //recompute the map with the correct size
      this.map4.invalidateSize();
    },
    update_graph5() {
      console.log("helloooo")
      console.log("pigeon spider data", this.pigeon_spider_data)

      
      var data = [
      {
      type: 'scatterpolar',
      r: [39, 28, 8, 7, 28, 39],
      theta: ['A','B','C', 'D', 'E', 'A'],
      fill: 'toself',
      name: 'Group A'
      },
      {
      type: 'scatterpolar',
      r: [1.5, 10, 39, 31, 15, 1.5],
      theta: ['A','B','C', 'D', 'E', 'A'],
      fill: 'toself',
      name: 'Group B'
      }
    ]

    var layout = {
      polar: {
        radialaxis: {
          visible: true,
          range: [0, 50]
        }
      }
    }

    Plotly.newPlot("ds-graph5", data, layout)
    }
    
  },
  mounted() {
    this.init_graph3();
    this.init_graph4();
  },
  beforeUnmount() {
    Plotly.purge("ds-graph2");
  },
  computed: {
    pigeon_data: {
      get() {
        return this.$store.state.pigeon_data;
      },
    },
    pigeon_spider_data: {
      get() {
        return this.$store.state.pigeon_spider_data;
      },
    },
  },
  watch: {
    pigeon_data() {
      this.update_graph2();
      this.update_graph3();
      this.update_graph4();
    },
    pigeon_spider_data() {
      this.update_graph5();
      }
  },
};
</script>


<style scoped>
.title {
  text-transform: uppercase;
  font-weight: bold;
}

.vertical-center {
  min-height: 100%; /* Fallback for browsers do NOT support vh unit */

  display: flex;
  justify-content: center;
  align-items: center;
}

.full-height {
  min-height: 100%;
}

#ds-graph3 {
  height: 80%;
  width: 80%;
  margin-left: 10%;
}

#ds-graph4 {
  height: 80%;
  width: 80%;
  min-height: 80vh !important;
  min-width: 80vh !important;

  margin-right: 10%;
}

#ds-graph5 {
  height: 80%;
  width: 80%;
  min-height: 80vh !important;
  min-width: 80vh !important;

  margin-right: 10%;
}
</style>