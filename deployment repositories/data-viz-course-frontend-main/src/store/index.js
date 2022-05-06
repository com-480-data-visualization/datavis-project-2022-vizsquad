import {createStore} from 'vuex'
import {HTTP} from "@/utils/http-common";

export default createStore({
    state: {
        studies: [],
        selected_studies: [],
        events: [],
    },
    mutations: {
        //studies
        SET_STUDIES(state, studies) {
            state.studies = studies
        },
        SET_SELECTED_STUDIES(state, studies) {
            state.selected_studies = studies
        },

        ADD_STUDY_EVENTS_TO_EVENTS(state, event) {
            state.events.push(...event)
        },
        //animals
        SET_ANIMALS(state, animals) {
            state.animals = animals
        },
        SET_SELECTED_ANIMALS(state, animals) {
            state.selected_animals = animals
        },
    },
    actions: {
        //studies
        async fetchStudies(context) {
            try {
                const result = await HTTP.post('/bq_execute_query', {"query": "select * from epfl-course.datavizcourse.studies"});
                if (result.status === 200) {
                    context.commit('SET_STUDIES', result.data);

                    this.dispatch('setSelectedStudies', [20873986]);
                } else {
                    console.log('Error fetching studies');
                }
            } catch (e) {
                console.log(e)
            }
        },
        
        async fetchEvents(context, studyId) {
            try {
                const result = await HTTP.post('/bq_execute_query',
                    {"query": `select timestamp, location_lat, location_long, tag_id, study_id \
                            from epfl-course.datavizcourse.tot_events_2 \
                            where study_id = ` + studyId +
                            ` AND location_lat IS NOT NULL \
                            AND location_long IS NOT NULL \
                            ORDER BY timestamp ASC LIMIT 10000`});
                if (result.status === 200) {
                    context.commit('ADD_STUDY_EVENTS_TO_EVENTS', result.data);
                    console.log("Fetched event of study " + studyId);
                }
            } catch (e) {
                console.log(e);
            }
        },
        setSelectedStudies(context, studies) {
            console.log(studies);
            context.commit('SET_SELECTED_STUDIES', studies);
        },
        //animals
        async fetchAnimals(context) {
            try {
                const result = await HTTP.post('/bq_execute_query', {"query": "SELECT DISTINCT ROW_NUMBER() OVER() AS id, name, FROM ( SELECT DISTINCT individual_taxon_canonical_name AS name FROM epfl-course.datavizcourse.tot_events_2)"});
                if (result.status === 200) {
                    context.commit('SET_ANIMALS', result.data);
                    console.log("Fetched Animals");
                } else {
                    console.log('Error fetching animals');
                }
            } catch (e) {
                console.log(e)
            }
        },
        
        setSelectedAnimals(context, animals) {
            context.commit('SET_SELECTED_ANIMALS', animals);
        },
        async fetchAnimalsStudy(context, studyId) {
            try {
                const result = await HTTP.post('/bq_execute_query',
                {"query": "SELECT ROW_NUMBER() OVER() as id, name, FROM ( SELECT DISTINCT individual_taxon_canonical_name AS name FROM epfl-course.datavizcourse.tot_events_2 WHERE study_id = " + studyId + ")"});
                if (result.status === 200) {
                    console.log("Fetched animals of study " + studyId + result.data);
                    context.commit('SET_ANIMALS', result.data);
                    context.commit('SET_SELECTED_ANIMALS', result.data);
                }
            } catch (e) {
                console.log(e);
            }
        }
    }
})
