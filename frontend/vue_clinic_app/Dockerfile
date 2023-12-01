# Build Stage
FROM node:lts-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Serve Stage
FROM node:lts-alpine AS serve-stage
WORKDIR /app
COPY --from=build-stage /app/dist /app/dist
RUN npm install -g http-server
EXPOSE 8080
CMD ["http-server", "dist"]
