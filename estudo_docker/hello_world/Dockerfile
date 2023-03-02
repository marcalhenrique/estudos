FROM node:14
WORKDIR  /home/marcal/Documents/Marcal/estudos/estudo_docker/hello_world
ARG PORT=8080
EXPOSE $PORT
ENV PORT=$PORT
COPY . .
RUN npm install
ENTRYPOINT npm start
