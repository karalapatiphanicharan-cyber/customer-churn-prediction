import os
import matplotlib.pyplot as plt

def ensure_dir(directory):
    """Ensure that a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_plot(filename, directory='reports/figures/'):
    """Save a matplotlib plot to the specified directory."""
    ensure_dir(directory)
    filepath = os.path.join(directory, filename)
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {filepath}")

def get_project_root():
    """Returns the root directory of the project."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
