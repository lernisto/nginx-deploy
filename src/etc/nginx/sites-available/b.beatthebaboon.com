server {
	listen 80;
	listen [::]:80;

	root /var/www/QD583HKkzJRE/public;

	index index.html index.htm index.nginx-debian.html;

	server_name b.beatthebaboon.com;

	location / {
		try_files $uri $uri/ =404;
	}

}