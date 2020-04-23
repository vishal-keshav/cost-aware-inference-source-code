config = {
    'API_KEY': '',
    'project_name': 'branchynet_exp',
    'workspace': '',
    # ####################### USE LISTS FOR HPs(GRID SEARCH) ##################
    'learning_rate': [0.001, 0.01, 0.1],
    'nr_epochs': [200],
    'batch_size': [8, 32],
    # ######################### ENABLE THIS FOR HP SEARCH #####################
    # 'metric': 'loss',
    # 'objective': 'minimize',
    # 'algorithm': 'bayes'
}