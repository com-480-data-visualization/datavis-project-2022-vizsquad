# data-viz-course-backend
Data viz course EPFL 2022 backend


# authentication
include in the headers:
- internal_auth_token -> dummy_token (to be implemented for production deployment)

# endpoints
Accessible at (local) http://localhost:2001/
Accesible at (cloud) https://data-viz-course-backend-e4sglwkopa-uc.a.run.app

# headers
internal_auth_token : data_viz

# body (JSON)
/bq_execute_query {"query": "select * from `epfl-course.datavizcourse.test_table1`"}

- root /
GET, non authenticated \
returns welcome message

- /auth
POST, authenticated \
returns the sent body (dummy endpoint)

- /hello_world
GET, authenticated \
returns dummy "hello world!" message. The code is not in main.py but in a separate file. Useful to split concerns in the app.