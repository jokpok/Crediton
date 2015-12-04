from pytz import timezone  
from datetime import datetime, timedelta  
from zipline.utils.tradingcalendar import get_early_closes
from numpy import matrix, array, zeros, empty, sqrt, ones, dot, append, mean, cov, transpose, linspace
import numpy as np
import scipy.optimize
import math
import random

# Compute expected return on portfolio.
def compute_mean(W,R):
    return sum(R*W)

# Compute the variance of the portfolio.
def compute_var(W,C):
    return dot(dot(W, C), W)

# Combination of the two functions above - mean and variance of returns calculation. 
def compute_mean_var(W, R, C):
    return compute_mean(W, R), compute_var(W, C)

def fitness(W, R, C, r):
    # For given level of return r, find weights which minimizes portfolio variance.
    mean_1, var = compute_mean_var(W, R, C)
    # Penalty for not meeting stated portfolio return effectively serves as optimization constraint
    # Here, r is the 'target' return
    penalty = 50**abs(mean_1-r)
    return var + penalty
    
# Given risk-free rate, asset returns, and covariances, this function
# calculates the weights of the tangency portfolio with regard to Sharpe
# ratio maximization.

def fitness_sharpe(W, R, C, rf):
    mean_1, var = compute_mean_var(W, R, C)
    utility = (mean_1 - rf)/sqrt(var)
    return 1/utility

# Solves for the optimal portfolio weights using the Sharpe ratio 
# maximization objective function.

def solve_weights(R, C, rf):
    n = len(R)
    W = ones([n])/n # Start optimization with equal weights
    b_ = [(0.,1.) for i in range(n)] # Bounds for decision variables
    c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. }) 
    # Constraints - weights must sum to 1
    optimized = scipy.optimize.minimize(fitness, W, (R, C, rf), method='SLSQP', constraints=c_, bounds=b_)
    if not optimized.success:
        raise BaseException(optimized.message)
    return optimized.x    

# Solve for the efficient frontier using the variance + penalty minimization
# function fitness. 

def solve_frontier(R, C, rf):
    frontier_mean, frontier_var, frontier_weights = [], [], []
    n = len(R)      # Number of assets in the portfolio
    for r in linspace(min(R), max(R), num=50): # Iterate through the range of returns on Y axis
        W = ones([n])/n # Set initial guess for weights
        b_ = [(0,1) for i in range(n)] # Set bounds on weights
        c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. }) # Set constraints
        optimized = scipy.optimize.minimize(fitness, W, (R, C, r), method='SLSQP', constraints=c_, bounds=b_)  
        #if not optimized.success:
        #    raise BaseException(optimized.message)
        # Add point to the efficient frontier
        frontier_mean.append(r)
        frontier_var.append(compute_var(optimized.x, C))   # Min-variance based on optimized weights
        frontier_weights.append(optimized.x)
    return array(frontier_mean), array(frontier_var), frontier_weights
        
# Weights - array of asset weights (derived from market capitalizations)
# Expreturns - expected returns based on historical data
# Covars - covariance matrix of asset returns based on historical data

def assets_meanvar(daily_returns, context):    
    
    # Calculate expected returns
    expreturns = array([])
    daily_returns = daily_returns.transpose()
    
    for i in range(0, len(context.securities)):
        expreturns = append(expreturns, mean(daily_returns[i,:]))
    
    # Compute covariance matrix
    covars = cov(daily_returns)
    # Annualize expected returns and covariances
    # Assumes 255 trading days per year    
    expreturns = (1+expreturns)**255-1
    covars = covars * 255
    expreturns = np.array(expreturns)
    
    return expreturns, covars


def initialize(context):
    # Set day
    context.day = 0
    
    # Enter the risk tolerance on a scale of 1 to 20.
    # 1 is the lowest risk tolerance (lowest risk portfolio)
    # 20 is the highest risk tolerance (highest risk portfolio)
    context.risk_tolerance = 20
     
    # Select equities for the portfolio
    # The default selection of equities is the fourteen highest market cap stocks in the S&P 500
    context.securities = [sid(9883),sid(19917),sid(25150), sid(14848), sid(6653), sid(3766), sid(11941)] 
    # Set Max and Min positions in security
    context.max_notional = 1000000.1
    context.min_notional = -1000000.0
    context.previous_month = 0


def handle_data(context, data):    
    
    loc_dt = get_datetime().astimezone(timezone('US/Eastern'))
    date = get_datetime().date()
    
    if loc_dt.month != context.previous_month and context.previous_month != 0:
        all_prices = history(200, '1d', 'price')
        daily_returns = all_prices.pct_change().dropna()
                
        dr = np.array(daily_returns)
        
        (rr,cc) = dr.shape
        
        expreturns, covars = assets_meanvar(dr, context)
        R = expreturns
        C = covars
        rf = 0.015
        expreturns = np.array(expreturns)
        
        frontier_mean, frontier_var, frontier_weights = solve_frontier(R, C, rf)
        
        f_w = array(frontier_weights)          
        (row_1, col_1) = f_w.shape         
  
        # Choose an allocation along the efficient frontier
        wts = frontier_weights[10]
        new_weights = wts  
            
        # Set leverage to 1
        leverage = sum(abs(new_weights))
        portfolio_value = (context.portfolio.positions_value + context.portfolio.cash)/leverage
    
        # Reweight portfolio 
        i = 0
        for sec in context.securities:
            order_target_percent(sec, wts[i])
            log.info(get_datetime())
            i=i+1
        
    context.previous_month = loc_dt.month
