# jupyterhub/jupyterhub_config.py

c = get_config()

# Set the IP address for JupyterHub
c.JupyterHub.ip = '0.0.0.0'

# Set the port for JupyterHub
c.JupyterHub.port = 8000

# Use NativeAuthenticator
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'

# Allow users to sign up
c.NativeAuthenticator.open_signup = True

# Define admin user
c.Authenticator.admin_users = {'admin'}

# Specify the notebook directory
c.Spawner.notebook_dir = '~/notebooks'
