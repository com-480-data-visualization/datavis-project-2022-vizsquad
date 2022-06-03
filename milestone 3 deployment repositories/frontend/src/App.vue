<template>
  <NavBar/>
  <full-page ref="fullpage" :options="options" id="fullpage" style="width: 100vw;" >
    <IntroductionSection/>

    <StudiesMapSection/>
    <MoveBankSection/>
    <DataStorySection/>
    <AboutUs/>
  </full-page>
  <div id="globeControler" class="modal">
    JUST SOME TEXT
          <div class="btn-group">
              <a href="#" id="monthly-btn" class="btn btn-primary active" @click="update_texture_selector('monthly')"
               aria-current="page">Monthly climate</a>
            <a href="#" id="countries-btn" class="btn btn-primary" @click="update_texture_selector('countries')">Country
              borders</a>
          </div>
  </div>
  <DataLoader/>

</template>

<script>
import GlobeView  from "@/components/GlobeView";
import DataLoader from "@/components/DataLoader";

import IntroductionSection from "@/components/sections/IntroductionSection";
import NavBar from "@/components/sections/NavBar";
import MoveBankSection from "@/components/sections/MoveBankSection";
import StudiesMapSection from "@/components/sections/StudiesMapSection";
import DataStorySection from "@/components/sections/DataStorySection";
import AboutUs from "@/components/sections/AboutUs";

export default {
  name: 'App',
  components: {
    AboutUs,
    DataStorySection,
    StudiesMapSection,
    MoveBankSection,
    NavBar,
    IntroductionSection,
    // StudiesList,
    // DateRangePickerComponent,
    // DirectionalSpider,

    // PigeonStory,
    DataLoader
  },
  data(){
    return {
      options: {
        navigation: true,
        sectionsColor: ['#f2f2f2', '#f7f6f2', '#000011', ],
        navigationTooltips: ["Home", "Studies", "Data"],
        menu: '#menu',
        anchors: ['page1', 'page2', 'page3'],
        //scrollOverflow: true,
        scrollBar: false,

        verticalCentered: true,

        normalScrollElements: '.scroll-box, #foamtree-selector, .globe-view, #canvasContainer',

        onLeave: this.onLeave
      }
    }
  },
  methods:{
    onLeave(origin, destination, direction){
      if(origin.index == 0 && destination.index == 1){
        document.getElementById("mainNav").classList.add("navbar-other-pages");
        document.getElementById("mainNav").classList.add("navbar-shrink");
      }
      if(origin.index == 1 && destination.index == 0){
        document.getElementById("mainNav").classList.remove("navbar-other-pages");
        document.getElementById("mainNav").classList.remove("navbar-shrink");
      }
    }
  }
}
</script>

<style>
#fullpage {
  width: 100vw;
}

#fp-nav ul li a span,
.fp-slidesNav ul li a span {
  background: white;
  width: 8px;
  height: 8px;
  margin: -4px 0 0 -4px;
}

#fp-nav ul li a.active span,
.fp-slidesNav ul li a.active span,
#fp-nav ul li:hover a.active span,
.fp-slidesNav ul li:hover a.active span {
  width: 16px;
  height: 16px;
  margin: -8px 0 0 -8px;
  background: transparent;
  box-sizing: border-box;
  border: 1px solid #24221F;
}

#globeControler {
  background: green;
  position: absolute;
  float: left;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
}


</style>
