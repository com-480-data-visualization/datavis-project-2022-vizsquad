FROM python:3.6-slim-buster

WORKDIR /usr/src/app

# upgrade to latest pip
RUN pip install --upgrade pip

# install dependencies
COPY python-requirements.txt ./
RUN pip3 install --no-cache-dir -r python-requirements.txt

# copy the scripts
COPY / .

# GOOGLE CLOUD RUN
EXPOSE $PORT 
#set environment variable on linux: export PORT=2001
CMD exec gunicorn --bind $PORT:$PORT

#comment the 2 following lines to execute on local and access bash terminal inside the container.
#should not be commented for execution in GOOGLE CLOUD RUN
ENTRYPOINT ["python"]
CMD ["/usr/src/app/main.py"]


# RUN in detached mode
# docker run -d -p 2001:2001 -v $PWD:/usr/src/app/ data-viz-backend

# RUN in interactive mode
# docker run -p 2001:2001 -it -v $PWD:/usr/src/app/ data-viz-backend

# RUN container in production simulation
# docker run -d -p 2001:2001 data-viz-backend


# BUILD docker image
# docker build -t data-viz-backend .

# USE TERMINAL inside docker container
# docker run -it -v $PWD:/usr/src/app/ data-viz-backend bash
