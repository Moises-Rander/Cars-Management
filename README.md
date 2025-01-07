# Cars - Fullstack Django Project

## Description
"Cars" is an inventory management system for vehicles, developed with Django and hosted on AWS. It allows users to register, edit, view, and delete vehicles, as well as provides authentication and user management features.

## Technologies Used
- **Django**: Web development framework.
- **PostgreSQL**: Relational database.
- **AWS**: Hosting the system.
  - **EC2**: Virtual server instance.
  - **IP Elástico**: Fixed IP address for access.
  - **Volume de Backup**: Additional storage for emergencies.
- **Git**: Version control.

## Features
- Complete CRUD functionality for vehicle registration.
- User registration and authentication.
- Upload and display images of vehicles.
- Authentication validation for system access.
- Native Django admin for table management.

## Local Setup
To configure and run the project locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/usuario/projeto-carros.git
2. Navigate into the project directory:
   ```bash
   cd projeto-carros
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Create an .env file at the root of your project and declare your database password:
   ```bash
   DATABASE_PASSWORD="Senha_Do_Seu_Banco_De_Dados_PostgreSQL"
   
6. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver

## AWS Deploy
The deployment was done following these steps:
1. Create an EC2 instance on AWS.
2. Configure an Elastic IP for fixed access.
3. Set up firewall rules for global access.
4. Configure backup volumes for emergencies.
5. Link the GitHub repository to the server.
6. Deploy the project on the EC2 instance.

## Architecture
The project follows the MTV (Model-Template-View) architecture, typical of Django applications, with well-organized folders for easy maintenance and scalability.

## Challenges and Solutions
- **AWS Hosting**: Faced challenges configuring and managing the EC2 instance for the first time.
- **Frontend and Backend Integration**: Worked on creating UI layouts that efficiently integrated with the backend.

## Screenshots
1. Logged-in user homepage
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 06 36" src="https://github.com/user-attachments/assets/a440ad9c-8bb8-4cb3-8963-83543c744be7" />

2. Login page
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 07 12" src="https://github.com/user-attachments/assets/c0c0999d-64e4-478b-80a9-ec5487e3f030" />

3. User registration page
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 07 31" src="https://github.com/user-attachments/assets/53a7643c-7dfc-43c0-bb85-5e01e994240c" />

4. Car registration page
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 08 00" src="https://github.com/user-attachments/assets/be42f9d3-acbb-483b-9cd1-af3badaec873" />

5. Car details page
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 08 23" src="https://github.com/user-attachments/assets/f3a44e3e-3b39-4777-a547-b292690cc1d4" />

6. Django Admin for table management
- <img width="1710" alt="Captura de Tela 2025-01-07 às 10 05 22" src="https://github.com/user-attachments/assets/613138fd-150a-41c8-92ea-ffdb03f13106" />

## Contact
- **Email**: moisesrander@outlook.com
- **Phone**: +55 (98) 99123-2503

