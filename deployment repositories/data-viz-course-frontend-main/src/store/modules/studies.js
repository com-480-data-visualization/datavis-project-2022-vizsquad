import {HTTP} from '@/utils/http-common.js'

export const StudiesModule = {
    state: {
        studies: ["bokic", "smokic"]
    },
    mutations: {
        SET_STUDIES(state, studies) {
            state.studies = studies
        }
    },
    actions: {
        async fetchStudies(context) {
            const result = await HTTP.post('/bq_execute_query', {"query": "select * from epfl-course.datavizcourse.studies"});
            if(result.status === 200) {
                context.commit('SET_STUDIES', result.data);
                console.log("Fetched studies");
            }
            else {
                console.log('Error fetching studies');
            }
        }
    }
}