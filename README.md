# One Stack

<p align="center">
  <a href="https://fakerino.com"><img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-ziovv&psig=AOvVaw3uZ16aK3mSaajGqkXV8Jif&ust=1686850209644000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJCUwvGkw_8CFQAAAAAdAAAAABAJ" alt="Fakerino"></a>
</p>
<p align="center">
    <em>The one Data Stack to rule them all. Deploy all you need for your data project, in open source fashion 🚀🌐 A comprehensive project incorporating Metabase, Airflow, dbt, Docker, Terraform, and GitHub Workflows. </em>
</p>
<a href="https://github.com/alfredosa/onestack" target="_blank">
    <img src="https://img.shields.io/github/stars/alfredosa/onestack?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://onestack.slack.com/" target="_blank">
    <img src="https://img.shields.io/badge/slack-join-white.svg?logo=slack" alt="Slack">
</a>
<a href="https://www.youtube.com/watch?v=5ula1NjaHUA&ab_channel=PortalPostMalone" target="_blank">
    <img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/5ula1NjaHUA?style=social">
</a>
<a href="https://github.com/alfredosa/onestack/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white" alt="License">
</a>
</p>

## Description

One Stack is a powerful project that combines the capabilities of Airflow, dbt, Docker, Terraform, and GitHub Workflows. It provides a scalable and efficient solution for managing and orchestrating data workflows, running dbt transformations, and deploying infrastructure resources.

This repository contains the necessary files and configurations to set up an end-to-end data engineering and deployment pipeline using popular tools and technologies.

## Installation

To get started with One Stack, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/one-stack.git
   cd one-stack
   ```

2. **Configure your environment:**
- Update the necessary configuration files according to your requirements.
- Ensure you have the required credentials for services like AWS, Docker Hub, and others.

3. **Set up infrastructure:**
- Use Terraform to provision the required infrastructure resources. Navigate to the `terraform` directory and follow the instructions in the README file.

4. **Build and deploy Docker containers:**
- Customize the Dockerfile and docker-compose.yml files in the `docker` directory based on your project needs.
- Build and deploy the Docker containers by running the appropriate Docker commands.

5. **Configure Airflow and dbt:**
- Set up the Airflow configuration by modifying the airflow.cfg file in the `airflow` directory.
- Create your Airflow DAGs in the `dags` directory and customize them according to your workflows.
- Define your dbt models in the `dbt` directory and update the dbt_project.yml file accordingly.

6. **Enable CI/CD with GitHub Workflows:**
- Customize the `.github/workflows/ci_cd.yml` file to suit your CI/CD pipeline requirements.
- Configure the necessary secrets in your GitHub repository settings for secure access to services.

For detailed instructions and additional customization options, refer to the documentation included in each directory.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Let's build One Stack together!

## License

This project is licensed under the [MIT License](LICENSE).

