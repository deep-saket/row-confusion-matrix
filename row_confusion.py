import pandas as pd
import numpy as np
from collections import Counter

def generate_row_confusion_matrix(y_true, y_pred):
    """
    Generate a row confusion matrix as a DataFrame.

    Parameters:
    - y_true: List or array of ground truth labels
    - y_pred: List or array of predicted labels

    Returns:
    - pd.DataFrame with columns ['GT Class', 'Predicted Class', 'Error Rate (%)']
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Length of y_true and y_pred must be the same")

    total_per_class = Counter(y_true)
    confusion_counter = Counter()

    for true, pred in zip(y_true, y_pred):
        if true != pred:
            confusion_counter[(true, pred)] += 1

    rows = []
    for (gt_class, pred_class), count in confusion_counter.items():
        error_rate = 100.0 * count / total_per_class[gt_class]
        rows.append((gt_class, pred_class, round(error_rate, 2)))

    df = pd.DataFrame(rows, columns=["GT Class", "Predicted Class", "Error Rate (%)"])
    df.sort_values(by="Error Rate (%)", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
