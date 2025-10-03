import sys

print("✅ Python executable:", sys.executable)

try:
    import pandas as pd
    import numpy as np
    import matplotlib
    import seaborn
    import sklearn
    import statsmodels

    print("🎉 All libraries imported successfully!")
    print("Pandas version:", pd.__version__)
    print("NumPy version:", np.__version__)
    print("Matplotlib version:", matplotlib.__version__)
    print("Seaborn version:", seaborn.__version__)
    print("Scikit-learn version:", sklearn.__version__)
    print("Statsmodels version:", statsmodels.__version__)

except ImportError as e:
    print("❌ Import error:", e)
