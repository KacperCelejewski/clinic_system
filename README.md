# Clinic System

This is a web application built with Flask, Vue.js, Docker,Docker-Compose and PostgreSQL. It is designed to provide a system for searching, editing, and deleting patient records.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/clinic_system.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `local_settings.py` file in the root directory of the project or configure the database settings. For example:

   ```python
   # local_settings.py

   DATABASE_URI = 'postgresql://username:password@localhost:5432/clinic_system'
   ```
5.1 Install docker and follow the instructions: https://www.docker.com/get-started/ 

5. Build and run the Docker containers from the top of the project:

   ```bash
   docker-compose up --build -d
   ```

6. Access the application in your browser at `http://localhost:8080`.

## Usage

- Search for a patient by entering their PESEL in the search bar.
- Edit a patient's information by clicking on the "Edit" button next to their record.
- Delete a patient's record by clicking on the "Delete" button next to their record.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
