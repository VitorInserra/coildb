# Stage 1: Build the React application
FROM node:18 AS build

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code and build
COPY . .
RUN npm run build

# Stage 2: Serve the application with Bitnami NGINX
FROM bitnami/nginx:latest

# Remove the default server blocks if they exist (safeguard)
RUN rm -f /opt/bitnami/nginx/conf/server_blocks/default-server-block.conf

# Copy the custom NGINX configuration
COPY nginx.conf /opt/bitnami/nginx/conf/nginx.conf

# Copy the built application from the previous stage
COPY --from=build /app/build /app

# Set the NGINX document root
ENV NGINX_DOCUMENT_ROOT=/app

# Expose port 8080
EXPOSE 8080

# Start NGINX in the foreground
CMD ["nginx", "-g", "daemon off;"]
