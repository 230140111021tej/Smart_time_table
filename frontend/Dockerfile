FROM node:18

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
RUN yarn install --frozen-lockfile || npm install

COPY . /usr/src/app

EXPOSE 3000

CMD ["yarn", "dev"]
