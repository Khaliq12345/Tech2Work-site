# Use a lightweight Node.js base image
FROM node:20-slim

# Set working directory
WORKDIR /app

# Copy the pre-built .output folder
COPY .output .output

# Expose the port the app runs on (default for Nuxt is 3000)
EXPOSE 3000

# Run the Nuxt server
CMD ["node", ".output/server/index.mjs"]
