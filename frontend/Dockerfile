FROM node:alpine

WORKDIR /app

COPY . .

RUN npm install && npm run build

RUN npm install -g serve

EXPOSE 80

CMD ["serve", "-s", "build", "-l", "80", "--host", "0.0.0.0"]
