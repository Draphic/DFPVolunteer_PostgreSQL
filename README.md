# DFPVolunteer_PostgreSQL
PostgreSQL for DFP Volunteer
Get Started with PostgreSQL: https://www.postgresql.org/docs/current/tutorial.html

Prerequisites:
	Download pgadmin4 v7.6: https://www.postgresql.org/ftp/pgadmin/pgadmin4/v7.6/windows/
	Setup WSL and docker: https://docs.docker.com/desktop/wsl/
	
To start and run the PostgreSQL server:
Requires: Docker is already installed and setup
	1. Clone the repo
	2. Open a terminal in the repo directory
	3. Create and run the image:
		$ docker compose up

You can now access the server using PGAdmin.
	1. Open PGAdmin (complete any initial setup)
	2. Go to Object > Register > Server
	3. Under the general tab
		a. Give the server a name (I name it DFPostgres)
		b. (optional) Customize the foreground and/or background color
	4. Under the Connection tab
		a. Host name/address: localhost
		b. Port: 5401
			Note: You can find the port number by opening the Docker desktop app, look in containers, and hover over the 'Port(s)' column of the db-1 row
		c. Maintenance database: postgres
		d. Username: postgres
		e. Password: see the .env file (ask for this if you don't have it yet)
		f. (optional) save password - enable to reconnect later without re-entering the password
	5. Press 'Save' to save credentials and connect

If the init scripts are changed:
	1. Open Docker Desktop
	2. In 'Containers', delete the dfpvolunteer_postgresql container
	3. In 'Volumes', delete the dfpvolunteer_postgresql_pgdata volume
	4. Create and run the image:
		$ docker compose up
