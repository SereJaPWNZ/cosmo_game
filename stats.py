class Stats():
    '''отслеживание статистики'''


    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        '''статистика изменяюзаяся во время игры'''
        self.guns_left = 2