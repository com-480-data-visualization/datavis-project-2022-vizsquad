import axios from 'axios';

export const HTTP = axios.create({
    baseURL: `https://data-viz-course-backend-e4sglwkopa-uc.a.run.app/`,
    headers: {
        internal_auth_token: 'data_viz',
    }
})
