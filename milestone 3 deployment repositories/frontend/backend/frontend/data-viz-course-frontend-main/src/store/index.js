import {createStore} from 'vuex'
import {HTTP} from "@/utils/http-common";
import {has} from "lodash";


export default createStore({
    state: {
        studies: [],
        selected_studies: new Set(),
        events: {},
        fetched_studies: new Set(),
        taxons: [],
        pigeon_data: [],
        pigeon_spider_data: [],
        // current month and date for analysis
        selected_date: new Date(80)
    },
    mutations: {
        //studies
        SET_STUDIES(state, studies) {
            state.studies = studies
        },
        ADD_TO_SELECTED_STUDIES(state, studies_group) {
            state.selected_studies.add(studies_group)
        },
        REMOVE_FROM_SELECTED_STUDIES(state, studies_group) {
            state.selected_studies.delete(studies_group)
        },

        ADD_STUDY_EVENTS_TO_EVENTS(state, events_study) {
            state.events[events_study["study_id"]] = events_study["events"]
        },
        //animals
        SET_TAXONS(state, taxons) {
            state.taxons = taxons
        },
        SET_SELECTED_DATE(state, date) {
            state.selected_date = date
        },
        ADD_FETCHED_STUDIES(state, study) {
            state.fetched_studies.add(study)
        },
        BATCH_SWAP_SELECTED_STUDIES(state, studies) {
            state.selected_studies = studies
        },
        SET_PIGEON_DATA(state, data) {
            state.pigeon_data = data
        },
        SET_PIGEON_SPIDER_DATA(state, data) {
            state.pigeon_spider_data = data
        }
    },
    actions: {
        //studies
        async fetchStudies(context) {
            try {
                const result = await HTTP.get('/studies');
                if (result.status === 200) {
                    context.commit('SET_STUDIES', result.data);
                    //this.dispatch('setSelectedStudies', [20873986]);
                } else {
                    console.log('Error fetching studies');
                }
            } catch (e) {
                console.log(e)
            }
        },

        async fetchEvents(context, studyId) {
            console.log('fetching events for study: ' + studyId);
            if(has(context.state.events, studyId)){
                // already fetched no need to add again to dataset
                return;
            }
            try {
                const result = await HTTP.get(`/events/${studyId}`,);
                if (result.status === 200) {
                    console.log("RESULT", result.data)
                    context.commit('ADD_STUDY_EVENTS_TO_EVENTS', {"events": result.data, "study_id": studyId});
                    console.log("Fetched event of study " + studyId);
                }
            } catch (e) {
                console.log(e);
            }
        },

        addSelectedStudies(context, studies) {
            context.commit('ADD_TO_SELECTED_STUDIES', studies);
        },

        removeSelectedStudies(context, studies) {
            context.commit('REMOVE_FROM_SELECTED_STUDaIES', studies);
        },

        batchSwapSelectedStudies(context, studies) {
            context.commit('BATCH_SWAP_SELECTED_STUDIES', studies);
        },

        async fetchTaxons(context) {
            try {
                const result = await HTTP.get('/taxons_reduced');
                if (result.status === 200) {
                    result.data = result.data.map(taxon => {
                        taxon.hierarchy_string = taxon.hierarchy_string.split("-");
                        return taxon;
                    });
                    //console.log(result.data)
                    context.commit('SET_TAXONS', result.data);
                    console.log("Fetched taxons");
                }
            } catch (e) {
                console.log(e);
            }
        },

        setSelectedDate(context, date) {
            context.commit('SET_SELECTED_DATE', date);
        },

        async fetchPigeonData(context) {
            try {
                const result = await HTTP.get('/pigeons');
                if (result.status === 200) {
                    context.commit('SET_PIGEON_DATA', result.data);
                    console.log("Fetched pigeon data");
                }
            } catch (e) {
                console.log(e);
            }
        },
        async fetchPigeonSpiderData(context) {
            try {
                const result = await HTTP.get('/spider');
                if (result.status === 200) {
                    context.commit('SET_PIGEON_SPIDER_DATA', result.data);
                    console.log("Fetched spider data");
                }
            } catch (e) {
                console.log(e);
            }
        }

    }
})
