import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw" / "telco_support_tickets_dataset.csv"

def load_data():
    df = pd.read_csv('data/raw/telco_support_tickets_dataset.csv')
    return df


def save_snapshot(df):
    processed_path = Path('data/processed')
    processed_path.mkdir(parents=True, exist_ok=True)
    
    snapshot_path = processed_path / "v1_telco_support_tickets_snapshot.csv"
    df.to_csv(snapshot_path, index=False, encoding="utf-8")
    
    print(f"Snapshot saved to {snapshot_path}")
    

def main():
    df = load_data()

    # Phase 3.1 — structural setup only
    df["text_norm_v1"] = df["ticket_text"]

    save_snapshot(df)

if __name__ == "__main__":
    main()
    
    