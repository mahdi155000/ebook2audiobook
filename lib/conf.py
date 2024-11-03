import os

NATIVE = "native"
DOCKER_UTILS = "docker_utils"
FULL_DOCKER = "full_docker"

version = "2.0.0"
min_python_version = (3, 10)
max_python_version = (3, 11)

requirements_file = os.path.abspath(os.path.join(".","requirements.txt"))

docker_utils_image = 'utils'
web_interface_port = 7860
web_dir_expire = 72 # hours

python_env_dir = os.path.abspath(os.path.join(".","python_env"))
models_dir = os.path.abspath(os.path.join(".","models"))
ebooks_dir = os.path.abspath(os.path.join(".","ebooks"))
audiobooks_web_dir = os.path.abspath(os.path.join(".","audiobooks","web"))
audiobooks_local_dir = os.path.abspath(os.path.join(".","audiobooks","local"))
processes_dir = os.path.abspath(os.path.join(".","tmp"))

supported_ebook_formats = ['.epub', '.mobi', '.azw3', 'fb2', 'lrf', 'rb', 'snb', 'tcr', '.pdf', '.txt', '.rtf', '.docx', '.html', '.odt', '.azw']
final_format = "m4b"

os.environ["TTS_CACHE"] = models_dir
os.environ["TORCH_HOME"] = models_dir
os.environ["HUGGINGFACE_HUB_CACHE"] = models_dir
os.environ["HF_HOME"] = models_dir
os.environ["HF_DATASETS_CACHE"] = models_dir
os.environ["HF_TOKEN_PATH"] = os.path.join(os.path.expanduser("~"), ".huggingface_token")
os.environ["CALIBRE_TEMP_DIR"] = processes_dir
os.environ["CALIBRE_CACHE_DIRECTORY"] = processes_dir
os.environ["CALIBRE_NO_NATIVE_FILEDIALOGS"] = "1"