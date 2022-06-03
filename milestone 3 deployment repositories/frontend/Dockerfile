FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /vue_app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]



# BUILD docker image
# docker build -t vue-app .

# RUN in interactive mode
# docker run -p 8080:8080 -it vue-app
# docker run -p 8080:8080 -it -v $PWD:/vue_app/ vue-app (not working)

# USE TERMINAL inside docker container
# docker run -it -v $PWD:/vue_app/ vue-app bash