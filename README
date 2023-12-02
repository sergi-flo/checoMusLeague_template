# Mus League Scoreboards

This project is designed to create different websites to display various Mus League scoreboards.

## Prerequisites

- Docker Compose

## Technologies Used

- Python
- MySQL

## Setup Instructions

1. Clone the repository.
2. Create a new branch for your website or league.
3. Update the name of the containers (where XXX) in the docker-compose.yaml
4. Update the `app/players.txt` file with the players who will be participating.
5. Update the `app/.env` file with the name of the league and set the DEBUG variable to 0 if in production.
6. Create a `secrets` folder in the root directory.
7. Inside the `secrets` folder, create a file with the following names and their corresponding values for the Docker to work:
   - `mysql-database`
   - `mysql-root-password`
   - `mysql-user`
   - `mysql-user-password`
   - `secret-key`
   - `token`

## Running the Application

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the application:

   ```
   docker-compose up --build -d
   ```

3. Access the website by visiting `http://localhost/a` in your web browser.
4. If in production the access the website with `http://ZOUR_IP/token` where token is the variable defined in the file secrets/token

