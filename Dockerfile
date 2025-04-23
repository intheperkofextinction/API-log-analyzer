# Use the official Node.js image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of your app code
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Run the app
CMD ["node", "server.js"]

