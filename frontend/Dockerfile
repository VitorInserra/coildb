FROM node:alpine

WORKDIR /app

COPY build/ .
RUN npm install -g serve

EXPOSE 80

CMD ["serve", "-s", ".", "-l", "80"]
