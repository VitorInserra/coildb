
FROM node:18 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM caddy:2.7.4-alpine

COPY --from=build /app/build /usr/share/caddy

EXPOSE 8080

USER caddy

CMD ["caddy", "run", "--config", "./Caddyfile"]



