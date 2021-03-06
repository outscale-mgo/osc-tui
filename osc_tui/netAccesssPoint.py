import npyscreen
import pyperclip

import createVm
import main
import popup
import selectableGrid
import virtualMachine

class Grid(selectableGrid.SelectableGrid):
    def __init__(self, screen,  *args, **keywords):
        super().__init__(screen, *args, **keywords)
        self.col_titles = ["Id", "Net ID", "Service Name", "State"]

    def refresh(self):
        groups = main.GATEWAY.ReadNetAccessPoints(form=self.form)['NetAccessPoints']
        values = list()
        for g in groups:
            values.append([g['NetAccessPointId'], g['NetId'], g['ServiceName'],
                           g['State']])
        self.values = values
