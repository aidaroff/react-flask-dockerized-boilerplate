FROM node:10-alpine

LABEL maintainer="Alibek Aidarov aydarov.alibek@gmail.com"

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY . .
RUN npm install --silent

# start app
CMD ["npm", "start"]