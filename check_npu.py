import sys
import os

# Remove the current directory from sys.path to avoid importing the unbuilt source
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir in sys.path:
    sys.path.remove(current_dir)

import intel_npu_acceleration_library
from intel_npu_acceleration_library.backend import npu_available, get_driver_version

print(f"Intel NPU Acceleration Library Version: {intel_npu_acceleration_library.__version__}")
print(f"Library Path: {os.path.dirname(intel_npu_acceleration_library.__file__)}")

try:
    available = npu_available()
    print(f"NPU Available: {available}")
    if available:
        try:
            version = get_driver_version()
            print(f"NPU Driver Version: {version}")
        except Exception as e:
            print(f"Error getting driver version: {e}")
    else:
        print("NPU is NOT detected by the library.")
except Exception as e:
    print(f"Error checking NPU availability: {e}")