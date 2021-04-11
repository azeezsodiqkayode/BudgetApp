from collections import defaultdict


class Budget:
    def __init__(self, categories={}):
        self.categories = defaultdict(int, categories)

    def depositFund(self, category, amount):
        """ Depositing funds to each of the categories """
        self.categories[category] += amount
    
    def withdrawFund(self, category, amount):
        """ Withdrawing funds from each category """
        if category not in self.categories:
            print('Category not in budget. New category added.')
        if amount > self.categories[category]:
            print('Budget for this category exceeded. Withdrawing balance...')
        amount = min(self.categories[category], amount)
        self.categories[category] -= amount
        return amount
    
    def getBalance(self, category):
        """ Computing category balances """
        return self.categories[category]

    def transferBalance(self, fromCategory, toCategory):
        """ Transferring balance amounts between categories """
        self.categories[toCategory] += self.categories[fromCategory]
        self.categories[fromCategory] = 0
    
    def __repr__(self):
        return 'Budget(' + str({k : v for k, v in self.categories.items()}) + ')'


if __name__ == "__main__":
    
    budgetApp = Budget({'clothing': 1000})
    budgetApp.depositFund('food', 5000)
    budgetApp.depositFund('entertainment', 500)
    
    print(budgetApp, '\n')
    print(budgetApp.getBalance('food'), '\n')

    budgetApp.withdrawFund('entertainment', 100)
    print(budgetApp.getBalance('entertainment'), '\n')
    
    budgetApp.withdrawFund('transport', 100)
    print(budgetApp.getBalance('transport'), '\n')
    
    budgetApp.transferBalance('clothing', 'food')
    print(budgetApp.getBalance('food'))
    
