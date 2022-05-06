import {HTTP} from '@/utils/http-common.js'

export const AnimalsModule = {
    state: {
        animals: ["hello", "world"]
    },
    mutations: {
        SET_ANIMALS(state, animals) {
            state.animals = animals
        }
    },
    actions: {
        async fetchAnimals(context) {
            const result = await HTTP.post('/bq_execute_query', {"query": "SELECT DISTINCT ROW_NUMBER() OVER() AS id, name, FROM ( SELECT DISTINCT individual_taxon_canonical_name AS name FROM epfl-course.datavizcourse.tot_events_2)"});
            if(result.status === 200) {
                context.commit('SET_ANIMALS', result.data);
                console.log("Fetched animals");
            }
            else {
                console.log('Error fetching animals');
            }
        }
    }
}