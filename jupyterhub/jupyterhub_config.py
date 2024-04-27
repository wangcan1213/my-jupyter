from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator
import os

c.JupyterHub.authenticator_class = NativeAuthenticator


c.GenericOAuthenticator.enable_auth_state = True
c.Spawner.http_timeout = 300
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.hub_ip = '0.0.0.0'

c.DockerSpawner.network_name = 'jupyterhub'

c.DockerSpawner.remove = True

c.JupyterHub.spawner_class = DockerSpawner
c.NativeAuthenticator.create_system_users = True


notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/jupyter'
c.DockerSpawner.notebook_dir = notebook_dir

def pre_spawn_hook(spawner):
    username = spawner.user.name  
    volume_path = f"/home/jupyter/jupyterhub-files/{username}"
    if not os.path.exists(volume_path):
        os.makedirs(volume_path, exist_ok=True)
    os.chmod(volume_path, 0o777) 

c.DockerSpawner.pre_spawn_hook = pre_spawn_hook

c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.image = "my_remote_jupyterlab:latest"

# root
c.DockerSpawner.environment = {'GRANT_SUDO': 'yes'}
c.DockerSpawner.extra_create_kwargs = {'user': 'jovyan'}

# Persistence
c.JupyterHub.db_url = "sqlite:///data/jupyterhub.sqlite"
c.DockerSpawner.volumes = {
    '/home/jupyter/jupyterhub-files/{username}': notebook_dir
}


# Enable user registration
c.Authenticator.allowed_users = set()
c.Authenticator.admin_users = {'admin', 'wangcan'}
c.NativeAuthenticator.open_signup = True
