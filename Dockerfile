# jupyterhub/Dockerfile
FROM python:3.12

# Install necessary packages
RUN apt-get update && apt-get install -y wget unzip npm nodejs

# Install JupyterHub and notebook
RUN pip install --no-cache-dir jupyterhub notebook

# Install configurable-http-proxy
RUN npm install -g configurable-http-proxy

# Install NativeAuthenticator
RUN pip install jupyterhub-nativeauthenticator

# Install JupyterHub client
RUN pip install jupyterhub-client

# Install additional Python packages
RUN pip install --no-cache-dir requests numpy pandas matplotlib scikit-learn mysql-connector-python pymongo hdfs pyhive sqlalchemy pyspark pyarrow

# Copy the JupyterHub configuration file
COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

# Copy the admin creation script
COPY create_admin.py /usr/local/bin/create_admin.py

# Expose the port for JupyterHub
EXPOSE 8000

# Start JupyterHub and create admin user
CMD ["sh", "-c", "jupyterhub --config /etc/jupyterhub/jupyterhub_config.py & sleep 10 && python /usr/local/bin/create_admin.py"]
