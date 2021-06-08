run:
	FLASK_ENV=development 	FLASK_APP=infopublic_mail/app.py	flask run

export_username:
	export MAIL_USERNAME=admin@infopublicpb.com.br

export_password:
	export MAIL_PASSWORD=mP83EUd8