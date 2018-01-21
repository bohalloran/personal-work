#########################
# Wordpress installation
#########################

# Set the base image for this installation
FROM bohalloran/centos7base:7.4.1708

# File Author / Maintainer
MAINTAINER brian@ohalloran.com

# Pre-reqs
RUN touch /var/lib/rpm/* && \
yum clean all && \
yum -y update && \
yum -y install httpd mod_rewrite mod_ssl mod_env php-common php-cli php-mysql mysql-server unzip wget && \
rm -rf /var/cache/*

# Files that need to be added
ADD mysql-setup.sql /tmp/
ADD wordpress.conf /etc/httpd/conf.d/

# Application Install
RUN wget -P /var/www/html/ https://wordpress.org/latest.zip && \
unzip /var/www/html/latest.zip -d /var/www/html/ && \
rm -rf /var/www.html/latest.zip

# Run Mysql install
RUN service mysqld start && \
mysql < /tmp/mysql-setup.sql && \
rm -rf /tmp/mysql-setup.sql* && \
service mysqld stop

# Copy the WP-config file
RUN cp /var/www/html/wordpress/wp-config-sample.php /var/www/html/wordpress/wp-config.php

# Edit the wp-config file
RUN sed -ie 's/database_name_here/wordpress/g' /var/www/html/wordpress/wp-config.php && \
sed -ie 's/username_here/wpuser/g' /var/www/html/wordpress/wp-config.php && \
sed -ie 's/password_here/P@ssw0rd/g' /var/www/html/wordpress/wp-config.php

# Set Permissions
RUN chown -R apache:apache /var/www/html/wordpress && \
chmod -R 755 /var/www/html/wordpress

# Start mysql and apache on boot
RUN echo "service mysqld start" >> ~./bashrc && \
echo "service httpd start" >> ~./bashrc

# Expose Necessary Ports
EXPOSE 80
