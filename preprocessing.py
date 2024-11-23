import pandas as pd

def encode_class_scores(violation_df: pd.DataFrame):
    violation_df['class'] = violation_df['class'].map(lambda x: ord(x) - ord('A'))
    return violation_df

def calculate_append_severity_scores(violation_df: pd.DataFrame):
    violation_df['risk_score'] = violation_df.groupby(['violationid'])['class'].transform('sum')
    violation_df['risk_score_cat'] = violation_df['risk_score'].clip(upper=4)
    violation_df = violation_df.drop_duplicates(subset=['violationid'])
    return violation_df