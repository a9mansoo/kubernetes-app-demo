FROM node:20-alpine AS build

WORKDIR /opt/app/

COPY frontend/app/ /opt/app/

RUN npm i 

RUN npm run build

RUN ls -al /opt/app/

FROM nginx:stable-alpine

WORKDIR /opt/app/

COPY --from=build /opt/app/dist /usr/share/nginx/html

COPY nginx_conf/nginx.conf /etc/nginx/

CMD ["nginx", "-g", "daemon off;"]
