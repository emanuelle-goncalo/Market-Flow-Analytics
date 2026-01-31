from utils import start_pipeline, process_data, create_dashboard

def main():
    try:
        # Extract, Transform and Load Pipeline
        df_raw = start_pipeline() 
        df_processed = process_data(df_raw)
        create_dashboard(df_processed)

        print("Pipeline executed successfully. Dashboard is live!")

    except Exception as e:
        print(f"\nERROR: {e}")

if __name__ == "__main__":
    main()