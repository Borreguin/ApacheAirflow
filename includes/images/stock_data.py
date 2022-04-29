import yfinance as yf
import pickle


tsla = yf.Ticker('TSLA')

# 1ST Reco
print(tsla.recommendations("To Grade").value_counts().keys()[0])
# 2nd Reco
#print(tsla.recommendations("To Grade").value_counts().keys()[0])

#with open('/tmp/scrip.out', 'wb+') as tmp_file:
#     pickle.dump({'test':'ok'}, tmp_file)