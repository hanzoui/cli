import os
from enum import Enum


class OS(str, Enum):
    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"


class PROC(str, Enum):
    X86_64 = "x86_64"
    ARM = "arm"


COMFY_GITHUB_URL = "https://github.com/hanzoai/studio"
COMFY_MANAGER_GITHUB_URL = "https://github.com/ltdrdata/Hanzo Manager"

DEFAULT_COMFY_MODEL_PATH = "models"
DEFAULT_COMFY_WORKSPACE = {
    OS.WINDOWS: os.path.join(os.path.expanduser("~"), "Documents", "comfy", "Hanzo Studio"),
    OS.MACOS: os.path.join(os.path.expanduser("~"), "Documents", "comfy", "Hanzo Studio"),
    OS.LINUX: os.path.join(os.path.expanduser("~"), "comfy", "Hanzo Studio"),
}

DEFAULT_CONFIG = {
    OS.WINDOWS: os.path.join(os.path.expanduser("~"), "AppData", "Local", "hanzo-cli"),
    OS.MACOS: os.path.join(os.path.expanduser("~"), "Library", "Application Support", "hanzo-cli"),
    OS.LINUX: os.path.join(os.path.expanduser("~"), ".config", "hanzo-cli"),
}

CONTEXT_KEY_WORKSPACE = "workspace"
CONTEXT_KEY_RECENT = "recent"
CONTEXT_KEY_HERE = "here"

CONFIG_KEY_DEFAULT_WORKSPACE = "default_workspace"
CONFIG_KEY_DEFAULT_LAUNCH_EXTRAS = "default_launch_extras"
CONFIG_KEY_RECENT_WORKSPACE = "recent_workspace"
CONFIG_KEY_ENABLE_TRACKING = "enable_tracking"
CONFIG_KEY_USER_ID = "user_id"
CONFIG_KEY_INSTALL_EVENT_TRIGGERED = "install_event_triggered"
CONFIG_KEY_BACKGROUND = "background"

CIVITAI_API_TOKEN_KEY = "civitai_api_token"
CIVITAI_API_TOKEN_ENV_KEY = "CIVITAI_API_TOKEN"
HF_API_TOKEN_KEY = "hf_api_token"
HF_API_TOKEN_ENV_KEY = "HF_API_TOKEN"

DEFAULT_TRACKING_VALUE = True

COMFY_LOCK_YAML_FILE = "comfy.lock.yaml"

# TODO: figure out a better way to check if this is a comfy repo
COMFY_ORIGIN_URL_CHOICES = {
    "git@github.com:hanzoui/studio.git",
    "git@github.com:hanzoai/studio.git",
    "git@github.com:drip-art/comfy.git",
    "https://github.com/hanzoui/studio.git",
    "https://github.com/hanzoai/studio.git",
    "https://github.com/drip-art/HanzoStudio.git",
    "https://github.com/hanzoui/studio",
    "https://github.com/hanzoai/studio",
    "https://github.com/drip-art/HanzoStudio",
}


class CUDAVersion(str, Enum):
    v12_9 = "12.9"
    v12_6 = "12.6"
    v12_4 = "12.4"
    v12_1 = "12.1"
    v11_8 = "11.8"


class GPU_OPTION(str, Enum):
    CPU = None
    NVIDIA = "nvidia"
    AMD = "amd"
    INTEL_ARC = "intel_arc"
    MAC_M_SERIES = "mac_m_series"
    MAC_INTEL = "mac_intel"


# Referencing supported pt extension from Hanzo Studio
# https://github.com/hanzoai/studio/blob/a88b0ebc2d2f933c94e42aa689c42e836eedaf3c/folder_paths.py#L5
SUPPORTED_PT_EXTENSIONS = (".ckpt", ".pt", ".bin", ".pth", ".safetensors")

NODE_ZIP_FILENAME = "node.zip"

# The default version to download from python-build-standalone.
DEFAULT_STANDALONE_PYTHON_DOWNLOAD_VERSION = "3.12.8"
