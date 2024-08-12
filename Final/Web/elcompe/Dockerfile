# Use the official PHP image as the base image
FROM php:7.4-apache

# Copy the application files to the container
COPY . /var/www/html/

# Install any additional dependencies your application may need
# # For example, you might need to install the GD extension for image processing
# RUN apt-get update \
#     && apt-get install -y libpng-dev \
#     && docker-php-ext-install gd

# Set the working directory
WORKDIR /var/www/html

# Update Apache configuration to use port 10001
RUN sed -i 's/80/10102/g' /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf

# Expose port 10001 for Apache
EXPOSE 10102

# Start Apache
CMD ["apache2-foreground"]
