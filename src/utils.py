import yfinance as yf
import polars as pl
import plotly.graph_objects as go

def start_pipeline():
    """Extraction Layer: Fetching Crypto data (ETH, BTC, ADA)"""
    print("Starting data extraction for Cryptocurrencies...")
    
    # Define tickers for the required assets
    tickers = ["ETH-USD", "BTC-USD", "ADA-USD"] 
    
    # Download 5 years of historical
    raw_data = yf.download(tickers, period="5y", interval="1d", auto_adjust=True)
    
    # Reset the Date index
    df_close = raw_data['Close'].reset_index()
    df_close.columns = [str(col) for col in df_close.columns]
    
    # Convert from Pandas to Polars for high-performance
    return pl.from_pandas(df_close)

def process_data(df_pl):
    """Engineering Layer: Normalization (Base 100)"""

    print("Calculating accumulated growth...")
    
    # Identify all columns except 'Date' to apply transformation
    assets = [col for col in df_pl.columns if col != "Date"]
    
    for asset in assets:
        # Get the first available non-null value as the starting baseline
        first_val_series = df_pl.select(pl.col(asset).filter(pl.col(asset).is_not_null())).head(1)
        
        if first_val_series.height > 0:
            first_val = first_val_series.item()
            # Create a normalized column (Current Price / Initial Price * 100)
            df_pl = df_pl.with_columns(
                ((pl.col(asset) / first_val) * 100).alias(f"{asset}_Indexed")
            )
    return df_pl

def create_dashboard(df_pl):
    
    print("Generating interactive dashboard...")
    fig = go.Figure()
    
    # Select only the normalized columns for plotting
    indexed_cols = [col for col in df_pl.columns if "_Indexed" in col]
    
    for col in indexed_cols:
        # Drop null values
        clean_df = df_pl.select(["Date", col]).drop_nulls()
        
        fig.add_trace(go.Scatter(
            x=clean_df["Date"], 
            y=clean_df[col], 
            name=col.replace("_Indexed", ""),
            mode='lines'
        ))

    # dark theme
    fig.update_layout(
        title="<b>Market-Flow Analytics:</b> BTC vs ETH vs ADA Performance (Base 100)",
        xaxis_title="Timeline",
        yaxis_title="Relative Value (Base 100)",
        template="plotly_dark",
        hovermode="x unified"
    )
    
    fig.show()