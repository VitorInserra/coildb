FROM node:alpine

WORKDIR /app

COPY . .

RUN npm install && npm run build

RUN npm install -g http-server

EXPOSE 8080

ENV HOST 0.0.0.0

CMD ["http-server", "build", "-p", "8080", "-a", "0.0.0.0"]
