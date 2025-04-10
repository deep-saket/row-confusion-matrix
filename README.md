# Row Confusion Matrix

A lightweight, intuitive alternative to the traditional confusion matrix. Ideal for classification tasks with many labels.

## Why Row Confusion Matrix?

Traditional confusion matrices can become unreadable with 10+ classes. This row-based format offers:

- Better readability
- Easier debugging of misclassifications
- Excel and log-friendly formatting
- Sortable error rates

## Example Format

| GT Class | Predicted Class | Error Rate (%) |
|----------|------------------|----------------|
| invoice  | receipt          | 18.4           |
| cheque   | form             | 12.9           |

## Install

```bash
pip install pandas numpy
