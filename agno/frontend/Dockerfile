FROM node:24.0.2-alpine3.21
WORKDIR /home
RUN apk add git && npx create-agent-ui@1.1.6 agent-ui
WORKDIR /home/agent-ui
RUN npm install
ENTRYPOINT ["npm", "run", "dev"]
