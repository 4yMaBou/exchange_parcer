import binance
import bybit
import huobi
import latoken
import poloniex
import pandas as pd



def get_tickers():
    response_binance = binance.main()
    response_bybit = bybit.main()
    response_houbi = huobi.main()
    response_latoken = latoken.main()
    response_poloniex = poloniex.main()
    sorted_binance = {key: response_binance[key] for key in sorted(response_binance)}
    sorted_bybit = {key: response_bybit[key] for key in sorted(response_bybit)}
    sorted_huobi = {key: response_houbi[key] for key in sorted(response_houbi)}
    sorted_latoken = {key: response_latoken[key] for key in sorted(response_latoken)}
    sorted_poloniex = {key: response_poloniex[key] for key in sorted(response_poloniex)}
    sorted_responses = [sorted_binance, sorted_bybit, sorted_huobi, sorted_latoken, sorted_poloniex]
    df = pd.DataFrame(sorted_responses, index=["binance", "bybit", "huobi", "latoken", "poloniex"])
    df = df.transpose()
    df = df.loc[df.notna().sum(axis=1) != 1]
    df['Difference'] = ((df.max(axis=1) - df.min(axis=1)) / df.min(axis=1)) * 100
    threshold = 1.5 
    df = df.loc[df['Difference'] > threshold]


    df.to_csv("main.csv")



if __name__ == "__main__":
    get_tickers()