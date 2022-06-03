<template>
  <div id="foamtree-selector" class="scroll-box" ref="foamtree-ref"></div>
  <!--  <script defer type="text/javascript" src="assets/foamtree.js"></script>-->
</template>


<script>
window.foamtree = require('../assets/foamtree.js');

import {isEqual} from 'lodash';

export default {
  name: "TreeFoamSelectorTaxons",
  data() {
    return {
      remove_categories_with_one_child: true,
    }
  },
  methods: {
    init_foamtree_selector() {
      this.foamtree = new window.CarrotSearchFoamTree({

        // Identifier of the HTML element defined above
        id: "foamtree-selector",
        pixelRatio: window.devicePixelRatio || 1,

        // Disable rollout and pullback animations, use simple fading
        rolloutDuration: 0,
        pullbackDuration: 0,
        fadeDuration: 0,

        // Increase the relaxation quality threshold a little for
        // faster processing at the cost of slightly lower layout quality.
        relaxationQualityThreshold: 3,

        // Lower the parent group opacity, so that lower-level groups show through.
        parentFillOpacity: 0.5,

        // Always draw group labels, this will make zooming more attractive.
        wireframeLabelDrawing: "always",

        // You can change how many levels of polygons and labels below
        // each topmost closed group FoamTree will draw. Lower values will
        // result in faster rendering, but also less detail "underneath" the closed groups.
        maxGroupLevelsDrawn: 15,
        maxGroupLabelLevelsDrawn: 15,


        rainbowStartColor: "hsl(0, 90%, 50%)",
        rainbowEndColor: "hsl(120, 90%, 50%)",
        rainbowSaturationCorrection: 0.7,

        // Lower the border radius a bit to fit more groups.
        groupBorderWidth: 8,
        groupInsetWidth: 3,
        groupSelectionOutlineWidth: 4,

        groupMinDiameter: 0,

        dataObject: {},

        groupLabelDecorator: function (opts, params, vars) {
          if (params.hasChildren && params.browseable === false) {
            vars.labelText += " [+]";
          }
        },

        onGroupClick: function (event) {
          event.preventDefault();
        },

        onGroupHold: event => {
          this.foamtree.select({
            groups: event.group,
            selected: !this.foamtree.get("selection").groups.includes(event.group),
            keepPrevious: event.ctrlKey
          })
          this.update_group_selection(this.foamtree.get("selection"));
          event.preventDefault()
        },


        onGroupSelectionChanged: this.update_group_selection

      });
    },
    update_group_selection(selected){
      var set_of_selected_studies = new Set();
      selected.groups.forEach(function (group) {
        set_of_selected_studies.add(group.studies)
      });
      this.$store.dispatch("batchSwapSelectedStudies",set_of_selected_studies);
    },

    update_foamtree_selector() {
      if (this.studies.length === 0 || this.taxons.length === 0)
        return;


      var graph = {"groups": []};

      this.taxons.forEach(taxon => {
        var ref = graph.groups;
        taxon.hierarchy_string.forEach(current_taxon_id => {
          var cur_taxon = this.taxons.find(taxon => taxon.id == current_taxon_id)
          if (ref.find(group_member => group_member.id == cur_taxon.id) === undefined) {
            ref.push({
              "id": cur_taxon.id,
              "label": cur_taxon.canonical_name,
              "groups": []
            })
          }
          ref = ref.find(group_member => group_member.id == cur_taxon.id).groups;
        })
      })


      //console.log(this.studies)

      var start_point = graph;
      while (start_point.groups.length === 1 &&
      this.studies.find(study => study.taxon_id === start_point.groups[0].taxon_id) === undefined) {
        start_point = start_point.groups[0];
      }
      graph.groups = start_point.groups;

      function propagate_studies_and_weight(node, studies) {
        node.weight = 0;
        node.studies = new Set();

        studies.forEach(study => {
          if (study.taxon_id === node.id) {
            node.weight += 1
            node.studies.add(study.study_id)
          }
        })
        node.groups.forEach(group => {
          propagate_studies_and_weight(group, studies)
          node.weight += group.weight;
          group.studies.forEach(study_set => {
            node.studies.add(study_set)
          })
        })
      }

      propagate_studies_and_weight(graph, this.studies)

      //console.log(graph.groups)

      if (this.remove_categories_with_one_child) {
        function dfs_remove_categories_with_one_child(node, studies) {
          while (node.groups.length === 1) {
            node.groups = node.groups[0].groups;
          }
          node.groups.forEach(group => {
            dfs_remove_categories_with_one_child(group, studies)
          });
        }

        dfs_remove_categories_with_one_child(graph, this.studies);
      }

      this.foamtree.set({
        dataObject: {
          groups: graph.groups
        }
      });

    },
    update_foamtree_selected(oldSelectedStudies, newSelectedStudies) {
      //console.log(this.foamtree.get("selection"));
    },
    update_foamtree_resize() {
      this.foamtree.resize();
    },

  },
  mounted() {
    this.init_foamtree_selector();
    window.addEventListener('resize', this.update_foamtree_resize);
  },
  unmounted() {
    window.removeEventListener('resize', this.update_foamtree_resize);
  },
  computed: {
    studies: {
      get() {
        return this.$store.state.studies;
      }
    },
    selected_studies: {
      get() {
        return this.$store.state.selected_studies;
      }
    },
    taxons: {
      get() {
        return this.$store.state.taxons;
      }
    }
  },
  watch: {
    studies() {
      this.update_foamtree_selector();
    },
    taxons() {
      this.update_foamtree_selector();
    },
    selected_studies(newSelectedStudies, oldSelectedStudies) {
      this.update_foamtree_selected(newSelectedStudies, oldSelectedStudies);
    }
  }
}
</script>

<style scoped>
  #foamtree-selector {
    width: 100%;
    height: 100%;
    min-height: 150px;
    margin: 0;
    padding: 0;
  }
</style>