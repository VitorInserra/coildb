FROM node:alpine

WORKDIR /app

COPY . .

RUN npm install && npm run build

RUN npm install -g serve

EXPOSE 8080

ENV HOST 0.0.0.0

CMD ["serve", "-s", "build", "-l", "8080"]
