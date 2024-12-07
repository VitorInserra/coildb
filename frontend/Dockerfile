FROM node:18 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM bitnami/nginx:latest

COPY default.conf /opt/bitnami/nginx/conf/server_blocks/default.conf

COPY --from=build /app/build /app

ENV NGINX_DOCUMENT_ROOT=/app

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
