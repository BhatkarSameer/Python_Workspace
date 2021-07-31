import matplotlib.pyplot as plot
import numpy as np

# For making attractive and informative statistical graph
plot.style.use('seaborn-darkgrid')


def put_payoff(sT, strike_price, premium):
    pn1 = np.where(sT < strike_price, strike_price - sT, 0)
    return pn1 - premium


# Infosys stock price
spot_price = 900

# Put strike price and cost
strike_price = 900
premium = 20

# Stock price range at the expiration of the put
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9 * spot_price, 1.1 * spot_price)

payoff_long_put = put_payoff(sT, strike_price, premium)

# Plotting the graph
fig, axis = plot.subplots(figsize=(8, 5))
axis.spines['bottom'].set_position('zero')
axis.plot(sT, payoff_long_put, label='Put option buyer payoff')

plot.xlabel('Infosys Stock Price')
plot.ylabel('Profit and Loss')
plot.legend()
plot.show()

payoff_short_put = payoff_long_put * -1.0

# Plot
fig, axis = plot.subplots(figsize=(8, 5))
axis.spines['bottom'].set_position('zero')
axis.plot(sT, payoff_short_put, label='Put option seller payoff', color='r')

plot.xlabel('Infosys Stock Price')
plot.ylabel('Profit and Loss')
plot.legend()
plot.show()
