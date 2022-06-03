import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

import 'bootstrap/dist/css/bootstrap.min.css'

import 'font-awesome/css/font-awesome.min.css'

import 'vue-fullpage.js/dist/style.css'
import VueFullPage from 'vue-fullpage.js'

import * as d3 from "d3";

import 'leaflet/dist/leaflet.css';
import L from "leaflet";

import 'leaflet-sidebar-v2/css/leaflet-sidebar.css';
import "leaflet-sidebar-v2";

import "./styles/main.css";

const app = createApp(App)
app.use(store)
app.use(VueFullPage)
app.provide("d3", d3)
app.provide("L", L)
app.mount('#app')

window.bootstrap = require('bootstrap/dist/js/bootstrap.bundle.js')