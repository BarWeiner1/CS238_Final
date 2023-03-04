import numpy as np
import itertools

class TradingSimulator:

    def __init__(self, train_data, starting_investment):
        # data
        self.stock_price_history =  # pass in csv's

        # instance attributes
        self.init_invest = starting_invest
        self.cur_action = 0
        self.stock_owned = []
        self.stock_price = 0
        self.money_balance = None

    def explore_trades(self, action):
        # all combo to sell(0), hold(1), or buy(2) stocks
        action_space = map(list, itertools.product([0, 1, 2], repeat=self.n_stock))